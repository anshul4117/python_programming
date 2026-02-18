# area of circle and perameter
radius = float(input("Enter the radius (in centimeter) :  "))
if(radius <= 0.0):
    print("radius should be greater then 0.0")
    exit()
else:
    pie = 3.14
    area = 0
    parameter = 0
    area = pie * radius * radius
    parameter = 2 * pie * radius
    print("area of circle",area)
    print("area of parameter",parameter)
