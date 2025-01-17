# Define a string
my_string = "  Hello, Python World!  "

# 1. Strip whitespace from the beginning and end
stripped_string = my_string.strip()
print(f"Stripped string: '{stripped_string}'")

# 2. Convert the string to uppercase
uppercase_string = my_string.upper()
print(f"Uppercase string: '{uppercase_string}'")

# 3. Convert the string to lowercase
lowercase_string = my_string.lower()
print(f"Lowercase string: '{lowercase_string}'")

# 4. Replace 'Python' with 'Java'
replaced_string = my_string.replace("Python", "Java")
print(f"Replaced string: '{replaced_string}'")

# 5. Count occurrences of 'o'
count_o = my_string.count("o")
print(f"Count of 'o': {count_o}")

# 6. Find the position of 'Python'
find_python = my_string.find("Python")
print(f"Position of 'Python': {find_python}")

# 7. Check if the string starts with '  Hello'
starts_with_hello = my_string.startswith("  Hello")
print(f"Starts with '  Hello': {starts_with_hello}")

# 8. Check if the string ends with 'World!'
ends_with_world = my_string.endswith("World!")
print(f"Ends with 'World!': {ends_with_world}")

# 9. Split the string into words
split_string = my_string.split()
print(f"Split string into words: {split_string}")

# 10. Join a list of words into a single string
words = ['Python', 'is', 'awesome']
joined_string = " ".join(words)
print(f"Joined string: '{joined_string}'")
