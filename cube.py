import math

def calculate_cube(num):
    cube = num ** 3
    return cube

def calculate_cube_root(num):
    cube_root = num ** (1/3)
    return cube_root

while True:
    print("Choose an option:")
    print("1. Calculate Cube")
    print("2. Calculate Cube Root")
    print("3. Quit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        num = float(input("Enter a number to calculate its cube: "))
        cube = calculate_cube(num)
        print(f"The cube of {num} is: {cube}")
    elif choice == '2':
        num = float(input("Enter a number to calculate its cube root: "))
        if num >= 0:
            cube_root = calculate_cube_root(num)
            print(f"The cube root of {num} is: {cube_root}")
        else:
            print("Cube root is not defined for negative numbers.")
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
