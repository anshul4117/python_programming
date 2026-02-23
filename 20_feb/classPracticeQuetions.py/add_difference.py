# import mathUtils as cal

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# sum_res = cal.add_numbers(num1,num2)
# sub_res = cal.subtract_numbers(num1,num2)
# print("Sum:",sum_res)
# print("Difference:",sub_res)


from mathUtils import *

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_res = add_numbers(num1,num2)
sub_res = subtract_numbers(num1,num2)
print("Sum:",sum_res)
print("Difference:",sub_res)