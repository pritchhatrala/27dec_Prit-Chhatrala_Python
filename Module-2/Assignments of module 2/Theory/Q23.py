#23.Introduction to Python modules and importing modules.

import math
print("Square root of 16:", math.sqrt(16))

from math import factorial
print("Factorial of 5:", factorial(5))

import random as rnd
print("Random number between 1 and 10:", rnd.randint(1, 10))

from datetime import *
today = date.today()
print("Today's date:", today)

