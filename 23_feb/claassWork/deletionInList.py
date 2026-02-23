# WAP in python to create list of 20 numbers and ask the user to input any number and
# delete this number from the list from its all the occurences accept first occurence

# numbersList = [
#     12,
#     12,
#     12,
#     12,
#     12,
#     12,
#     12,
#     112,
#     12,
#     12,
#     12,
#     11,
#     12,
#     121,
#     12,
#     221,
#     12,
#     12,
#     12,
# ]
# print("The list of numbers is: ", numbersList)
# numToDelete = int(input("Enter number to delete from the list : "))
# if(numToDelete != 0):
#     frequency  = 0
#     frequency = numbersList.count(numToDelete)
#     if(frequency == 0):
#         print("The number is not present in the list")
#     elif(frequency == 1):
#         print("The number is present only once in the list, so it cannot be deleted", numbersList)
#     else:
#         numbersList.reverse()
#         for i in range(1,frequency):
#             numbersList.remove(numToDelete)
#         numbersList.reverse()
#         print("The list after deletion of the number is: ", numbersList)
# else:    
#     print("Please enter a valid number to delete from the list")

x = {}
x.add(1)
print(type(x))