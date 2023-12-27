"""This file contains all code for calculating tensile stress 
at the bottom of the cross section using Navier's equation."""

import bending_moment as bmd_
import bridge_parameters as bp_

# Calculate applied stresses for moments using Navier's equation. 

# Beam failure resulting from tension (bottom surface to centroidal axis). 
def calculate_tensile_stress() -> float: 
    y = bp_.centroidal_axis(bp_.param)
    I = bp_.second_moment_of_area(bp_.param)
    max_moment = max(bmd_.bmd_envelope_all())

    return round(max_moment * y / I, 3)

# Beam failure resulting from compression (centroidal axis to top surface). 
if __name__ == "__main__":
    tensile_stress = calculate_tensile_stress()

    print("Maximum Tensile Stress [MPa]: " + str(tensile_stress))
