import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import trapz 
import shear_force as sfd 

# Shear force diagrams. 
shear_force_diagrams = sfd.calculate_sfd()

# Bending moment diagrams. 
left_bmd, middle_bmd, right_bmd = [0] * (sfd.n + 1), [0] * (sfd.n + 1), [0] * (sfd.n + 1)


def calculate_bmd(): 
    # Calculate bending moment diagrams for each SFD. 
    for i in range(sfd.n_train): 
        sfd_values = shear_force_diagrams[i]
        
        # Iterate through 1 mm segments of the bridge. 
        for x_end in range(sfd.n + 1): 
            subsection_sfd = sfd_values[:x_end]
            bending_moment = trapz(subsection_sfd)

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
    bending_moment_diagrams = calculate_bmd() 

    left_max_moment = max(bending_moment_diagrams[0])
    middle_max_moment = max(bending_moment_diagrams[1]) 
    right_max_moment = max(bending_moment_diagrams[2])

    return left_max_moment, middle_max_moment, right_max_moment


if __name__ == "__main__": 
    bending_moment_diagrams = calculate_bmd() 
    
    # Note that all compressions will be given as positive.
    # Refer to the bending moment diagrams to see which signs the moment has.
    print("Moment Envelope (Nmm)")
    print("-" * len("Moment Envelope (Nmm)"))
    print(bmd_envelope())
    
    for bmd in range(len(bending_moment_diagrams)): 
        leg_label = None
        match bmd: 
            case 0: 
                leg_label = "Left BMD"
            case 1: 
                leg_label = "Middle BMD"
            case 2: 
                leg_label = "Right BMD"

        plt.plot(np.array(bending_moment_diagrams[bmd]), label = leg_label)
        
    plt.plot(np.array([0] * (sfd.n + 1)), color="black")

    plt.legend()
    plt.ylim(100000, 0)
    plt.xlabel("Bridge Distance (mm)")
    plt.ylabel("Moment (Nmm)")
    plt.title("Bending Moment Diagrams for Left, Middle, and Right Train Placements")
    plt.show()