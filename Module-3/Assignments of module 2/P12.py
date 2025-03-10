try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = num1 / num2
    
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

except ValueError:
    print("Error: Invalid input! Please enter numeric values.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
