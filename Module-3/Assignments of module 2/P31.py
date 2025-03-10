import re

text = "Python is a powerful programming language."

pattern = r"Python"

match = re.match(pattern, text)

if match:
    print(f"Match found: '{match.group()}' at the beginning of the string.")
else:
    print("No match found at the beginning of the string.")
