my_dict = {
    "name": "Prit",
    "age": 21,
    "city": "Keshod",
    "profession": "Engineer",
    "hobby": "Playing games",
    "language": "Python"
}


print("Original Dictionary:", my_dict)

key = input("Enter the key to update: ")

if key in my_dict:
    new_value = input("Enter the new value: ")
    my_dict[key] = new_value  
    print("Updated Dictionary:", my_dict)
else:
    print("Key not found in the dictionary!")
