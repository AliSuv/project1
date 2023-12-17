num = int(input("enter a number: "))
reverse_num = 0

while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num //= 10
print(f"Reversed num: {reverse_num}.")