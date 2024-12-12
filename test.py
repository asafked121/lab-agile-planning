# This is a simple Python script to calculate the factorial of a number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get input from the user
num = int(input("Enter a number: "))

# Calculate and print the factorial
print("The factorial of", num, "is", factorial(num))
