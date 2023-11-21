# Define Bridge Parameters. 
# xb, bft, tft 
# xb:   Location of centroid, xb, of cross-section change (relative to bottom) (mm)
# bft:  Cross Section Width (mm)
# tft:  Cross Section Thickness/Height (mm)

p_0 = [[0.635, 80, 1.27], 
        [37.5, 1.27, 72.46],
        [37.5, 1.27, 72.46],
        [74.365, 6.27, 1.27],
        [74.365, 6.27, 1.27],
        [75.635, 100, 1.27]
        ]

y_0 = 76.27
gl_0 = 75
gw_0 = 2 * 6.27 

# First Iteration: Adding matboard layer to the top to reduce compressive stress. 
p_1 = [[0.635, 80, 1.27], 
        [37.5, 1.27, 72.46],
        [37.5, 1.27, 72.46],
        [74.365, 6.27, 1.27],
        [74.365, 6.27, 1.27],
        [75.635, 100, 1.27],
        [75.635 + 1.27 / 2, 100, 1.27],
        ]

y_1 = 76.27 + 1.27
gw_1 = 2 * 6.27 
a_2 = [0, 1200]

# Second Iteration: Increase length of glue tabs. 
p_2 = [[0.635, 80, 1.27], 
        [37.5, 1.27, 72.46],
        [37.5, 1.27, 72.46],
        [74.365, 40, 1.27],
        [74.365, 40, 1.27],
        [75.635, 100, 1.27]
        ]

y_2 = 76.27 + 1.27
gw_2 = 2 * 40
a_2 = [0, 1200]

# Third Iteration: Increase height of the bridge to 120. 
p_3 = [[0.635, 80, 1.27], 
        [60 + 1.27, 1.27, 120],
        [60 + 1.27, 1.27, 120],
        [1.27 + 120 + 0.635, 1.27, 1.27],
        [1.27 + 120 + 0.635, 1.27, 1.27],
        [1.27 + 120 + 1.27 + 0.635, 100, 1.27]
        ]

y_3 = 120 + 3 * 1.27
gw_3 = 80
a_3 = [0, 1200]

# Fourth Iteration: Decrease width of the top plate to decrease free edge buckling.
p_4 = [[0.635, 80, 1.27], 
        [60 + 1.27, 1.27, 120],
        [60 + 1.27, 1.27, 120],
        [1.27 + 120 + 0.635, 1.27, 1.27],
        [1.27 + 120 + 0.635, 1.27, 1.27],
        [1.27 + 120 + 1.27 + 0.635, 120, 1.27]
        ]

y_4 = 120 + 3 * 1.27
gw_4 = 80
a_4 = [0, 1200]




param = p_4
glue_width = gw_4
diaphram = a_4


top_layers = 2
y_top = param[0][2]
for i in range(1, len(param)):
    if param[i][0] != param[i-1][0]:
        y_top += param[i][2]
glue_location = y_top - top_layers*1.27
flange = (param[len(param) - 1][1] - 80)/2
param_glue = param[-top_layers:]
y_bot = 0 
centroidal_axis_width = 2 * 1.27



























def leftover(param):
    sum = 0
    for i in param:
        if i[1] != 1.27:
            sum += i[1]
            # print(i[1])
        if i[2] != 1.27:
            sum += i[2]
            # print(i[2])

    sum *= 1200
    return 826008 - sum 

def centroidal_axis(param) -> float: 
    """Return the position of the centroidal axis relative to the
    bottom of the cross section in mm."""
    total_area = 0 
    centroid_area = 0

    for cross_section in param: 
        area = cross_section[1] * cross_section[2]

        total_area += area
        centroid_area += area * cross_section[0]

    return round(centroid_area / total_area, 3)


def second_moment_of_area(param) -> float: 
    """Return the second moment of area of the cross section based 
    on parallel axis theorem in mm4."""

    cent_axis = centroidal_axis(param)
    I = 0 

    # Calculate moments about individual centroids. 
    # Assume all pieces are rectangular (I = bh^3 / 12). 
    for cross_section in param: 
        rect_moment = cross_section[1] * cross_section[2] ** 3 / 12  
        parallel_moment = cross_section[1] * cross_section[2] * (cent_axis - cross_section[0]) ** 2 

        I += rect_moment + parallel_moment 

    return round(I, 3)

# First Moment of Area Parameters for Centroidal Axis. 
# Take relative position from the bottom surface of the bridge. 
param_centroidal_axis = [[1.27 / 2, 80, 1.27], 
                         [1.27 + (centroidal_axis(param) - 1.27) / 2, 1.27, centroidal_axis(param) - 1.27], 
                         [1.27 + (centroidal_axis(param) - 1.27) / 2, 1.27, centroidal_axis(param) - 1.27]
                        ]


def calculate_first_moment_of_area(param, axis, glue=False) -> float:     
    first_moment_of_area = 0

    # Keep track of the last cross section's height. 
    # This will indicate which cross sections are not fully within the 
    # first moment of area calculation. 
    last_height = 0
    temp_height = 0
    last_centroid = 0

    # Calculate shaded area.
    for cross_section in param: 
        # Be careful with duplicate sections. 
        # If elements have the same centroid, they will have the same last height.
        if cross_section[0] != last_centroid: 
            last_height = temp_height

        # Check if the cross sections height is below the centroidal axis. 
        height = cross_section[2] + last_height 

        if height <= axis:
            first_moment_of_area += cross_section[1] * cross_section[2] 
        else:
            first_moment_of_area += cross_section[1] * max(0, axis - last_height)
            
        temp_height = height
        last_centroid = cross_section[0]

    # Multiply by distance between centroid of shaded area to centroid of entire section. 
    if glue: 
        shaded_centroid = centroidal_axis(param_glue) 
        first_moment_of_area *= abs(shaded_centroid - centroidal_axis(param))
    else: 
        shaded_centroid = centroidal_axis(param_centroidal_axis)
        first_moment_of_area *= abs(shaded_centroid - centroidal_axis(param))

    return round(first_moment_of_area, 3)
