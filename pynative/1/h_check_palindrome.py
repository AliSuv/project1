def palindrome(num):
    num_str = str(num)
    reverse_str = num_str[::-1]
    return num_str == reverse_str

num1 = 545
num2 = 12321
num3 = 12345
num4 = 576423755

print(f"Is {num1} a palindrome? {palindrome(num1)}.")
print(f"Is {num2} a palindrome? {palindrome(num2)}.")
print(f"Is {num3} a palindrome? {palindrome(num3)}.")
print(f"Is {num4} a palindrome? {palindrome(num4)}.")