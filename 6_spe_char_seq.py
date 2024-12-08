import re


# Example 1: \d - Matches any digit
text1 = "abc 123"
pattern1 = r'\d'
matches1 = re.findall(pattern1, text1)

# Example 2: \w - Matches any word character (letters, digits, or underscore)
text2 = "abc_123"
pattern2 = r'\w'
matches2 = re.findall(pattern2, text2)

# Example 3: \s - Matches any whitespace character (spaces, tabs, newlines)
text3 = "hello world\n"
pattern3 = r'\s'
matches3 = re.findall(pattern3, text3)

# Example 4: ^ - Matches the start of the string
text4 = "hello world"
pattern4 = r'^hello'
matches4 = re.findall(pattern4, text4)

# Example 5: $ - Matches the end of the string
text5 = "hello world"
pattern5 = r'world$'
matches5 = re.findall(pattern5, text5)

# Example 6: [] - Matches any one of the characters in the brackets
text6 = "hello world"
pattern6 = r'[aeiou]'  # Matches vowels
matches6 = re.findall(pattern6, text6)

# Print all results
print("Matches for \\d (digits):", matches1)
print("Matches for \\w (word characters):", matches2)
print("Matches for \\s (whitespace):", matches3)
print("Matches for ^ (start of string):", matches4)
print("Matches for $ (end of string):", matches5)
print("Matches for [aeiou] (vowels):", matches6)
