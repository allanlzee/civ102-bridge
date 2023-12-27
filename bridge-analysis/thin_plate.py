import bridge_parameters as bp_

import numpy as np

# Matboard properties.
thickness = 1.27          # mm
E = 4000                  # MPa
poisson = 0.2             # unitles
flange_width = bp_.flange         # mm


def center():
    global thickness, E, poisson
    k = 4
 
    t = bp_.param[5][2] * bp_.top_layers
    b = bp_.param[5][1] - 2 * flange_width

    return round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2, 3)


def free_edge():
    global thickness, E, poisson
    k = 0.425

    t = bp_.param[5][2] * bp_.top_layers
    b = flange_width

    return round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2, 3)


def web():
    global thickness, E, poisson
    k = 6

    t = bp_.param[1][1]
    b = 1.27 + bp_.param[1][2] - bp_.centroidal_axis(bp_.param)

    return round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2, 3)


def shear():
    global thickness, E, poisson
    k = 5

    t = bp_.param[1][1]
    h = 1.27 + bp_.param[1][2]

    a = diaphrams()

    return round((k * np.pi**2 * E ) / (12*(1-poisson**2)) * ((t/h)**2 + (t/a)**2), 3)


def diaphrams():
    n_diaphrams = 10         
    a = 1270 / n_diaphrams

    return a


if __name__ == "__main__":
    print(web())