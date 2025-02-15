#5. Understanding list methods like append(), insert(), remove(), pop().

fruits = ["Apple", "Banana", "Cherry"]

# 1. Using append() - Adding 'Mango' at the end
fruits.append("Mango")
print("After append:", fruits)  
# Output: ['Apple', 'Banana', 'Cherry', 'Mango']

# 2. Using insert() - Adding 'Orange' at index 1
fruits.insert(1, "Orange")
print("After insert:", fruits)  
# Output: ['Apple', 'Orange', 'Banana', 'Cherry', 'Mango']

# 3. Using remove() - Removing 'Banana'
fruits.remove("Banana")
print("After remove:", fruits)  
# Output: ['Apple', 'Orange', 'Cherry', 'Mango']

# 4. Using pop() - Removing the last element ('Mango')
removed_item = fruits.pop()
print("After pop:", fruits)  
# Output: ['Apple', 'Orange', 'Cherry']
print("Removed item:", removed_item)  
# Output: Mango
