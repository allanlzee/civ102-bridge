# Factor of Safety Calculations 
import bending_moment as bmd_
import applied_tension as at_
import applied_compression as ac_
import shear_stress as ss_
import thin_plate as tp_
import bridge_parameters as bp_

# Tensile Stress [MPa]
tensile_stress = at_.calculate_tensile_stress()
MATBOARD_TENSILE_STRENGTH = 30 
fos_tensile = MATBOARD_TENSILE_STRENGTH / tensile_stress

fos_tensile = round(fos_tensile, 3)

# Compressive Stress [MPa]
compressive_stress = ac_.calculate_compressive_stress()

MATBOARD_COMPRESSIVE_STRENGTH = 6
fos_compressive = MATBOARD_COMPRESSIVE_STRENGTH / compressive_stress
fos_compressive = round(fos_compressive, 3)

# Shear Stress [MPa]
axis_shear = ss_.axis_shear(False)

MATBOARD_SHEAR_STRENGTH = 4 
fos_shear = MATBOARD_SHEAR_STRENGTH / axis_shear
fos_shear = round(fos_shear, 3)

# Glue Shear Stress [MPa]
glue_shear = ss_.axis_shear(True)

# Assume glue/contact cement is fully dried.
GLUE_SHEAR_STRENGTH = 2 
fos_glue = GLUE_SHEAR_STRENGTH / glue_shear
fos_glue = round(fos_glue, 3)

# Thin Plate Buckling 
MAX_COMPRESSION = ac_.calculate_compressive_stress()
fos_center = tp_.center() / MAX_COMPRESSION
fos_free_edge = tp_.free_edge() / MAX_COMPRESSION

web_compression = max(bmd_.bmd_envelope_all()) * (bp_.param[4][0] + bp_.param[4][2] / 2 - bp_.centroidal_axis(bp_.param)) / bp_.second_moment_of_area(bp_.param)
fos_web = tp_.web() / web_compression

fos_shear_buckling = tp_.shear() / ss_.axis_shear(False)

fos_center = round(fos_center, 3)
fos_free_edge = round(fos_free_edge, 3)
fos_web = round(fos_web, 3)
fos_shear_buckling = round(fos_shear_buckling, 3)