import bridge_parameters as bp_

import numpy as np

# matboard params
thickness = 1.27          # mm
E = 4000                  # MPa
poisson = 0.2             # unitless

def top_center():
    global thickness, E, poisson
    k = 4
    t = bp_.param[0][2]
    b = bp_.param[0][1]

    return (k * np.pi * E ) / (12*(1-poisson**2)) * (t/b)**2
    
def free_edge():
    global thickness, E, poisson
    k = 0.425
    t = bp_.param[0][2]
    b = bp_.param[0][1]

    return (k * np.pi * E ) / (12*(1-poisson**2)) * (t/b)**2

def web():
    global thickness, E, poisson
    k = 6
    t = bp_.param[1][2]
    b = bp_.param[1][1]

    return (k * np.pi * E ) / (12*(1-poisson**2)) * (t/b)**2

def shear():
    global thickness, E, poisson
    k = 5
    t = bp_.param[0][2]
    h = bp_.param[0][1]
    a = 50               # to be optimized

    return (k * np.pi * E ) / (12*(1-poisson**2)) * ((t/h)**2 + (t/a)**2)

if __name__ == "__main__":
    print("Top Center (Mpa): " + str(top_center()))
    print("Free Edge (Mpa): " + str(free_edge()))
    print("Web (Mpa): " + str(web()))
    print("Shear (Mpa): " + str(shear()))

