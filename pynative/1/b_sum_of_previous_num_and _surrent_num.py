prev_number = 0
for i in range(10):
    curr_number = i
    sum_curr_previous = curr_number + prev_number
    print(f"Current number is : {curr_number}, Previous number is : {prev_number}, and the Sum is : {sum_curr_previous}")
    prev_number = curr_number