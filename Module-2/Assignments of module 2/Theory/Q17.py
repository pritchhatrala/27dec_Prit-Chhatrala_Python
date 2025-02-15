#17. Iterating over a dictionary using loops

student = {
    "name": "Prit",
    "age": 21,
    "subject": "Python",
    "city": "Keshod"
}

print("Iterating over keys:")
for key in student:
    print("Key:", key)

print("\nUsing keys() method:")
for key in student.keys():
    print("Key:", key)

print("\nIterating over values:")
for value in student.values():
    print("Value:", value)

print("\nIterating over key-value pairs:")
for key, value in student.items():
    print(f"{key}: {value}")



