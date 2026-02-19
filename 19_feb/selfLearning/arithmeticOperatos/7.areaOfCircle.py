# 7.Write a program to calculate the area of a circle without inbuilt function
radius = float(input("Enter the radius of the circle: "))
if(radius <= 0.0):
    print("radius should be greater then 0.0")
else:
    pi = 3.14
    area = pi * radius ** 2
    print("The area of the circle is:", area)

