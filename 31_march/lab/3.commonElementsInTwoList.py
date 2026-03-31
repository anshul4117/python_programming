list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

common_elements = []


for num in list1:
    if num in list2:
        if num not in common_elements:
            common_elements.append(num)

print("List 1:", list1)
print("List 2:", list2)
print("Common elements:", common_elements)