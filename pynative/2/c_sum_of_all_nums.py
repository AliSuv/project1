first = 0

num = int(input("Enter a number to calculate sum of all the nums in row: "))

for i in range(1, num + 1):
    first += i

print(f"Sum is: {first}")