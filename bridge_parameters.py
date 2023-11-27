"""This file contains all code related to the geometry of the bridge cross section, 
left over Matboard, first and second moment of area, and centroidal axis."""

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

# First Iteration: Adding matboard layer to the top to reduce compressive stress. 
p_1 = [[0.635, 80, 1.27], 
        [37.5, 1.27, 72.46],
        [37.5, 1.27, 72.46],
        [74.365, 6.27, 1.27],
        [74.365, 6.27, 1.27],
        [75.635, 100, 1.27],
        [75.635 + 1.27, 100, 1.27]
        ]

# Second Iteration: Increase length of glue tabs all the way to the middle. 
p_2 = [[0.635, 80, 1.27], 
        [37.5, 1.27, 72.46],
        [37.5, 1.27, 72.46],
        [74.365, 40, 1.27],
        [74.365, 40, 1.27],
        [75.635, 100, 1.27],
        [75.635 + 1.27, 100, 1.27]
        ]

# Third Iteration: Increase height of the bridge to 140. 
h_3 = 140 
p_3 = [[0.635, 80, 1.27], 
        [(h_3 - 4 * 1.27) / 2 + 1.27, 1.27, h_3 - 4 * 1.27],
        [(h_3 - 4 * 1.27) / 2 + 1.27, 1.27, h_3 - 4 * 1.27],
        [h_3 - 2 * 1.27 - 0.635, 6.27, 1.27],
        [h_3 - 2 * 1.27 - 0.635, 6.27, 1.27],
        [h_3 - 1.27 - 0.635, 100, 1.27],
        [h_3 - 0.635, 100, 1.27]
        ]

# Fourth Iteration: Increase width of the top plate to decrease free edge buckling.
h_4 = 140 
p_4 = [[0.635, 80, 1.27], 
        [(h_4 - 4 * 1.27) / 2 + 1.27, 1.27, h_4 - 4 * 1.27],
        [(h_4 - 4 * 1.27) / 2 + 1.27, 1.27, h_4 - 4 * 1.27],
        [h_4 - 2 * 1.27 - 0.635, 6.27, 1.27],
        [h_4 - 2 * 1.27 - 0.635, 6.27, 1.27],
        [h_4 - 1.27 - 0.635, 120, 1.27],
        [h_4 - 0.635, 120, 1.27]
        ]

# Fifth Iteration: Adding a bottom layer. # TODO: change code for centroidal axis.
h_5 = 140
p_5 = [[0.635, 80, 1.27],
       [0.635 + 1.27, 80, 1.27], 
       [(h_5 - 5 * 1.27) / 2 + 2 * 1.27, 1.27, h_5 - 5 * 1.27],
       [(h_5 - 5 * 1.27) / 2 + 2 * 1.27, 1.27, h_5 - 5 * 1.27],
       [h_5 - 2 * 1.27 - 0.635, 6.27, 1.27],
       [h_5 - 2 * 1.27 - 0.635, 6.27, 1.27],
       [h_5 - 1.27 - 0.635, 100, 1.27],
       [h_5 - 0.635, 100, 1.27]
      ]

# Sixth Iteration: Failure by compression counteracted by raising centroidal axis. 
# TODO: change top layer number to 3
h_6 = 140
p_6 = [[0.635, 80, 1.27], 
        [(h_6 - 5 * 1.27) / 2 + 1.27, 1.27, h_6 - 5 * 1.27],
        [(h_6 - 5 * 1.27) / 2 + 1.27, 1.27, h_6 - 5 * 1.27],
        [h_6 - 3 * 1.27 - 0.635, 6.27, 1.27],
        [h_6 - 3 * 1.27 - 0.635, 6.27, 1.27],
        [h_6 - 2 * 1.27 - 0.635, 100, 1.27],
        [h_6 - 1.27 - 0.635, 100, 1.27], 
        [h_6 - 0.635, 100, 1.27]
        ]

# ---------

# Seventh Iteration: Taking off the bottom layer.
# TODO: change centroidal axis to bottomless layer.
p_7 = [[0, 0, 0], 
        [137.46 / 2 + 1.27, 1.27, 137.46],
        [137.46 / 2 + 1.27, 1.27, 137.46],
        [140 - 2 * 1.27 - 0.635, 6.27, 1.27],
        [140 - 2 * 1.27 - 0.635, 6.27, 1.27],
        [140 - 1.27 - 0.635, 100, 1.27],
        [140 - 0.635, 100, 1.27]
        ]

