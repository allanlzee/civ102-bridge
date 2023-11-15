import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import trapz
import copy

# Initialize Parameters 
L = 1200    # Length of Bridge 
n = 1200    # Discretize into 1 mm segments 
P = 400     # Total Weight of Train [N]
x = [] 

for i in range(1201): 
    x.append(i)

x = np.array(x)     # X Axis 

# 1. SFD, BMD Under Train Loading 
x_train = [52, 228, 392, 568, 732, 908]     # Train Load Locations (mm)
P_train = [1, 1, 1, 1, 1, 1]                # Train Load Forces (N)

for p in range(len(P_train)): 
    P_train[p] *= P / 6 

n_train = 3     # Number of train locations 
SFDi = []
BMDi = [] 

# Start Positions 
# -52: last wheel on left pin support 
# 84: train centered in middle 
# 292: first wheel on right pin support 
start_locations = [-52, 120, 292]

left_sfd, middle_sfd, right_sfd = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)

def calculate_sfd():
    global left_sfd 
    global middle_sfd 
    global right_sfd 

    # SFD calculations neglect the self-weight of the bridge.
    for start in range(len(start_locations)):
        wheel_locations = copy.deepcopy(x_train)

        # Get wheel positions for each starting position.
        for i in range(len(wheel_locations)):
            wheel_locations[i] += start_locations[start]

        # Calculate reaction force on left pin (N). 
        wheel_moments_left_pin = 0 
        for wheel in range(len(wheel_locations)): 
            wheel_moments_left_pin += wheel_locations[wheel] * P_train[wheel]   # Nmm
    
        # Sum of moments (0) = -(Train Moment) + Ry x 1200
        left_pin_reaction = wheel_moments_left_pin / L   # N 
        
        # Sum of vertical forces.
        right_pin_reaction = P - left_pin_reaction    # N

        # Iterate through each dissection of the bridge. 
        for cut_position in range(n + 1): 
            shear_force = 0

            # Add left pin reaction force. 
            if cut_position >= 1: 
                shear_force += left_pin_reaction 

            # Add right pin reaction force 
            if cut_position >= L:
                shear_force += right_pin_reaction

            # Add forces applied by the wheels. 
            for wheel in range(len(wheel_locations)):
                if wheel_locations[wheel] <= cut_position: 
                    shear_force -= P_train[wheel]

            if cut_position == 0: 
                shear_force = 0

            match start: 
                case 0: 
                    left_sfd[cut_position] = shear_force
                    
                case 1: 
                    middle_sfd[cut_position] = shear_force 

                case 2: 
                    right_sfd[cut_position] = shear_force 

    return [left_sfd, middle_sfd, right_sfd]


if __name__ == "__main__":
    shear_force_diagrams = calculate_sfd()

    for sfd in range(len(shear_force_diagrams)): 
        leg_label = None
        match sfd: 
            case 0: 
                leg_label = "Left SFD"
            case 1: 
                leg_label = "Middle SFD"
            case 2: 
                leg_label = "Right SFD"
            
        plt.plot(np.array(shear_force_diagrams[sfd]), label = leg_label)
        
    plt.plot(np.array([0] * (n + 1)), color="black")

    plt.legend()
    plt.ylim(-500, 500)
    plt.xlabel("Bridge Distance (mm)")
    plt.ylabel("Shear Force (N)")
    plt.title("Shear Force Diagrams for Left, Middle, and Right Train Placements")
    plt.show()