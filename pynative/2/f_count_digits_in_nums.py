num = int(input("enter a number to count its digits: "))
count = 0

while num != 0:
    num = num // 10
    count = count + 1
print(f"There are {count} digits in your number.")