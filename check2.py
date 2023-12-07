# Ask the user for input
number = int(input("Enter a number: "))

# Check if the number is a power of 2
def is_power_of_two(num):
    if num <= 0:
        return False
    return (num & (num - 1)) == 0

if is_power_of_two(number):
    print(f"{number} is a power of 2.")
else:
    print(f"{number} is not a power of 2.")
