num = int(input("Enter a number: "))
start = int(input("Enter a number you want to work with: "))
sequence = 0

for i in range(1, num + 1):
    print(start, end=" + ")
    sequence += start
    start = (start * 10)
print(f"Sum is: {sequence}")

#not finished