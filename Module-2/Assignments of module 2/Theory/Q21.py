#21. Different types of functions: with/without parameters, with/without return values.

# 1. Function Without Parameters & Without Return Value
def greet():
    print("Hello! Welcome to Python.")

# 2. Function With Parameters & Without Return Value
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python.")

# 3. Function Without Parameters & With Return Value
def get_greeting():
    return "Hello! Welcome to Python."

# 4. Function With Parameters & With Return Value
def add(a, b):
    return a + b

# Function Calls
greet() 

greet_user("Prit")  

message = get_greeting()  
print(message)

result = add(5, 3) 
print("Sum:", result)
