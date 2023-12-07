def remove_item_from_tuple(input_tuple, item_to_remove):
    if item_to_remove in input_tuple:
        index = input_tuple.index(item_to_remove)
        result_list = list(input_tuple)
        result_list.pop(index)
        return tuple(result_list)
    else:
        return input_tuple

user_input = input("Enter a tuple (comma-separated values): ")
my_tuple = tuple(user_input.split(","))
item_to_remove = input("Enter the item to remove: ")
new_tuple = remove_item_from_tuple(my_tuple, item_to_remove)
print("Updated tuple:", new_tuple)

