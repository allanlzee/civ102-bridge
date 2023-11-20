import numpy as np
import matplotlib.pyplot as plt 
import copy

# PARAMETERS
x_train = [52, 228, 392, 568, 732, 908]     # Train Load Locations (mm)
start_locations = [0, 120, 240]
P_train = [66, 66, 66, 66, 66, 66]          # Load Case 1
# P_train = [66, 66, 66, 66, 90, 90]        # Load Case 2

L = 1200    # Length of Bridge 
n = 1200    # Discretize into 1 mm segments 

x = [] 
for i in range(1201): 
    x.append(i)
x = np.array(x) 

P = sum(P_train)
n_train = 3     # Number of train locations 
SFDi = []
BMDi = [] 

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
        right_pin_reaction = wheel_moments_left_pin / L   # N 
        
        # Sum of vertical forces.
        left_pin_reaction = P - right_pin_reaction    # N

        # Initial shear force = left pin
        shear_force = left_pin_reaction
        for cut_position in range(n + 1): 
            # If cur position is at wheel, drop down SFD by wheel force.
            for wheel in range(len(wheel_locations)):
                if wheel_locations[wheel] == cut_position: 
                    shear_force -= P_train[wheel]

            match start: 
                case 0: 
                    left_sfd[cut_position] = shear_force
                    
                case 1: 
                    middle_sfd[cut_position] = shear_force 

                case 2: 
                    right_sfd[cut_position] = shear_force 

        # Add right pin reaction in the end
        shear_force += right_pin_reaction

    return [left_sfd, middle_sfd, right_sfd]


def sfd_envelope(): 
    shear_force_diagrams = calculate_sfd() 

    left_max_shear = max(max(shear_force_diagrams[0]), abs(min(shear_force_diagrams[0])))
    middle_max_shear = max(max(shear_force_diagrams[1]), abs(min(shear_force_diagrams[1])))
    right_max_shear = max(max(shear_force_diagrams[2]), abs(min(shear_force_diagrams[2])))

    return left_max_shear, middle_max_shear, right_max_shear

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
    plt.ylim(-300, 300)
    plt.xlabel("Bridge Distance (mm)")
    plt.ylabel("Shear Force (N)")
    plt.title("Shear Force Diagrams for Left, Middle, and Right Train Placements")
    plt.show()