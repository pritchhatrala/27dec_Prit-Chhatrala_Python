#24. Standard library modules: math, random.
print("--------math module--------")
import math

print("Square root of 25:", math.sqrt(25))  
print("Factorial of 5:", math.factorial(5))  
print("Power of 2^3:", math.pow(2, 3))  
print("Greatest Common Divisor (GCD) of 24 and 36:", math.gcd(24, 36))  
print("Floor of 3.7:", math.floor(3.7))  
print("Ceil of 3.2:", math.ceil(3.2))  
print("Value of Pi:", math.pi)  



print("\n--------Random module--------")
import random

print("Random integer (1-10):", random.randint(1, 10))
print("Random float (0-1):", random.random())  
print("Random float (1-5):", random.uniform(1, 5))  
print("Random choice from list:", random.choice(["Apple", "Banana", "Cherry"]))  
print("Random sample of 3 from list:", random.sample(range(1, 20), 3))  

# Shuffling a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)

