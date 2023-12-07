from itertools import combinations

# Input string
input_string = input("Enter a string: ")

# Generate and print all possible combinations
print("All possible combinations of the string:")
for r in range(1, len(input_string) + 1):
    for combo in combinations(input_string, r):
        print(''.join(combo))
