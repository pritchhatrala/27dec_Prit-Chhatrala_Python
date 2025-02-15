operation = lambda a, b: (a + b, a * b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result, Mul_result = operation(num1, num2)

print("Sum:", sum_result)
print("Mul.:", Mul_result)
