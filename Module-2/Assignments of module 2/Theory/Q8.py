#8. Basic list manipulations: addition, deletion, updating, and slicing.

fruits = ["Apple", "Banana", "Cherry"]
print("Original List:", fruits)

# 1. **Addition**
# Using append() to add an item at the end
fruits.append("Mango")
print("After append:", fruits)  # ['Apple', 'Banana', 'Cherry', 'Mango']

# Using insert() to add an item at a specific index
fruits.insert(1, "Orange")  
print("After insert at index 1:", fruits)  # ['Apple', 'Orange', 'Banana', 'Cherry', 'Mango']

# 2. Deletion
# Using remove() to delete an item by value
fruits.remove("Banana")
print("After remove 'Banana':", fruits)  # ['Apple', 'Orange', 'Cherry', 'Mango']

# Using pop() to delete an item by index (default last)
removed_item = fruits.pop(2)
print("After pop index 2:", fruits)  # ['Apple', 'Orange', 'Mango']

# 3. Updating
# Updating an element at a specific index
fruits[1] = "Pineapple"  
print("After updating index 1:", fruits)  # ['Apple', 'Pineapple', 'Mango']

# 4. Slicing
# Getting a sublist (first two elements)
sublist = fruits[:2]
print("Sliced List (first two elements):", sublist)  # ['Apple', 'Pineapple']

# Getting last two elements using negative indexing
sublist_negative = fruits[-2:]
print("Sliced List (last two elements):", sublist_negative)  # ['Pineapple', 'Mango']
