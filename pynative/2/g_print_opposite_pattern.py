row = int(input("Enter how many rows you want to have: "))
start_num = int(input("Enter a number you want to start pattern: "))

for i in range(1, row + 1):
    for j in range(start_num - i, 0, -1):
        print(j+1, end=" ")
    print("")
