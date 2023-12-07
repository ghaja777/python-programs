# Function to check if a number is even or odd
def is_even_or_odd(number):
    last_digit = number % 10  # Get the last digit of the number
    if last_digit in (0, 2, 4, 6, 8):
        return "Even"
    else:
        return "Odd"

# Ask the user for input
try:
    num = int(input("Enter a number: "))
    
    # Check if the number is even or odd
    result = is_even_or_odd(num)
    print(f"{num} is {result}")
    
except ValueError:
    print("Invalid input. Please enter a valid integer.")
