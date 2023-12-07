def find_index_of_item(input_tuple, item):
    if item in input_tuple:
        return input_tuple.index(item)
    else:
        return -1  # Item not found

user_input = input("Enter a tuple (comma-separated values): ")
my_tuple = tuple(user_input.split(","))
item_to_find = input("Enter the item to find: ")
index = find_index_of_item(my_tuple, item_to_find)
if index != -1:
    print(f"Index of {item_to_find} in the tuple is: {index}")
else:
    print(f"{item_to_find} not found in the tuple.")
