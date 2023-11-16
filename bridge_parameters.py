# Define Bridge Parameters. 
# xb, bft, tft 
# xb:   Location of centroid, xb, of cross-section change (relative to bottom) (mm)
# bft:  Cross Section Width (mm)
# tft:  Cross Section Thickness/Height (mm)
param = [[0.635, 80, 1.27], 
         [37.5, 1.27, 72.46],
         [37.5, 1.27, 72.46],
         [74.365, 6.27, 1.27],
         [74.365, 6.27, 1.27],
         [75.635, 100, 1.27]
        ]

y_bot = 0 
y_top = 76.27
glue_location = 73.73

def centroidal_axis(param) -> float: 
    """Return the position of the centroidal axis relative to the
    bottom of the cross section in mm."""
    total_area = 0 
    centroid_area = 0

    for cross_section in param: 
        area = cross_section[1] * cross_section[2]

        total_area += area
        centroid_area += area * cross_section[0]

    return centroid_area / total_area


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

    return I


def calculate_first_moment_of_area(param, axis) -> float:     
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

    return first_moment_of_area
        

if __name__ == "__main__":
    print("Centroidal Axis (mm): " + str(centroidal_axis(param)))
    print("Second Moment of Area (mm4): " + str(second_moment_of_area(param)))
    print("First Moment of Area (Centroidal Axis to Bottom) [mm3]: " + str(calculate_first_moment_of_area(param, centroidal_axis(param))))
    print("First Moment of Area (Glue to Centroidal Axis) [mm3]: " + str(calculate_first_moment_of_area(param, glue_location)))