import math
number =  input("Enter a number between 1-10: ") 
number = int(number)
if (number <= 10 and number >= 0):
    for i in range(1,number + 1): 
        print("*" * i)
else:
    print("Your inputed number is larger than 10, please input smaller number.")