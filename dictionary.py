# Create a dictionary
my_dict = {'a': 1, 'b': 2}

# Add a new key-value pair
my_dict['c'] = 3

# Output: {'a': 1, 'b': 2, 'c': 3}
print(my_dict)

# Modify the value of an existing key
my_dict['a'] = 10

# Output: {'a': 10, 'b': 2, 'c': 3}
print(my_dict)

# Delete an item using its key
del my_dict['b']

# Output: {'a': 10, 'c': 3}
print(my_dict)

# Delete an item using pop() and get its value
removed_value = my_dict.pop('c')

# Output: 3
print(removed_value)

# Output: {'a': 10}
print(my_dict)
