import shear_force as sfd_
import bending_moment as bmd_
import bridge_parameters as bp_

import matplotlib.pyplot as plt
import numpy as np

# Calculate applied stresses for moments using Navier's equation. 

# Beam failure resulting from tension (bottom surface to centroidal axis). 
def calculate_tensile_stress(bmds) -> list: 
    left_tension, middle_tension, right_tension = [0] * (sfd_.n + 1), [0] * (sfd_.n + 1), [0] * (sfd_.n + 1)

    y = bp_.centroidal_axis(bp_.param)
    I = bp_.second_moment_of_area(bp_.param)

    for i in range(len(bmds)): 
        for pos in range(sfd_.n + 1): 
            moment = round(bmds[i][pos] * y / I, 3)
            
            match i: 
                case 0: 
                    left_tension[pos] = moment
                    
                case 1: 
                    middle_tension[pos] = moment 

                case 2: 
                    right_tension[pos] = moment
            
    return [left_tension, middle_tension, right_tension]

# Beam failure resulting from compression (centroidal axis to top surface). 
