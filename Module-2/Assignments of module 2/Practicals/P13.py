my_tuple = (10, 3.14, "Hello world!", True, [1, 2, 3], {"name": "prit"}, (5, 6))

print("Tuple with multiple data types:", my_tuple)

print("\nElement types in the tuple:")
for item in my_tuple:
    print(f"{item} - {type(item)}")
