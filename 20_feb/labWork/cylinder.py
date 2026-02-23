import threedmodule as tm 

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Curved Surface Area:", tm.cylinder_csa(r, h))
print("Total Surface Area:", tm.cylinder_tsa(r, h))
print("Volume:", tm.cylinder_volume(r, h))

# output
# Enter radius: 5
# Enter height: 10
# Curved Surface Area: 314.0
# Total Surface Area: 471.0
# Volume: 785.0
