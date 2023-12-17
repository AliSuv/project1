word_input = input("Enter a word : ")
result = ""

for i in range(len(word_input)):
    if i % 2 == 0:
        result += word_input[i]

print("Characters at even index numbers are :", result)