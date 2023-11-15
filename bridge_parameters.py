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


def first_moment_of_area_centroidal_axis() -> float: 
    # Take shaded area from bottom of cross section to centroidal axis. 
    cent_axis = centroidal_axis(param)
    
    first_moment_of_area = 0

    # Keep track of the last cross section's height. 
    # This will indicate which cross sections are not fully within the 
    # first moment of area calculation. 

    last_height = 0
    for cross_section in param: 
        # Check if the cross sections height is below the centroidal axis. 
        height = cross_section[0] 
        
        


if __name__ == "__main__":
    print("Centroidal Axis (mm): " + str(centroidal_axis(param)))
    print("Second Moment of Area (mm4): " + str(second_moment_of_area(param)))