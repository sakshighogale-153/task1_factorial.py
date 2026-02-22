import math

# Get the input
user_input = input("Enter a number: ")
num = float(user_input)

# Perform calculations
res_sqrt = math.sqrt(num)
res_log = math.log(num)
res_sin = math.sin(num)

# Display exactly as shown in the example
print(f"Square root: {res_sqrt}")
print(f"Logarithm: {res_log}")
print(f"Sine: {res_sin}")
