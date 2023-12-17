def extract_digits(number):
    num_str = str(number)
    reversed_digits = num_str[::-1]
    result = " ".join(reversed_digits)
    return result

given_int = 7536
output = extract_digits(given_int)
print("Output:", output)