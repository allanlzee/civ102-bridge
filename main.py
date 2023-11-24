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

def compressive_stress (plot):
    print("\nCOMPRESSIVE STRESS")
    compressive_stresses = ac_.calculate_compressive_stress(bmd_.calculate_bmd())

    for stress in range(len(compressive_stresses)):
        leg_label = None 

        match stress: 
            case 0: 
                leg_label = "Left Stress"
            case 1: 
                leg_label = "Middle Stress"
            case 2: 
                leg_label = "Right Stress"

        plt.plot(np.array(compressive_stresses[stress]), label = leg_label)

    print("Maximum Compressive Stress [MPa]: " + str(max(compressive_stresses[0])))

    plt.legend()
    plt.xlabel("Bridge Distance (mm)")
    plt.ylabel("Compressive Stress (MPa)")
    plt.title("Compressive Stress Diagrams for Left, Middle, and Right Train Placements")
    
    if plot:
        plt.show()

def shear_stress (): 
    print("\nSHEAR STRESS")
    print("Centroidal Axis [MPa]: " + str(ss_.axis_shear(False)))
    print("Glue Point [MPa]: " + str(ss_.axis_shear(True))) 

def thin_plate():
    print("\nTHIN PLATE")
    print("Four restrianed (MPa): " + str(tp_.center()))
    print("Free edge (MPa): " + str(tp_.free_edge()))
    print("Web (MPa): " + str(tp_.web()))
    print("Shear (MPa): " + str(tp_.shear()))

def shear_force (plot):
    print("\nSHEAR FORCE")
    print("Shear Envolope (N):", sfd_.sfd_envelope())

    shear_force_diagrams = sfd_.calculate_sfd()

    for sfd in range(len(shear_force_diagrams)): 
        leg_label = None
        match sfd: 
            case 0: 
                leg_label = "Left SFD"
            case 1: 
                leg_label = "Middle SFD"
            case 2: 
                leg_label = "Right SFD"
            
        plt.plot(np.array(shear_force_diagrams[sfd]), label = leg_label)
    
    plt.plot(np.array([0] * (sfd_.n + 1)), color="black")
        
    plt.legend()
    plt.ylim(-300, 300)
    plt.xlabel("Bridge Distance (mm)")
    plt.ylabel("Shear Force (N)")
    plt.title("Shear Force Diagrams for Left, Middle, and Right Train Placements")
    if plot:
        plt.show()

def tensile_stress(plot):
    print("\nTENSILE STRESS")
    tensile_stresses = at_.calculate_tensile_stress(bmd_.calculate_bmd())

    for stress in range(len(tensile_stresses)):
        leg_label = None 

        match stress: 
            case 0: 
                leg_label = "Left Stress"
            case 1: 
                leg_label = "Middle Stress"
            case 2: 
                leg_label = "Right Stress"

        plt.plot(np.array(tensile_stresses[stress]), label = leg_label)

    print("Maximum Tensile Stress [MPa]: " + str(max(tensile_stresses[0])))

    plt.legend()
    plt.xlabel("Bridge Distance (mm)")
    plt.ylabel("Tensile Stress (MPa)")
    plt.title("Tensile Stress Diagrams for Left, Middle, and Right Train Placements")
    if plot:
        plt.show()

def bending_moment(plot):
    print("\nBENDING MOMENT")
    bending_moment_diagrams = bmd_.calculate_bmd() 
    
    # Note that all compressions will be given as positive.
    # Refer to the bending moment diagrams to see which signs the moment has.
    print("Moment Envelope (Nmm):", bmd_.bmd_envelope())
    
    for bmd in range(len(bending_moment_diagrams)): 
        leg_label = None
        match bmd: 
            case 0: 
                leg_label = "Left BMD"
            case 1: 
                leg_label = "Middle BMD"
            case 2: 
                leg_label = "Right BMD"

        plt.plot(np.array(bending_moment_diagrams[bmd]), label = leg_label)
        
    plt.plot(np.array([0] * (sfd_.n + 1)), color="black")

    plt.legend()
    plt.xlabel("Bridge Distance (mm)")
    plt.ylabel("Moment (Nmm)")
    plt.title("Bending Moment Diagrams for Left, Middle, and Right Train Placements")
    if plot:
        plt.show()

def FOS ():
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
    print("\nBRIDGE PARAMETERS")
    print("Leftover Matboard (mm^2): " + str(bp_.leftover(bp_.param)))
    print("Leftover Matboard (mm): " + str(round(bp_.leftover(bp_.param) ** 0.5, 3)))
    print("Centroidal Axis (mm): " + str(bp_.centroidal_axis(bp_.param)))
    print("I (mm4): " + str(bp_.second_moment_of_area(bp_.param)))
    print("Q (Centroidal Axis to Bottom) [mm3]: " + str(bp_.calculate_first_moment_of_area(bp_.param, bp_.centroidal_axis(bp_.param), False)))
    print("Q (Glue to Centroidal Axis) [mm3]: " + str(bp_.calculate_first_moment_of_area(bp_.param, bp_.glue_location, True)))

def sorted_FOS():
    lines_with_values = [
        ("Applied Tensile: ", fos_.fos_tensile),
        ("Applied Compressive: ", fos_.fos_compressive),
        ("Web Thin Plate: ", fos_.fos_web),
        ("Center Thin Plate: ", fos_.fos_center),
        ("Free Edge Thin Plate: ", fos_.fos_free_edge),
        ("Matboard Shear: ", fos_.fos_shear),
        ("Shear Thin Plate: ", fos_.fos_shear_buckling),
        ("Glue Shear: ", fos_.fos_glue)
    ]

    sorted_lines = sorted(lines_with_values, key=lambda x: x[1], reverse=True)

    print("\nSORTED FOS")
    for line, value in sorted_lines:
        print(line + str(value))

if __name__ == "__main__":
    print("\n" * 10)

    shear_force(False)
    # bending_moment(False)
    # compressive_stress(False)
    # tensile_stress(False)
    shear_stress()
    thin_plate()

    bridge_parameters()
    sorted_FOS()
