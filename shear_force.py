import numpy as np
import copy

# PARAMETERS
x_train = [52, 228, 392, 568, 732, 908]     # Train Load Locations (mm)
start_locations = [0, 120, 240]
start_locations = [0 + 35, 120 + 35, 240 + 35]
wheel = 66.666
wheel = 149.25
P_train = [wheel, wheel, wheel, wheel, wheel, wheel]          # Load Case 1
P_train = [wheel, wheel, wheel, wheel, wheel * 1.35, wheel * 1.35]        # Load Case 2

L = 1270    # Length of Bridge 
n = 1270    # Discretize into 1 mm segments 

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

            shear_force = round(shear_force, 3)

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