import math

num = float(input("Enter a number: "))

sqrt_result = math.sqrt(num)  
ceil_result = math.ceil(num)  
floor_result = math.floor(num)  
power_result = math.pow(num, 2)  
log_result = math.log(num) if num > 0 else "Undefined"  
sin_result = math.sin(math.radians(num)) 

print("\n Math Function Results:")
print(f"Square Root of {num}: {sqrt_result}")
print(f"Ceiling Value of {num}: {ceil_result}")
print(f"Floor Value of {num}: {floor_result}")
print(f"{num}^2 (Power of 2): {power_result}")
print(f"Logarithm (ln) of {num}: {log_result}")
print(f"Sine of {num} degrees: {sin_result}")
