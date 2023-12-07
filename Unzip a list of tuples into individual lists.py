def unzip_tuples(tuple_list):
    return tuple(zip(*tuple_list))

user_input = input("Enter a list of tuples (comma-separated key-value pairs, e.g., 1,a;2,b;3,c): ")
tuple_list = [tuple(item.split(",")) for item in user_input.split(";")]
unzipped = unzip_tuples(tuple_list)
print("Unzipped:", unzipped)

