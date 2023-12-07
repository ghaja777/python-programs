# Function to calculate the factorial of a number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Input from the user
num = int(input("Enter a non-negative integer: "))

# Check if the input is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorials of numbers from 1 to", num)
    for i in range(1, num + 1):
        result = factorial(i)
        print(f"{i}! = {result}")

