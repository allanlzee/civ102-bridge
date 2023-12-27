import shear_force as sfd_
import bridge_parameters as bp_

# Calculate maximum shear stress from SFD
# Txy = VQ / Ib
max_shear_forces = sfd_.sfd_envelope_all()

def axis_shear(glue_point: False) -> int: 
    Q = 0
    if glue_point: 
        Q = bp_.calculate_first_moment_of_area(bp_.param, bp_.glue_location, True)
    else: 
        Q = bp_.calculate_first_moment_of_area(bp_.param, bp_.centroidal_axis(bp_.param), False)
    
    I = bp_.second_moment_of_area(bp_.param)
    b = 0

    if glue_point: 
        b = bp_.glue_width
    else:
        b = bp_.centroidal_axis_width

    max_shear_stress = round((max(max_shear_forces) * Q) / (I * b), 3)

    return max_shear_stress


if __name__ == "__main__": 
    print("Centroidal Axis [MPa]: " + str(axis_shear(False)))
    print("Glue Point [MPa]: " + str(axis_shear(True))) 