import shear_force as sfd_
import bending_moment as bmd_
import bridge_parameters as bp_

import matplotlib.pyplot as plt
import numpy as np

# Calculate applied stresses for moments using Navier's equation. 

# Beam failure resulting from compression (bottom surface to centroidal axis). 
def calculate_compressive_stress() -> float: 
    # left_compression, middle_compression, right_compression = [0] * (sfd_.n + 1), [0] * (sfd_.n + 1), [0] * (sfd_.n + 1)

    y = bp_.y_top - bp_.centroidal_axis(bp_.param) 
    I = bp_.second_moment_of_area(bp_.param)
    max_moment = max(bmd_.bmd_envelope_all())

    """
    for i in range(len(bmds)): 
        for pos in range(sfd_.n + 1): 
            moment = round(bmds[i][pos] * y / I, 3)
            
            match i: 
                case 0: 
                    left_compression[pos] = moment
                    
                case 1: 
                    middle_compression[pos] = moment 

                case 2: 
                    right_compression[pos] = moment
            
    return [left_compression, middle_compression, right_compression]
    """
    return round(max_moment * y / I, 3)

# Beam failure resulting from compression (centroidal axis to top surface). 

if __name__ == "__main__":
    compressive_stresses = calculate_compressive_stress(bmd_.calculate_bmd_right_middle_left())

    for stress in range(len(compressive_stresses)):
        leg_label = None 

        match stress: 
            case 0: 
                leg_label = "Left Stress"
            case 1: 
                leg_label = "Middle Stress"
            case 2: 
                leg_label = "Right Stress"

        plt.plot(np.array(compressive_stresses[stress]), label = leg_label)

    print("Maximum Compressive Stress [MPa]: " + str(max(compressive_stresses[1])))

    plt.legend()
    plt.xlabel("Bridge Distance (mm)")
    plt.ylabel("Compressive Stress (MPa)")
    plt.title("Compressive Stress Diagrams for Left, Middle, and Right Train Placements")
    plt.show()