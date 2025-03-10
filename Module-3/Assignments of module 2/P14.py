def calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2 
        else:
            raise ValueError("Invalid operator!")  
        
        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")

    except ValueError:
        print("Error: Invalid input! Please enter numeric values and a valid operator.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

calculator()
