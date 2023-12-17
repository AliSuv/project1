def nums_divisible_by_5(numbers):
    for i in numbers:
        if i % 5 == 0:
            print(i)

num_list = [10, 25, 30, 17, 50, 63, 80, 5826, 45, 754]
nums_divisible_by_5(num_list)