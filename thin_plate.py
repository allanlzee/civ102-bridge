import bridge_parameters as bp_
import main as m_
import numpy as np

# matboard params
thickness = 1.27          # mm
E = 4000                  # MPa
poisson = 0.2             # unitles
flange_width = 10         # mm

def top_center():
    global thickness, E, poisson
    k = 4
 
    t = bp_.param[5][2]
    b = bp_.param[5][1] - 2 * flange_width

    print(t, b)

    return (k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2
    
def free_edge():
    global thickness, E, poisson
    k = 0.425

    t = bp_.param[5][2]
    b = bp_.param[5][1]

    print(t, b)

    return (k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2

def web():
    global thickness, E, poisson
    k = 6

    t = bp_.param[1][1]
    b = bp_.param[1][2]

    print(t, b)

    return (k * np.pi**2 * E ) / (12*(1-poisson**2)) * (t/b)**2

def shear():
    global thickness, E, poisson
    k = 5

    t = bp_.param[5][2]
    h = bp_.param[5][1]
    a = 50                      # to be optimized

    print(t, h, a)

    return (k * np.pi**2 * E ) / (12*(1-poisson**2)) * ((t/h)**2 + (t/a)**2)

if __name__ == "__main__":
    """print("Top Center (MPa): " + str(top_center()))
    print("Free Edge (MPa): " + str(free_edge()))
    print("Web (MPa): " + str(web()))
    print("Shear (MPa): " + str(shear()))

    m_.thin_plate()"""
    pass
