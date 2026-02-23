import threedmodule as tm 

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Curved Surface Area:", tm.cone_csa(r, h))
print("Total Surface Area:", tm.cone_tsa(r, h))
print("Volume:", tm.cone_volume(r, h))

# output
# Enter radius: 5
# Enter height: 10
# Curved Surface Area: 175.0
# Total Surface Area: 196.25
# Volume: 261.6666666666667
