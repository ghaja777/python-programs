def tuple_to_dict(input_tuple):
    keys = range(len(input_tuple))
    return dict(zip(keys, input_tuple))

user_input = input("Enter a tuple (comma-separated values): ")
my_tuple = tuple(user_input.split(","))
my_dict = tuple_to_dict(my_tuple)
print("Dictionary:", my_dict)


