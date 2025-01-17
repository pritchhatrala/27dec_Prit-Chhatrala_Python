# Define a string
my_string = "Hello, World!"

# Demonstrate different types of string slicing

# Slice from index 0 to 4 (not including 5)
slice1 = my_string[0:5]
print(f"Slice from index 0 to 4: {slice1}")

# Slice from index 7 to the end of the string
slice2 = my_string[7:]
print(f"Slice from index 7 to the end: {slice2}")

# Slice from the beginning up to index 5 (not including 5)
slice3 = my_string[:5]
print(f"Slice from the beginning up to index 5: {slice3}")

# Slice with step of 2
slice4 = my_string[::2]
print(f"Slice with step of 2: {slice4}")

# Slice with negative indexing (from the last character backwards)
slice5 = my_string[-6:-1]
print(f"Slice with negative indexing: {slice5}")

# Reverse the string using slicing
reverse_string = my_string[::-1]
print(f"Reversed string: {reverse_string}")