"""
# Eighth Iteration: Optimize for height to fix FOS for shear thin plate.
p_8 = [[0.635, 80, 1.27], 
        [(180 - 3 * 1.27) / 2 + 1.27, 1.27, 180 - 3 * 1.27],
        [(180 - 3 * 1.27) / 2 + 1.27, 1.27, 180 - 3 * 1.27],
        [(180 - 3 * 1.27) + 0.635, 5, 1.27],
        [(180 - 3 * 1.27) + 0.635, 5, 1.27],
        [180 - 0.635, 140, 1.27]
        ]

h_9 = 180
p_9 = [ [0, 0, 0],
        [(h_9 - 2 * 1.27) / 2, 1.27, h_9 - 2 * 1.27],
        [(h_9 - 2 * 1.27) / 2, 1.27, h_9 - 2 * 1.27],
        [(h_9 - 2 * 1.27) + 0.635, 5, 1.27],
        [(h_9 - 2 * 1.27) + 0.635, 5, 1.27],
        [h_9 - 1.27, 120, 2* 1.27],
        ]

h_10 = 180
p_10 = [ [0, 0, 0],
        [(h_10 - 3 * 1.27) / 2, 1.27, h_10 - 3 * 1.27],
        [(h_10 - 3 * 1.27) / 2, 1.27, h_10 - 3 * 1.27],
        [(h_10 - 3 * 1.27) + 0.635, 5, 1.27],
        [(h_10 - 3 * 1.27) + 0.635, 5, 1.27],
        [h_10 - 1.27, 140, 2* 1.27],
        ]
"""

h_8 = 160
final_design = [[0, 0, 0],
        [(h_8 - 3 * 1.27) / 2, 1.27, h_8 - 3 * 1.27],
        [(h_8 - 3 * 1.27) / 2, 1.27, h_8 - 3 * 1.27],
        [(h_8 - 3 * 1.27) + 0.635, 6.27, 1.27],
        [(h_8 - 3 * 1.27) + 0.635, 6.27, 1.27],
        [h_8 - 1.27 - 0.635, 100, 1.27],
        [h_8 - 0.635, 100, 1.27],
        ]

param = final_design

top_layers = 2
y_top = param[0][2]
for i in range(1, len(param)):
    if param[i][0] != param[i-1][0]:
        y_top += param[i][2]
glue_location = y_top - top_layers*1.27
flange = (param[len(param) - 1][1] - 80)/2

param_glue = param[0:len(param) - top_layers]

# Note that glue width will not go all the way to the edge.
glue_width = 6.27 * 2
y_bot = 0 
centroidal_axis_width = 2 * 1.27


def leftover(param) -> float:
    """Return leftover matboard in mm2."""
    sum = 0
    for i in param:
        if i[1] != 1.27:
            sum += i[1]
        if i[2] != 1.27:
            sum += i[2]

    sum *= 1270
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

# For one bottom layer. 
param_centroidal_axis_one_bottom_layer = [[0.635, 80, 1.27],
                         [1.27 + (centroidal_axis(param) - 1.27) / 2, 1.27, centroidal_axis(param) - 1.27], 
                         [1.27 + (centroidal_axis(param) - 1.27) / 2, 1.27, centroidal_axis(param) - 1.27]
                        ]

# For two bottom layers.
param_centroidal_axis_two_bottom_layers = [[0.635, 80, 1.27],
                         [1.27 + 1.27 / 2, 80, 1.27], 
                         [1.27 + 1.27 + (centroidal_axis(param) - 2 * 1.27) / 2, 1.27, centroidal_axis(param) - 2 * 1.27], 
                         [1.27 + 1.27 + (centroidal_axis(param) - 2 * 1.27) / 2, 1.27, centroidal_axis(param) - 2 * 1.27]
                        ]

# First Moment of Area Parameters without the Bottom Layer.
param_centroidal_axis_no_bottom_layer = [
                         [(centroidal_axis(param)) / 2, 1.27, centroidal_axis(param)], 
                         [(centroidal_axis(param)) / 2, 1.27, centroidal_axis(param)]
                        ]                


def calculate_first_moment_of_area(param, axis, glue=False) -> float:   
    """Calculate the first moment of area for the centroidal axis and glue axis.""" 

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
        shaded_centroid = centroidal_axis(param_centroidal_axis_no_bottom_layer)
        first_moment_of_area *= abs(shaded_centroid - centroidal_axis(param))

    return first_moment_of_area
