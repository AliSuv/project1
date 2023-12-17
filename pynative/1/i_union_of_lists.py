def create_list(list1, list2):
    new_list = list1 + list2
    return new_list

list_a = [1, 3, 5, 7, 9]
list_b = [2, 4, 6, 8, 10]

result_list = create_list(list_a, list_b)
print("New list:", result_list)