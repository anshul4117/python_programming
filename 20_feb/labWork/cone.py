import threedmodule as tm 

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Curved Surface Area:", tm.cone_csa(r, h))
print("Total Surface Area:", tm.cone_tsa(r, h))
print("Volume:", tm.cone_volume(r, h))