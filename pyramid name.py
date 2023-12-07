def print_name_pyramid(name):
    length = len(name)
    for i in range(1, length + 1):
        spaces = " " * (length - i)
        characters = name[:i]
        print(spaces + characters)

def print_inverse_name_pyramid(name):
    length = len(name)
    for i in range(length, 0, -1):
        spaces = " " * (length - i)
        characters = name[:i]
        print(spaces + characters)

try:
    user_input = input("Enter the name: ")
    print("Name Pyramid Pattern:")
    print_name_pyramid(user_input)
    print("Inverse Name Pyramid Pattern:")
    print_inverse_name_pyramid(user_input)
except ValueError:
    print("Please enter a valid name.")

