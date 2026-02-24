# Problem 57
# Problem Statement: Reverse a list without reverse method.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    element = int(input("Enter element : "))
    my_list.append(element)

print("Original list :", my_list)

reversed_list = []
for i in range(len(my_list) - 1, -1, -1):
    reversed_list.append(my_list[i])

print("Reversed list :", reversed_list)

# output
# Enter number of elements : 5
# Enter element : 10
# Enter element : 20
# Enter element : 30
# Enter element : 40
# Enter element : 50
# Original list : [10, 20, 30, 40, 50]
# Reversed list : [50, 40, 30, 20, 10]
