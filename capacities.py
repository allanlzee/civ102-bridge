"""
This code contains all functions outputting Shear Force Capacities and
Bending Moment Capacities. 

Note that for our bridge, which does not feature cross section changes, 
the capcities will all be straight, horizontal lines. 
"""

import matplotlib.pyplot as plt 
import numpy as np

import safety_factor as sf_
import shear_force as sfd_
import bending_moment as bmd_ 
import thin_plate as tp_
import applied_compression as ac_
import main

sfd = sfd_.calculate_sfd()
bmd = bmd_.calculate_bmd()
max_bmd = max(bmd_.bmd_envelope_all())

# Find the maximum shear force for the entire bridge. 
max_shear = max(sfd_.sfd_envelope_all())

# Find the maximum bending moment for the entire bridge. 
max_moment = max(bmd_.bmd_envelope_all())


def v_fail_shear(): 
    """Plot failure by centroidal axis shearing."""

    global sfd 

    shear_sf = sf_.fos_shear 

    capacity = [max_shear * shear_sf] * len(bmd[0])
    capacity_neg = [-max_shear * shear_sf] * len(bmd[0])

    plt.ylim(-capacity[0] * 1.25, capacity[0] * 1.25)
    plt.plot(np.array(capacity), label = "Matboard Shear Failure", color="red", linewidth=3.0) 
    plt.plot(np.array(capacity_neg), color="red", linewidth=3.0)
    plt.title("Shear Force Diagrams vs. Matboard Shear Failure")

    main.shear_force(True)

    
def v_fail_glue(): 
    """Plot failure by glue shear."""

    global sfd 

    glue_sf = sf_.fos_glue

    capacity = [max_shear * glue_sf] * len(bmd[0])
    capacity_neg = [-max_shear * glue_sf] * len(bmd[0])

    plt.ylim(-capacity[0] * 1.25, capacity[0] * 1.25)
    plt.plot(np.array(capacity), label = "Glue Shear Failure", color="red", linewidth=3.0) 
    plt.plot(np.array(capacity_neg), color="red", linewidth=3.0)
    plt.title("Shear Force Diagrams vs. Glue Shear Failure")

    main.shear_force(True)


def v_fail_buck(): 
    """Plot failure by shear buckling."""

    global sfd 

    shear_buck_sf = sf_.fos_shear_buckling

    capacity = [max_shear * shear_buck_sf] * len(bmd[0])
    capacity_neg = [-max_shear * shear_buck_sf] * len(bmd[0])

    plt.ylim(-capacity[0] * 1.5, capacity[0] * 1.5)
    plt.plot(np.array(capacity), label = "Shear Buckling Failure", color="red", linewidth=3.0) 
    plt.plot(np.array(capacity_neg), color="red", linewidth=3.0)

    plt.title("Shear Force Diagrams vs. Shear Buckling Failure")

    main.shear_force(True)


def m_fail_tens(): 
    """Plot failure by tensile stress."""

    global bmd 

    tens_sf = sf_.fos_tensile 

    capacity = [max_moment * tens_sf] * len(bmd[0])

    plt.ylim(max(capacity[0], max_moment) * 1.25, 0)
    plt.plot(np.array(capacity), label = "Matboard Tension Failure", color="red", linewidth=3.0)
    plt.title("Bending Moment Diagrams vs. Matboard Tension Failure")

    main.bending_moment(True)


def m_fail_comp(): 
    """Plot failure by compressive stress."""

    global bmd 

    comp_sf = sf_.fos_compressive 

    capacity = [max_moment * comp_sf] * len(bmd[0])

    plt.ylim(max(capacity[0], max_moment) * 1.25, 0)
    plt.plot(np.array(capacity), label = "Matboard Compression Failure", color="red", linewidth=3.0)
    plt.title("Bending Moment Diagrams vs. Matboard Compression Failure")

    main.bending_moment(True)


def m_fail_buck_center():
    """Plot failure by center buckling."""

    global bmd 

    capacity = [max_moment * sf_.fos_center] * len(bmd[0])
    
    plt.ylim(max(capacity[0], max_moment) * 1.25, 0)
    plt.plot(np.array(capacity), label = "Matboard Center Buckling Failure", color="red", linewidth=3.0)
    plt.title("Bending Moment Diagrams vs. Matboard Center Buckling Failure")

    main.bending_moment(True)


def m_fail_free_edge(): 
    """Plot failure by free edge buckling."""

    capacity = [max_moment * sf_.fos_free_edge] * len(bmd[0])

    plt.ylim(max(capacity[0], max_moment) * 1.05, 0)
    plt.plot(np.array(capacity), label = "Matboard Free Edge Buckling Failure", color="red", linewidth=3.0)
    plt.title("Bending Moment Diagrams vs. Matboard Free Edge Buckling Failure")

    main.bending_moment(True)


def m_fail_web():
    """Plot failure by web buckling."""

    capacity = [max_moment * sf_.fos_web] * len(bmd[0])

    plt.ylim(max(capacity[0], max_moment) * 1.05, 0)
    plt.plot(np.array(capacity), label = "Matboard Web Buckling Failure", color="red", linewidth=3.0)
    plt.title("Bending Moment Diagrams vs. Matboard Web Buckling Failure")

    main.bending_moment(True)


if __name__ == "__main__": 
    v_fail_shear()
    v_fail_glue()
    v_fail_buck()
    m_fail_tens()
    m_fail_comp()
    m_fail_buck_center()
    m_fail_free_edge()
    m_fail_web()