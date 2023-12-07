# Function to calculate the square root without built-in functions
def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number")
    
    guess = number  # Initial guess
    while True:
        new_guess = 0.5 * (guess + number / guess)
        if abs(new_guess - guess) < 1e-6:  # Adjust this tolerance as needed
            return new_guess
        guess = new_guess

# Ask the user for input
try:
    num = float(input("Enter a number: "))
    
    # Calculate the square root
    result_square_root = calculate_square_root(num)
    print(f"The square root of {num} is approximately {result_square_root:.6f}")
    
except ValueError:
    print("Invalid input. Please enter a valid number.")

