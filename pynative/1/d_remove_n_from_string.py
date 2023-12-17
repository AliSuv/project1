def remove_characters(input_word, n):
    if n < len(input_word):
        return input_word[n:]
    else:
        return "n must be less than the length of the word."

print(remove_characters("university", 4))
print(remove_characters("mobile", 2))


x = "suvchanov"
print(x[1:7])