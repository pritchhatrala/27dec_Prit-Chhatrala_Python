try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    file = open("non_existent_file.txt", "w")

    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

except ValueError:
    print("Error: Invalid input! Please enter numeric values.")

except FileNotFoundError:
    print("Error: File not found!")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("Execution completed.")
