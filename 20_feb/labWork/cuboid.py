import threedmodule as tm 

l = float(input("Enter length: "))
w = float(input("Enter width: "))
h = float(input("Enter height: "))

print("Curved Surface Area:", tm.cuboid_csa(l, w, h))
print("Total Surface Area:", tm.cuboid_tsa(l, w, h))
print("Volume:", tm.cuboid_volume(l, w, h))