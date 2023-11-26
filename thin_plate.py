import bridge_parameters as bp_

import numpy as np

# matboard params
thickness = 1.27          # mm
E = 4000                  # MPa
poisson = 0.2             # unitles
flange_width = bp_.flange         # mm

# Working
def center():
    global thickness, E, poisson
    k = 4
 
    t = bp_.param[5][2] * bp_.top_layers
    b = bp_.param[5][1] - 2 * flange_width

    """
    print("Center: ")
    print(k, t, b)
    """

    return round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2, 3)

# Working
def free_edge():
    global thickness, E, poisson
    k = 0.425

    t = bp_.param[5][2] * bp_.top_layers
    b = flange_width

    """
    print("Free Edge")
    print(k, t, b)
    """

    # print(round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2, 3))
    return round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2, 3)

# WORKING
def web():
    global thickness, E, poisson
    k = 6

    t = bp_.param[1][1]
    b = 1.27 + bp_.param[1][2] - bp_.centroidal_axis(bp_.param)

    """
    print("Web")
    print(bp_.centroidal_axis(bp_.param))
    print(bp_.param[1][2])
    print(k, bp_.param[1][2], t, b)
    """

    return round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2, 3)

def shear():
    global thickness, E, poisson
    k = 5

    t = bp_.param[1][1]
    h = 1.27 + bp_.param[1][2]

    a = diaphrams()

    # print(k, t, h, a)
    # print(round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * ((t/h)**2 + (t/a)**2), 3))

    return round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * ((t/h)**2 + (t/a)**2), 3)

def diaphrams():
    inner_b = 80 - 2*1.27
    inner_h = bp_.param[2][2]
    inner_area = inner_b * inner_h
    n_diaphrams = (bp_.leftover(bp_.param) - (bp_.leftover(bp_.param) % inner_area))/ inner_area

    n_diaphrams = 2            # override
    a = 1270 / n_diaphrams

    return a