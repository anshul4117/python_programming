nested_list = [1, [2, 3], [4, [5, 6]], 7, [8, [9, [10]]]]

flattened_list = []

def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            flatten(item)
        else:
            flattened_list.append(item)

flatten(nested_list)

print("Nested list:", nested_list)
print("Flattened list:", flattened_list)