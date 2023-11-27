import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import trapz 
import shear_force as sfd 

# Shear force diagrams. 
shear_force_diagrams_right_middle_left = sfd.calculate_sfd_right_middle_left()
shear_force_diagrams = sfd.calculate_sfd()

# Bending moment diagrams. 
left_bmd, middle_bmd, right_bmd = [0] * (sfd.n + 1), [0] * (sfd.n + 1), [0] * (sfd.n + 1)


def calculate_bmd(): 
    bmd = [] 

    for i in range(len(shear_force_diagrams) + 1): 
        bmd.append([0] * (sfd.n + 1))

    # Calculate bending moment diagrams for each SFD. 
    for i in range(len(shear_force_diagrams)): 
        sfd_values = shear_force_diagrams[i]
        
        # Iterate through 1 mm segments of the bridge. 
        for x_end in range(sfd.n + 1): 
            subsection_sfd = sfd_values[:x_end]
            bending_moment = round(trapz(subsection_sfd), 3)

            if x_end == sfd.n: 
                bending_moment = 0 
            
            bmd[i][x_end] = bending_moment

    return bmd


def calculate_bmd_right_middle_left(): 
    # Calculate bending moment diagrams for each SFD. 
    for i in range(sfd.n_train): 
        sfd_values = shear_force_diagrams_right_middle_left[i]
        
        # Iterate through 1 mm segments of the bridge. 
        for x_end in range(sfd.n + 1): 
            subsection_sfd = sfd_values[:x_end]
            bending_moment = round(trapz(subsection_sfd), 3)

            if x_end == sfd.n: 
                bending_moment = 0 
            
            match i: 
                case 0:
                    left_bmd[x_end] = bending_moment 
                case 1: 
                    middle_bmd[x_end] = bending_moment
                case 2: 
                    right_bmd[x_end] = bending_moment

    return [left_bmd, middle_bmd, right_bmd]


def bmd_envelope(): 
    bending_moment_diagrams = calculate_bmd_right_middle_left() 

    left_max_moment = max(bending_moment_diagrams[0])
    middle_max_moment = max(bending_moment_diagrams[1]) 
    right_max_moment = max(bending_moment_diagrams[2])

    return left_max_moment, middle_max_moment, right_max_moment


def bmd_envelope_all(): 
    bending_moment_diagrams = calculate_bmd() 
    max_moment = []

    # Find the maximum bending moment at each position. 
    for col in range(len(bending_moment_diagrams[0])): 
        max_bending_moment = 0 
        for row in range(len(bending_moment_diagrams)): 
            if (abs(bending_moment_diagrams[row][col])) > max_bending_moment: 
                max_bending_moment = abs(bending_moment_diagrams[row][col])

        max_moment.append(max_bending_moment)

    return max_moment


if __name__ == "__main__": 
    bending_moment_diagrams_right_middle_left = calculate_bmd_right_middle_left() 
    bending_moment_diagrams = calculate_bmd()
    
    # Note that all compressions will be given as positive.
    # Refer to the bending moment diagrams to see which signs the moment has.
    print("Moment Envelope (Nmm)")
    print("-" * len("Moment Envelope (Nmm)"))
    print(bmd_envelope())

    print(max(bmd_envelope_all()))

    for bmd in bending_moment_diagrams: 
        plt.plot(np.array(bmd))

    for bmd in range(len(bending_moment_diagrams_right_middle_left)): 
        leg_label = None
        match bmd: 
            case 0: 
                leg_label = "Left BMD"
            case 1: 
                leg_label = "Middle BMD"
            case 2: 
                leg_label = "Right BMD"

        plt.plot(np.array(bending_moment_diagrams_right_middle_left[bmd]), label = leg_label, linewidth=3.5)
        
    plt.plot(np.array([0] * (sfd.n + 1)), color="black")

    plt.legend()
    plt.xlabel("Bridge Distance (mm)")
    plt.ylabel("Moment (Nmm)")
    plt.title("Bending Moment Diagrams for Moving Placements - Design 0, Load Case 1")
    plt.show()