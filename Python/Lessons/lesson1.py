# input1=input("Write me a word: ")
# input2=input("Write me a number: ")
# print(f"There are {input2} amount of {input1}.")

import random

def get_numbers():
    output = []
    for i in range (0,9):
        output.append(str(i)) # converts an number to string value.
    return output

def get_letters():
    output = []
    for i in range (97,122): # asci table range of alphabets.
        output.append(chr(i)) # coverts from numbers to asci table values (letters).
    return output

def code(lenght, number):
    num=get_numbers()
    abc=get_letters()
    if number == False:
        output = ""
        for i in range (lenght):
            rint = random.randint(0, len(abc)-1) # len = gets a lenght of a variable.
            output += abc[rint]
        return output
    
    output = ""
    for i in range (lenght):
        choosebox=random.randint(0, 1)
        if choosebox == 0:
            output += abc[random.randint(0, len(abc)-1)]
        else:
            output += num[random.randint(0, len(num)-1)]
    return output

password=code(6,True)
print(password)

     
    
