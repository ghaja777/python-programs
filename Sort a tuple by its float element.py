def sort_tuple_by_float_element(input_tuple):
    try:
        sorted_tuple = tuple(sorted(input_tuple, key=lambda x: float(x) if isinstance(x, (int, float)) else x))
        return sorted_tuple
    except ValueError:
        return input_tuple

user_input = input("Enter a tuple (comma-separated values, including floats): ")
my_tuple = tuple(user_input.split(","))
sorted_tuple = sort_tuple_by_float_element(my_tuple)
print("Sorted tuple:", sorted_tuple)


