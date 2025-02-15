name = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    names = input(f"Enter element {i+1}: ")
    name.append(names) 
    
print("Final List:", name)
