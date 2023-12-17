def exponent():
    exp = int(input("Enter an exponent: "))
    base = int(input("Enter a base: "))
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)
7
exponent()