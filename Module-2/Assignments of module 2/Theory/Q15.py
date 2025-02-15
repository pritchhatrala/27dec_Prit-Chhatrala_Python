#15. Accessing, adding, updating, and deleting dictionary elements.

# Creating a dictionary
student = {
    "name": "Prit",
    "age": 21,
    "Subject":"Python"
}

# 1. Accessing elements
print("Name:", student["name"])  
print("Age:", student.get("age"))  
print("City:", student.get("city", "Not Found"))  

# 2. Adding elements
student["city"] = "Keshod"
student["course"] = "Full-Stack"
print("\nAfter Adding Elements:", student)

# 3. Updating elements
student["age"] = 20
student["subject"] = "JAVA"
student.update({"city": "junagadh", "course": "Python Backend"})
print("\nAfter Updating Elements:", student)

# 4. Deleting elements
del student["city"]  
removed_subject = student.pop("subject")  
last_item = student.popitem()  

print("\nAfter Deleting Elements:", student)
print("Removed subject:", removed_subject)
print("Last removed item:", last_item)

# 5. Clearing dictionary
student.clear()
print("\nAfter Clearing Dictionary:", student) 
