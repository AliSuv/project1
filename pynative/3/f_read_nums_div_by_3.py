# read test.txt
with open("num.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()

    # iterate each lines from a test.txt
    for line in lines:
            # write current line
            num = int(line)
            if num%3 == 0:  
                print(line)
        # in each iteration reduce the count