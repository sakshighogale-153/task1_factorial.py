# Task 1: Calculate Factorial Using a Function

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Taking input from user
num = int(input("Enter a number: "))

# Calling the function
fact = factorial(num)

# Printing the result
print("Factorial of", num, "is:", fact)
