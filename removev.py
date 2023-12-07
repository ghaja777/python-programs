# Ask the user for input
input_string = input("Enter a string: ")

# Function to remove vowels from a string
def remove_vowels(input_str):
    vowels = "AEIOUaeiou"  # Define a string of vowels
    result_str = ''.join([char for char in input_str if char not in vowels])
    return result_str

# Remove vowels from the input string
result = remove_vowels(input_string)

# Print the result
print("String with vowels removed:", result)
