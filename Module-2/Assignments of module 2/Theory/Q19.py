#19. Counting occurrences of characters in a string using dictionaries.

text = "Prit Chhattrala"  
char_count = {}  

for char in text:
    if char in char_count:
        char_count[char] += 1  
    else:
        char_count[char] = 1  

print("Character Frequency:", char_count)
