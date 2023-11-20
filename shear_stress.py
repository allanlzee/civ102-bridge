import shear_force as sfd_
import bridge_parameters as bp_
import main as m_

# Calculate maximum shear stress from SFD
# Txy = VQ / Ib
max_shear_forces = sfd_.sfd_envelope()

max_shear_stress = [0, 0, 0]


def axis_shear(glue_point: False): 
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

    for i in range(len(max_shear_stress)):
        max_shear_stress[i] = (max_shear_forces[i] * Q) / (I * b)

    return max_shear_stress


if __name__ == "__main__": 
    m_.shear_stress()