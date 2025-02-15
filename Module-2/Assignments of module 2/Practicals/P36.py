import random

random_int = random.randint(1, 100)
print("Random Integer (1-100):", random_int)

random_float = random.random()
print("Random Float (0-1):", random_float)

random_uniform = random.uniform(10, 50)
print("Random Float (10-50):", random_uniform)

numbers = [10, 20, 30, 40, 50]
random_choice = random.choice(numbers)
print("Random Choice from List:", random_choice)

random.shuffle(numbers)
print("Shuffled List:", numbers)
