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

def compressive_stress ():
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

    print("Maximum Compressive Stress [MPa]: " + str(max(compressive_stresses[1])))

    plt.legend()
    plt.xlabel("Bridge Distance (mm)")
    plt.ylabel("Compressive Stress (MPa)")
    plt.title("Compressive Stress Diagrams for Left, Middle, and Right Train Placements")
    plt.show()

def shear_stress (): 
    print("Centroidal Axis [MPa]: " + str(ss_.axis_shear(False)))
    print("Glue Point [MPa]: " + str(ss_.axis_shear(True))) 

def thin_plate():
    print("Bottom Center (MPa): " + str(tp_.center()))
    print("Overhangs (MPa): " + str(tp_.free_edge()))
    print("Web (MPa): " + str(tp_.web()))
    print("Top Center (MPa): " + str(tp_.shear()))

def shear_force ():
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
    plt.show()

def tensile_stress():
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

    print("Maximum Tensile Stress [MPa]: " + str(max(tensile_stresses[1])))

    plt.legend()
    plt.xlabel("Bridge Distance (mm)")
    plt.ylabel("Tensile Stress (MPa)")
    plt.title("Tensile Stress Diagrams for Left, Middle, and Right Train Placements")
    plt.show()

def bending_moment():
    bending_moment_diagrams = bmd_.calculate_bmd() 
    
    # Note that all compressions will be given as positive.
    # Refer to the bending moment diagrams to see which signs the moment has.
    print("Moment Envelope (Nmm)")
    print("-" * len("Moment Envelope (Nmm)"))
    print(bmd_.bmd_envelope())
    
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
    plt.ylim(100000, 0)
    plt.xlabel("Bridge Distance (mm)")
    plt.ylabel("Moment (Nmm)")
    plt.title("Bending Moment Diagrams for Left, Middle, and Right Train Placements")
    plt.show()

def FOS ():
    print("Tensile FOS.: " + str(fos_.fos_tensile))
    print("Compressive FOS.: " + str(fos_.fos_compressive))
    print("Matboard Shear FOS.: " + str(fos_.fos_shear))
    print("Glue Shear FOS: " + str(fos_.fos_glue))

def bridge_parameters():
    print("Centroidal Axis (mm): " + str(bp_.centroidal_axis(bp_.param)))
    print("Second Moment of Area (mm4): " + str(bp_.second_moment_of_area(bp_.param)))
    print("First Moment of Area (Centroidal Axis to Bottom) [mm3]: " + str(bp_.calculate_first_moment_of_area(bp_.param, bp_.centroidal_axis(bp_.param), False)))
    print("First Moment of Area (Glue to Centroidal Axis) [mm3]: " + str(bp_.calculate_first_moment_of_area(bp_.param, bp_.glue_location, True)))

if __name__ == "__main__":
    compressive_stress()
    shear_stress()
    thin_plate()
    shear_force()
    tensile_stress()
    bending_moment()
    FOS()
    bridge_parameters()

