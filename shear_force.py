import numpy as np
import copy

# PARAMETERS
x_train = [52, 228, 392, 568, 732, 908]     # Train Load Locations (mm)
start_locations = [-52, 120, 292]
#start_locations = [0 + 35, 120 + 35, 240 + 35]
wheel = 66.666
#wheel = 149.254
P_train = [wheel, wheel, wheel, wheel, wheel, wheel]          # Load Case 1
#P_train = [wheel, wheel, wheel, wheel, wheel * 1.35, wheel * 1.35]        # Load Case 2

L = 1200   # Length of Bridge 
n = 1200    # Discretize into 1 mm segments ()

x = [] 
for i in range(1201): 
    x.append(i)
x = np.array(x) 

P = sum(P_train)
n_train = 3     # Number of train locations 
SFDi = []
BMDi = [] 

left_sfd, middle_sfd, right_sfd = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
sfd_all_locations = [] 

# Take starting positions for the train being fully on the bridge (1200 mm between the supports).
for loc in range(292 + 52 + 1): 
    sfd_all_locations.append([0] * (n + 1))


def calculate_sfd_right_middle_left():
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

    # Add right pin reaction in the end.
    match start: 
        case 0: 
            left_sfd[-1] += right_pin_reaction
                    
        case 1: 
            middle_sfd[-1] += right_pin_reaction

        case 2: 
            right_sfd[-1] += right_pin_reaction

    return left_sfd, middle_sfd, right_sfd


def calculate_sfd():
    global left_sfd 
    global middle_sfd 
    global right_sfd 

    # SFD calculations neglect the self-weight of the bridge.
    for start in range(-52, 292 + 1):
        wheel_locations = copy.deepcopy(x_train)

        # Get wheel positions for each starting position.
        for i in range(len(wheel_locations)):
            wheel_locations[i] += start

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
        for cut_position in range(n - 1): 
            # If cur position is at wheel, drop down SFD by wheel force.
            for wheel in range(len(wheel_locations)):
                if wheel_locations[wheel] == cut_position: 
                    shear_force -= P_train[wheel]

            shear_force = round(shear_force, 3)

            sfd_all_locations[start + 52][cut_position] = shear_force

        # Add right pin reaction in the end.
        sfd_all_locations[start + 52][-1] += right_pin_reaction

    for i in range(len(sfd_all_locations)):
        sfd_all_locations[i] = sfd_all_locations[i][:1199]

    return sfd_all_locations


def sfd_envelope(): 
    shear_force_diagrams = calculate_sfd_right_middle_left() 

    left_max_shear = max(max(shear_force_diagrams[0]), abs(min(shear_force_diagrams[0])))
    middle_max_shear = max(max(shear_force_diagrams[1]), abs(min(shear_force_diagrams[1])))
    right_max_shear = max(max(shear_force_diagrams[2]), abs(min(shear_force_diagrams[2])))

    return left_max_shear, middle_max_shear, right_max_shear


def sfd_envelope_all():
    shear_force_diagrams = calculate_sfd() 
    max_shear = []
    min_shear = []

    abs_total_shear = []

    # Find the maximum shear force at each position.
    # Note that if a shear force is negative, its absolute value should be taken.
    for col in range(len(shear_force_diagrams[0])):
        max_shear_force = 0
        min_shear_force = 1000000000
        for row in range(len(shear_force_diagrams)): 
            if shear_force_diagrams[row][col] > max_shear_force: 
                max_shear_force = shear_force_diagrams[row][col]
            
            if shear_force_diagrams[row][col] < min_shear_force: 
                min_shear_force = shear_force_diagrams[row][col]

        max_shear.append(max_shear_force)
        
        min_shear.append(min_shear_force)

    for i in range(len(max_shear)): 
        if max_shear[i] > abs(min_shear[i]):   
            abs_total_shear.append(max_shear[i])
        else:
            abs_total_shear.append(min_shear[i])

    abs_total_shear.insert(0, 0)
    abs_total_shear.append(0)

    return abs_total_shear[:1201]


if __name__ == "__main__":
    print(calculate_sfd_right_middle_left()[2])
    print(sfd_envelope_all())