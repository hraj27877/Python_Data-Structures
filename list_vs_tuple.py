# Tuple example
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)
print("Tuple index of 2:", my_tuple.index(2))
# my_tuple[1] = 4  # Uncommenting this will result in a TypeError because tuples are immutable

# List example
my_list = [1, 2, 3]
print("\nList:", my_list)
my_list.append(4)  # Adding a new element
print("List after append:", my_list)
my_list[1] = 5  # Modifying an element
print("List after modification:", my_list)
