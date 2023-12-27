"""This code is the main file that runs all calculations to determine 
factor of safety for all possible modes of failure."""

import shear_stress as ss_
import applied_compression as ac_
import thin_plate as tp_
import shear_force as sfd_
import bending_moment as bmd_
import applied_tension as at_
import bridge_parameters as bp_
import safety_factor as fos_

import matplotlib.pyplot as plt
import numpy as np

def compressive_stress():
    """Calculate maximum compressive stress."""

    print("\nCOMPRESSIVE STRESS")
    compressive_stresses = ac_.calculate_compressive_stress()

    print("Maximum Compressive Stress [MPa]: " + str(compressive_stresses))


def shear_stress(): 
    """Calculate maximum shear stress at the centroidal axis and glue point."""

    print("\nSHEAR STRESS")
    print("Centroidal Axis [MPa]: " + str(ss_.axis_shear(False)))
    print("Glue Point [MPa]: " + str(ss_.axis_shear(True))) 


def thin_plate():
    """Calculate thin plate buckling for all four cases."""

    print("\nTHIN PLATE")
    print("Four restrained (MPa): " + str(tp_.center()))
    print("Free edge (MPa): " + str(tp_.free_edge()))
    print("Web (MPa): " + str(tp_.web()))
    print("Shear (MPa): " + str(tp_.shear()))


def shear_force (plot):
    """Plot shear force diagrams for all locations along the bridge."""

    print("\nSHEAR FORCE")

    all_shear_force_diagrams = sfd_.calculate_sfd()
    sfd_envelope = sfd_.sfd_envelope_all()

    for sfd in all_shear_force_diagrams: 
        sfd.insert(0, 0)
        plt.plot(np.array(sfd))

    # Plot shear force envelope. 
    plt.plot(np.array(sfd_envelope), label="Shear Force Envelope", linewidth=3.0)
    plt.plot(np.array([0] * (sfd_.n + 1)), color="black")
    plt.legend()
    plt.xlabel("Bridge Distance (mm)")
    plt.ylabel("Shear Force (N)")

    if plot:
        plt.show()


def tensile_stress():
    """Calculate maximum tensile stress."""

    print("\nTENSILE STRESS")
    tensile_stress = at_.calculate_tensile_stress()

    print("Maximum Tensile Stress [MPa]: " + str(tensile_stress))


def bending_moment(plot):
    """Plot bending moment diagrams for all locations on the bridge."""

    print("\nBENDING MOMENT")
    bending_moment_diagrams = bmd_.calculate_bmd_right_middle_left() 
    all_bending_moment_diagrams = bmd_.calculate_bmd()
    
    # Note that all compressions will be given as positive.
    # Refer to the bending moment diagrams to see which signs the moment has.
    bmd_envelope = bmd_.bmd_envelope_all() 

    for bmd in all_bending_moment_diagrams: 
        plt.plot(np.array(bmd))
    
    for bmd in range(len(bending_moment_diagrams)): 
        leg_label = None
        match bmd: 
            case 0: 
                leg_label = "Left BMD"
            case 1: 
                leg_label = "Middle BMD"
            case 2: 
                leg_label = "Right BMD"

        plt.plot(np.array(bending_moment_diagrams[bmd]), label = leg_label, linewidth=3.0)
        
    # Plot bending moment envelope. 
    plt.plot(np.array(bmd_envelope), label = "Bending Moment Envelope", linewidth=3.0)

    plt.plot(np.array([0] * (sfd_.n + 1)), color="black")

    plt.legend()
    plt.xlabel("Bridge Distance (mm)")
    plt.ylabel("Moment (Nmm)")

    if plot:
        plt.show()


def FOS():
    """Print all factors of safety for each mode of potential failure."""

    print("\nSAFETY FACTOR")
    print("Tensile FOS: " + str(fos_.fos_tensile))
    print("Compressive FOS: " + str(fos_.fos_compressive))
    print("Matboard Shear FOS.: " + str(fos_.fos_shear))
    print("Glue Shear FOS: " + str(fos_.fos_glue))
    print("Center Thin Plate Buckling: " + str(fos_.fos_center))
    print("Free Edge Thin Plate Buckling: " + str(fos_.fos_free_edge))
    print("Web Thin Plate Buckling: " + str(fos_.fos_web))
    print("Shear Thin Plate Buckling: " + str(fos_.fos_shear_buckling)) 


def bridge_parameters():
    """Calculate the bridge properties. 
    This includes leftover Matboard, centroidal axis, first moment of area, and second moment
    of area."""

    print("\nBRIDGE PARAMETERS")
    print("Leftover Matboard (mm^2): " + str(bp_.leftover(bp_.param)))

    try:
        print("Leftover Matboard (mm): " + str(round(max(0, bp_.leftover(bp_.param)) ** 0.5, 3)))
    except ValueError: 
        print("Not enough matboard.")
        
    print("Centroidal Axis (mm): " + str(bp_.centroidal_axis(bp_.param)))
    print("I (mm4): " + str(bp_.second_moment_of_area(bp_.param)))
    print("Q (Centroidal Axis to Bottom) [mm3]: " +  
        str(bp_.calculate_first_moment_of_area(bp_.param, bp_.centroidal_axis(bp_.param), False)))
    print("Q (Glue to Centroidal Axis) [mm3]: " + 
        str(bp_.calculate_first_moment_of_area(bp_.param, bp_.glue_location, True)))


def sorted_FOS():
    """Print factors of safety for each mode of potential failure in descending order."""

    lines_with_values = [
        ("Applied Tensile: ", fos_.fos_tensile),
        ("Applied Compressive: ", fos_.fos_compressive),
        ("Web Thin Plate: ", fos_.fos_web),
        ("Center Thin Plate: ", fos_.fos_center),
        ("Free Edge Thin Plate: ", fos_.fos_free_edge),
        ("Matboard Shear (Centroidal Axis): ", fos_.fos_shear),
        ("Shear Thin Plate: ", fos_.fos_shear_buckling),
        ("Glue Shear: ", fos_.fos_glue)
    ]

    sorted_lines = sorted(lines_with_values, key=lambda x: x[1], reverse=True)

    print("\nSORTED FOS")
    for line, value in sorted_lines:
        print(line + str(value))


if __name__ == "__main__":
    print("\n")
    print("Design Iteration")
    print("----------------")
    shear_force(True)
    bending_moment(True)

    tensile_stress()
    compressive_stress()
    
    shear_stress()
    thin_plate()

    bridge_parameters()
    sorted_FOS()
    print()
