# Define a list
fruits = ["apple", "banana", "cherry"]

# Access elements using indexing
print(fruits[0])  # Output: apple (first element)
print(fruits[1])  # Output: banana (second element)
print(fruits[-1]) # Output: cherry (last element)

# Modify an element in the list
fruits[1] = "blueberry"  # Change 'banana' to 'blueberry'

# Print the updated list
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Define a list
fruits = ["apple", "banana", "cherry"]

# Delete an element by index
del fruits[1]  # Remove 'banana' at index 1

# Print the updated list
print(fruits)  # Output: ['apple', 'cherry']

# Define a list
fruits = ["apple", "banana", "cherry"]

# Remove and return the element at index 1
removed_item = fruits.pop(1)  # Removes 'banana'
print(removed_item)  # Output: banana

# Print the updated list
print(fruits)  # Output: ['apple', 'cherry']

# Define a list
fruits = ["apple", "banana", "cherry"]

# Remove the first occurrence of a specific value
fruits.remove("banana")  # Removes 'banana'

# Print the updated list
print(fruits)  # Output: ['apple', 'cherry']

