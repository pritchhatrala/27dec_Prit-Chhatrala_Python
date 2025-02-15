#11. Basic operations with tuples: concatenation, repetition, membership.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenating two tuples
new_tuple = tuple1 + tuple2  
print(new_tuple)  


# Repeating the tuple 3 times
repeat_tuple = tuple1 * 3  
print(repeat_tuple) 


# Checking membership
print(1 in tuple1)   # Output: True
print(5 in tuple2)   # Output: False
print(10 in tuple1)  # Output: False
