def check_number(num):
    if num < 0:
        raise CustomError("Negative numbers are not allowed!")
    else:
        print(f"Valid number: {num}")

try:
    number = int(input("Enter a number: "))
    check_number(number)

except CustomError as e:
    print(f"Custom Exception Caught: {e}")

except ValueError:
    print("Error: Invalid input! Please enter a valid number.")
