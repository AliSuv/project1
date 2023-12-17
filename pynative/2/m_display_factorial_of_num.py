num = int(input("enter a number you want to factorialize: "))
factorial = 1

if num < 0:
    print("You cannot factorialize number below 0.")
elif num == 0:
    print("Factorial of number 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"Factorial of {num}: {factorial}")

#used a little help with: factorial = factorial * i