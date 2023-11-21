import bridge_parameters as bp_

import numpy as np

# matboard params
thickness = 1.27          # mm
E = 4000                  # MPa
poisson = 0.2             # unitles
flange_width = bp_.flange         # mm
dia = bp_.diaphram

def center():
    global thickness, E, poisson
    k = 4
 
    t = bp_.param[5][2]
    b = bp_.param[5][1] - 2 * flange_width

    # print(k, t, b)

    return round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2, 3)
    
def free_edge():
    global thickness, E, poisson
    k = 0.425

    t = bp_.param[5][2]
    b = flange_width

    # print(k, t, b)

    # print(round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2, 3))
    return round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2, 3)

def web():
    global thickness, E, poisson
    k = 6

    t = bp_.param[1][1]
    b = bp_.param[1][2] - bp_.centroidal_axis(bp_.param)

    # print(k, t, b)

    return round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2, 3)

def shear():
    global dia
    global thickness, E, poisson
    k = 5

    t = bp_.param[5][2]
    h = bp_.param[5][1]

    max = 0
    for i in range (len(dia) - 1):
        if dia[i+1] - dia[i]  > max:
            max = dia[i+1] - dia[i]
    print(max)
    a = max

    # print(k, t, h, a)

    return round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * ((t/h)**2 + (t/a)**2), 3)