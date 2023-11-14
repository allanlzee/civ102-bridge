import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import trapz

# Initialize Parameters 
L = 1200    # Length of Bridge 
n = 1200    # Discretize into 1 mm segments 
P = 400     # Total Weight of Train [N]
x = [] 

for i in range(1201): 
    x.append(i)

x = np.array(x)     # X Axis 

# 1. SFD, BMD Under Train Loading 
x_train = [52, 228, 392, 568, 732, 908]     # Train Load Locations 
P_train = [1, 1, 1, 1, 1, 1] 

for p in range(len(P_train)): 
    P_train[p] *= P / 6 

n_train = 3     # Number of train locations 
SFDi = []
BMDi = [] 

for i in range(n_train): 
    SFDi.append([0] * (n + 1))      # 1 SFD for each train location. 
    BMDi.append([0] * (n + 1))      # 1 BMD for each train location.

print(len(SFDi))
print(len(BMDi))

# Solve for SFD and BMD with the train at different locations. 
for i in range(n_train): 
    # Start location of train. 
    # Consider when train is fully on the bridge. 
    for start_pos in range(n + 1):
        # Get indices of front wheel and back wheel. 
        front_wheel = 2 * i + 1 
        back_wheel = 2 * i

        # Get locations of front wheel and back wheel. 
        front_wheel_pos = x_train[front_wheel] + start_pos 
        back_wheel_pos = x_train[front_wheel] + start_pos

        # Sum of moments at A equation to calculate right pin reaction force.
        # M = 0 = -(front wheel)(front wheel force) - (back wheel)(back wheel force) + (right pin)(1200)
        # Calculates in N mm. 
        right_pin_reaction_force = (front_wheel_pos * P_train[front_wheel] + back_wheel_pos * P_train[back_wheel]) / L 

        # Sum of Fy equation. 
        left_pin_reaction_force = P - right_pin_reaction_force

        # Construct applied loads. 
        # w(x)
        # Assume the self-weight of the bridge is negligible. 
        # Sum of forces y = 0 = -V + Ry + Ly - front wheel - back wheel 
        shear_force = right_pin_reaction_force - P_train[front_wheel] - P_train[back_wheel]
        SFDi[i][start_pos] = shear_force

    # SFD = num. integral(w)
    # BMD = num.integral(SFD)
    # SFD = trapz(10)
    # BMD = trapz(SFD)

print(SFDi[0])

SFD = 0    # SFD Envelope

for cart in range(len(SFDi)): 
    for pos in range(n + 1): 
        if abs(SFDi[cart][pos]) > SFD:
            SFD = abs(SFDi[cart][pos])

BMD = max(BMDi)     # BMD Envelope

# Y Axis of Shear Force Diagram 
y_shear_force = np.array(SFDi[0])

plt.plot(x, y_shear_force)
plt.show()