try:
    file = open("example.txt", "r")
    content = file.read()
    print("File Content:\n", content)
    file.close()

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2  
    print(f"Result: {result}")

except FileNotFoundError:
    print("Error: The file was not found!")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

except ValueError:
    print("Error: Invalid input! Please enter numeric values.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("Execution completed.")
