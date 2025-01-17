List1 = ['apple', 'banana', 'mango']

search_string = input("Enter the string to find: ")

found = False
for fruit in List1:
    if fruit == search_string:
        print(f"'{search_string}' is found in the list.")
        found = True
        break

if not found:
    print(f"'{search_string}' is not found in the list.")
