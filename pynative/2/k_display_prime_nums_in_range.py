start = int(input("Enter a start of a range: "))
end = int(input("Enter an end of a range: "))

for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

#used help with this: if (num % i) == 0
