# Function to calculate the factorial of a number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Function to check if a number is a strong number
def is_strong_number(number):
    # Convert the number to a string to iterate through its digits
    num_str = str(number)
    
    # Calculate the sum of factorials of its digits
    factorial_sum = sum(factorial(int(digit)) for digit in num_str)
    
    # Check if the sum is equal to the original number
    return factorial_sum == number

# Example usage:
number = int(input("Enter a number: "))
if is_strong_number(number):
    print(f"{number} is a strong number.")
else:
    print(f"{number} is not a strong number.")
