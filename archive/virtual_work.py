def virtual_work_table(force, area, length, dummy): 
    """
    Force - kN 
    Area - mm2 
    Length - m 
    Dummy - kN
    """
    force_N = force * 1000 
    stress = force_N / area 
    strain = stress / 200 
    deform = strain * length 
    virtual_work = dummy * deform 

    print(force, area, stress, strain, length, deform, dummy, virtual_work)

print("Force Area Stress Strain Length Deform Dummy Work")
# virtual_work_table(160, 1000, 2, 1.000) # AB
""" virtual_work_table(80.0, 1000, 2, 1.000) # AC
virtual_work_table(-113.1, 1000, 2.83, -1.414) # AD
virtual_work_table(80.0, 1000, 2, 1.000) # BD
virtual_work_table(160.0, 1000, 2, 3.000) # CD
virtual_work_table(-113.1, 1000, 2.83, -1.414) # BE
virtual_work_table(80.0, 1000, 2, 2.000) # DE """

virtual_work_table(160, 1000, 2, 1.000) # CD
virtual_work_table(80, 1000, 2, 1.000) # DE