def add_students(n):
    """Function to add student data into a dictionary."""
    students = {}  # Dictionary to store student data
    for i in range(n):
        Id = input(f"Enter ID for student {i+1}: ")
        name = input(f"Enter Name for student {i+1}: ")
        students[Id] = name  # Store ID as key and Name as value
    return students

def display_students(students):
    """Function to display all students."""
    print("\nStudent List:")
    for Id, name in students.items():
        print(f"ID: {Id}, Name: {name}")

# Asking user for the number of students
n = int(input("How many students' info do you want to enter? "))

# Calling functions
student_data = add_students(n)
display_students(student_data)
