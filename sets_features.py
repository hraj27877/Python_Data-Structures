# Creating a set
my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

# Adding elements
my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Removing elements
my_set.remove(3)  # Removes 3 from the set
print(my_set)  # Output: {1, 2, 4, 5}

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union
union_set = set_a | set_b
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection
intersection_set = set_a & set_b
print(intersection_set)  # Output: {3, 4}

# Difference
difference_set = set_a - set_b
print(difference_set)  # Output: {1, 2}

# Symmetric Difference
sym_diff_set = set_a ^ set_b
print(sym_diff_set)  # Output: {1, 2, 5, 6}

for element in my_set:
    print(element)

# Check if an element is in the set
print(3 in my_set)  # Output: False
print(4 in my_set)  # Output: True
