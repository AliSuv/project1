row = int(input("Enter how many rows you want to have: "))

for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
        #x = 10 - i
        #print(f"{j: >x}", end="") 