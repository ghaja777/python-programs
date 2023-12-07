def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

try:
    user_input = int(input("Enter a non-negative integer: "))
    print(f"The factorial of {user_input} is {factorial(user_input)}")
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")
