def slice_tuple(input_tuple, start, end):
    return input_tuple[start:end]

user_input = input("Enter a tuple (comma-separated values): ")
my_tuple = tuple(user_input.split(","))
start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))
sliced_tuple = slice_tuple(my_tuple, start, end)
print("Sliced tuple:", sliced_tuple)
