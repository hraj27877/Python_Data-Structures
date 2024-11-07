# Example 1 :-

my_dict = {
    (1, 2, 3): "a tuple",  # tuple is immutable
    "name": "John"
}

# Accessing the value with the key
print(my_dict[(1, 2, 3)])  # Output: a tuple

# Example 2 :-

my_dict = {
    [1, 2, 3]: "a list"  # list is mutable, this will raise an error
}

# Example 3 :-

# Valid keys (immutable types)
my_dict = {
    42: "integer",
    "key": "string",
    (1, 2): "tuple"
}

# Invalid key (mutable type)
try:
    my_dict[[1, 2]] = "list"  # This will raise TypeError
except TypeError as e:
    print(e)  # Output: unhashable type: 'list'
