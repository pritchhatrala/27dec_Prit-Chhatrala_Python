#18. Merging two lists into a dictionary using loops or zip().

keys = ["name", "age", "city"]
values = ["Prit", 21, "Keshod"]

merged_dict = {}

for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

print("Merged Dictionary:", merged_dict)
