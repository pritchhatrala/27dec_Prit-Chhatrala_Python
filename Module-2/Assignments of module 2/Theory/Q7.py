#7. Sorting and reversing a list using sort(), sorted(), and reverse()

numbers = [5, 2, 9, 1, 7]

print("Original List:", numbers)

# 1. Using sort() - Sorting the list in ascending order
numbers.sort()
print("After sort() (Ascending):", numbers) 

# 2. Using sort() with reverse=True - Sorting in descending order
numbers.sort(reverse=True)
print("After sort(reverse=True) (Descending):", numbers)

# 3. Using sorted() - Sorting in ascending order without modifying original list
numbers = [5, 2, 9, 1, 7]  
sorted_numbers = sorted(numbers)
print("Using sorted() (Ascending):", sorted_numbers)  # [1, 2, 5, 7, 9]
print("Original List remains:", numbers)  # [5, 2, 9, 1, 7]

# 4. Using sorted() with reverse=True - Sorting in descending order without modifying original list
desc_sorted = sorted(numbers, reverse=True)
print("Using sorted(reverse=True) (Descending):", desc_sorted)  # [9, 7, 5, 2, 1]

# 5. Using reverse() - Reversing the list (not sorting)
numbers.reverse()
print("After reverse():", numbers)  # [7, 1, 9, 2, 5] (Order flipped)
