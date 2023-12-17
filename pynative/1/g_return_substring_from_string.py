def count_substring(main_string, substring):
    count = main_string.count(substring)
    return count

given_string = "Ali is a good programmer. Ali loves football too."
substring_find = "Ali"

result = count_substring(given_string, substring_find)
print(f"Substring '{substring_find}' appears {result} times in the string.")