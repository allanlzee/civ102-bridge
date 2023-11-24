import shear_force as sfd_
import bending_moment as bmd_
import bridge_parameters as bp_

import matplotlib.pyplot as plt
import numpy as np

# Calculate applied stresses for moments using Navier's equation. 

# Beam failure resulting from compression (bottom surface to centroidal axis). 
def calculate_compressive_stress(bmds): 
    left_compression, middle_compression, right_compression = [0] * (sfd_.n + 1), [0] * (sfd_.n + 1), [0] * (sfd_.n + 1)

    y = bp_.y_top - bp_.centroidal_axis(bp_.param) 
    I = bp_.second_moment_of_area(bp_.param)

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

# Beam failure resulting from compression (centroidal axis to top surface). 