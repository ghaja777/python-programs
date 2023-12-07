# Ask the user for input to create a list of strings
string_list = []
while True:
    string = input("Enter a string (or 'q' to quit): ")
    if string.lower() == 'q':
        break
    string_list.append(string)

# Concatenate the list of strings into a single string
concatenated_string = ''.join(string_list)

# Print the concatenated string
print("Concatenated String:", concatenated_string)
