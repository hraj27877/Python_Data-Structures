coordinates = (10, 20, 30)  # Tuple to store immutable coordinates

def get_user_info():
    return ("John", 30, "Engineer")  # Returning a tuple with multiple values

name, age, profession = get_user_info()  # Unpacking the tuple into individual variables

point = (1, 2)  # Tuple used as a key
coordinates_dict = {point: "A"}  # Tuple as dictionary key

packed = 1, 2, 3  # Packing values into a tuple
a, b, c = packed  # Unpacking the tuple into variables

numbers = [1, 2, 2, 3, 4, 4]  # List with duplicate elements
unique_numbers = set(numbers)  # Converting list to set removes duplicates

set1 = {1, 2, 3}  # First set
set2 = {2, 3, 4}  # Second set

union_set = set1 | set2  # Union of set1 and set2 (all unique elements)
intersection_set = set1 & set2  # Intersection of set1 and set2 (common elements)
difference_set = set1 - set2  # Difference between set1 and set2 (elements in set1 but not in set2)

colors = {"red", "blue", "green"}  # Set of colors
if "blue" in colors:  # Checking if "blue" exists in the set
    print("Blue is in the set!")

words = {"apple", "banana", "cherry"}  # Set of words
if "banana" in words:  # Checking if "banana" is in the set
    print("Banana is in the set!")
