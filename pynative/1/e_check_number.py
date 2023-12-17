def check_first_last_equal(input_list):
    if len(input_list) >= 1 and input_list[1] == input_list[-2]:
        return True
    else:
        return False
print(check_first_last_equal([1, 2, 3, 2, 1])) 
print(check_first_last_equal([5, 6, 7, 8, 9]))
print(check_first_last_equal([3, 5]))
print(check_first_last_equal([78, 78]))