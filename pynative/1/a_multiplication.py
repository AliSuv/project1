def multiply_or_sum():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 * num2
    if result <= 1000:
        return result
    else:
        return num1 + num2
final = multiply_or_sum()
print("Result:", final)