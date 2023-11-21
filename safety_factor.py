# Factor of Safety Calculations 
import bending_moment as bmd_
import applied_tension as at_
import applied_compression as ac_
import shear_stress as ss_
import thin_plate as tp_

# Tensile Stress [MPa]
tensile_stress = at_.calculate_tensile_stress(bmd_.calculate_bmd())
max_tensile_left = max(tensile_stress[0])
max_tensile_middle = max(tensile_stress[1])
max_tensile_right = max(tensile_stress[2])

MATBOARD_TENSILE_STRENGTH = 30 
fos_tensile = MATBOARD_TENSILE_STRENGTH / max(max_tensile_left, max_tensile_middle, max_tensile_right)

fos_tensile = round(fos_tensile, 3)

# Compressive Stress [MPa]
compressive_stress = ac_.calculate_compressive_stress(bmd_.calculate_bmd())
max_compressive_left = max(compressive_stress[0])
max_compressive_middle = max(compressive_stress[1])
max_compressive_right = max(compressive_stress[2])

MATBOARD_COMPRESSIVE_STRENGTH = 6
fos_compressive = (MATBOARD_COMPRESSIVE_STRENGTH / max(max_compressive_left, max_compressive_middle, max_compressive_right))
fos_compressive = round(fos_compressive, 3)

# Shear Stress [MPa]
axis_shear = ss_.axis_shear(False)
max_shear_left = axis_shear[0]
max_shear_middle = axis_shear[1]
max_shear_right = axis_shear[2]

MATBOARD_SHEAR_STRENGTH = 4 
fos_shear = MATBOARD_SHEAR_STRENGTH / max(max_shear_left, max_shear_middle, max_shear_right)
fos_shear = round(fos_shear, 3)

# Glue Shear Stress [MPa]
glue_shear = ss_.axis_shear(True)
max_glue_left = axis_shear[0]
max_glue_middle = axis_shear[1]
max_glue_right = axis_shear[2]

# Assume glue/contact cement is fully dried.
GLUE_SHEAR_STRENGTH = 2 
fos_glue = GLUE_SHEAR_STRENGTH / max(max_glue_left, max_glue_middle, max_glue_right)
fos_glue = round(fos_glue, 3)

# Thin Plate Buckling 
fos_center = MATBOARD_COMPRESSIVE_STRENGTH / tp_.center()
fos_free_edge = MATBOARD_COMPRESSIVE_STRENGTH / tp_.free_edge()
fos_web = MATBOARD_COMPRESSIVE_STRENGTH / tp_.web() 
fos_shear_buckling = MATBOARD_SHEAR_STRENGTH / tp_.shear()

fos_center = round(fos_center, 3)
fos_free_edge = round(fos_free_edge, 3)
fos_web = round(fos_web, 3)
fos_shear_buckling = round(fos_shear_buckling, 3)