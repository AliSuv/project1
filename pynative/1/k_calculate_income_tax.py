def calculate_tax(income):
    if income <= 10000:
        tax = 0
    elif income <= 20000:
        tax = (income - 10000) * 0.10
    else:
        tax = 10000 * 0.10 + (income - 20000) * 0.20
    return tax

income = int(input("Enter your income: "))
result_tax = calculate_tax(income)
print(f"The income tax for ${income} is: ${result_tax}")
x = income - result_tax
print(f"Your salary: ${x}")