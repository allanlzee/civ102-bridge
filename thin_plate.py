import bridge_parameters as bp_

import numpy as np

# matboard params
thickness = 1.27          # mm
E = 4000                  # MPa
poisson = 0.2             # unitles
flange_width = bp_.flange         # mm

def center():
    global thickness, E, poisson
    k = 4
    t = 2*1.27
    b = 80
    
    crit = round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2, 3)

    return crit
    
def free_edge():
    global thickness, E, poisson
    k = 0.425

    t = 2*1.27
    b = flange_width

    crit = round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2, 3)
    return crit

def web():
    global thickness, E, poisson
    k = 6

    t = bp_.param[1][1]
    b = 140 - 2*1.27 -  bp_.centroidal_axis(bp_.param)

    return round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2, 3)

def shear():
    global thickness, E, poisson
    k = 5

    t = 1.27
    h = 140 - 3*1.27

    a = diaphrams()

    return round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * ((t/h)**2 + (t/a)**2), 3)

def diaphrams():
    inner_b = 80 - 2*1.27
    inner_h = bp_.param[2][2]
    inner_area = inner_b * inner_h
    n_diaphrams = (bp_.leftover(bp_.param) - (bp_.leftover(bp_.param) % inner_area))/ inner_area

    n_diaphrams = 12               # override
    a = 1270 / (n_diaphrams-1)

    return a