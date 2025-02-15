#16. Dictionary methods like keys(), values(), and items().

# Creating a dictionary
student = {
    "name": "Prit",
    "age": 21,
    "subject": "Python",
    "city": "Keshod"
}

print("Keys:", student.keys())

print("Values:", student.values())

print("Items:", student.items())

key_list = list(student.keys())
value_list = list(student.values())
items_list = list(student.items())

print("\nList of Keys:", key_list)
print("List of Values:", value_list)
print("List of Items:", items_list)

print("\nIterating over keys:")
for key in student.keys():
    print("Key:", key)

print("\nIterating over values:")
for value in student.values():
    print("Value:", value)

print("\nIterating over key-value pairs:")
for key, value in student.items():
    print(f"{key}: {value}")
