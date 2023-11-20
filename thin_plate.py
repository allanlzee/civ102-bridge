import bridge_parameters as bp_

import numpy as np

# matboard params
thickness = 1.27          # mm
E = 4000                  # MPa
poisson = 0.2             # unitles
flange_width = 10         # mm

def center():
    global thickness, E, poisson
    k = 4
 
    t = bp_.param[5][2]
    b = bp_.param[5][1] - 2 * flange_width

    # print(k, t, b)

    return (k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2
    
def free_edge():
    global thickness, E, poisson
    k = 0.425

    t = bp_.param[5][2]
    b = flange_width

    # print(k, t, b)

    return (k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2

def web():
    global thickness, E, poisson
    k = 6

    t = bp_.param[1][1]
    b = bp_.param[1][2]

    # print(k, t, b)

    return (k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2

def shear():
    global thickness, E, poisson
    k = 5

    t = bp_.param[5][2]
    h = bp_.param[5][1] - 2*flange_width
    a = 1200                      # to be optimized

    # print(k, t, h, a)

    return (k * np.pi**2 * E ) / (12*(1-poisson**2)) * ((t/h)**2 + (t/a)**2)

if __name__ == "__main__":
    print("Bottom Center (MPa): " + str(center()))
    print("Overhangs (MPa): " + str(free_edge()))
    print("Web (MPa): " + str(web()))
    print("Top Center (MPa): " + str(shear()))

