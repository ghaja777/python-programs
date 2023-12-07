def square_root(number, epsilon=1e-6):
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number")

    guess = number  # Initial guess
    while True:
        new_guess = 0.5 * (guess + number / guess)
        if abs(new_guess - guess) < epsilon:
            return new_guess
        guess = new_guess

# Example usage:
num = 25
result = square_root(num)
print(f"The square root of {num} is approximately {result:.6f}")