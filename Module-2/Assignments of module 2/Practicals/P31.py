def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    while True:
        print("\n Simple Calculator ")
        print("1 Addition")
        print("2 Subtraction")
        print("3 Multiplication")
        print("4 Division")
        print("5 Exit")

        choice = input("Select an operation (1-5): ")

        if choice == "5":
            print(" Exiting Calculator. Thank you! ")
            break

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    print("Result:", add(num1, num2))
                elif choice == "2":
                    print("Result:", subtract(num1, num2))
                elif choice == "3":
                    print("Result:", multiply(num1, num2))
                elif choice == "4":
                    print("Result:", divide(num1, num2))

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        else:
            print("Invalid choice! Please select between 1-5.")

# Run the calculator
calculator()
