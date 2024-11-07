# Creating a list with different types of elements
my_list = [1, "apple", 3.14, True]
print(my_list)

# Accessing elements by index
print("First element:", my_list[0])  # Output: 1
print("Second element:", my_list[1]) # Output: "apple"

# Changing the second element
my_list[1] = "orange"
print("Modified list:", my_list)

# Appending an element to the end of the list
my_list.append("banana")
print("After appending:", my_list)

# Inserting an element at a specific position
my_list.insert(2, "grape")
print("After inserting at index 2:", my_list)

# Removing a specific element by value
my_list.remove("orange")
print("After removing 'orange':", my_list)

# Removing an element by index
removed_item = my_list.pop(2)
print("After popping index 2:", my_list)
print("Popped item:", removed_item)

# Slicing a list to get a sublist
sub_list = my_list[1:3]  # Gets elements from index 1 up to, but not including, index 3
print("Sliced list:", sub_list)

# Creating a list of numbers for demonstration
numbers = [3, 1, 4, 1, 5, 9]

# Getting the length, maximum, and minimum values
print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))

# Sorting the list in ascending and descending order
numbers.sort()
print("Sorted in ascending order:", numbers)

numbers.sort(reverse=True)
print("Sorted in descending order:", numbers)

# A list with duplicates and different types of elements
mixed_list = ["apple", 42, 42, "apple", 3.14, True]
print("List with duplicates and mixed types:", mixed_list)
