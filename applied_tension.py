import shear_force as sfd_
import bending_moment as bmd_
import bridge_parameters as bp_

import matplotlib.pyplot as plt
import numpy as np

# Calculate applied stresses for moments using Navier's equation. 

# Beam failure resulting from tension (bottom surface to centroidal axis). 
def calculate_tensile_stress() -> float: 
    # left_tension, middle_tension, right_tension = [0] * (sfd_.n + 1), [0] * (sfd_.n + 1), [0] * (sfd_.n + 1)

    y = bp_.centroidal_axis(bp_.param)
    I = bp_.second_moment_of_area(bp_.param)
    max_moment = max(bmd_.bmd_envelope_all())

    """
    for i in range(len(bmds)): 
        for pos in range(sfd_.n + 1): 
            moment = round(max_moment * y / I, 3)
            
            match i: 
                case 0: 
                    left_tension[pos] = moment
                    
                case 1: 
                    middle_tension[pos] = moment 

                case 2: 
                    right_tension[pos] = moment
    
            
    return [left_tension, middle_tension, right_tension]
    """

    return round(max_moment * y / I, 3)

# Beam failure resulting from compression (centroidal axis to top surface). 

if __name__ == "__main__":
    tensile_stress = calculate_tensile_stress()

    """
    for stress in range(len(tensile_stresses)):
        leg_label = None 

        match stress: 
            case 0: 
                leg_label = "Left Stress"
            case 1: 
                leg_label = "Middle Stress"
            case 2: 
                leg_label = "Right Stress"

        plt.plot(np.array(tensile_stresses[stress]), label = leg_label)
    """

    print("Maximum Tensile Stress [MPa]: " + str(tensile_stress))

    """
    plt.legend()
    plt.xlabel("Bridge Distance (mm)")
    plt.ylabel("Tensile Stress (MPa)")
    plt.title("Tensile Stress Diagrams for Left, Middle, and Right Train Placements")
    plt.show()
    """