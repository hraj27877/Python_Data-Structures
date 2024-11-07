# Define a sample string
text = "Hello, World!"

# 1. Basic Slicing Examples

# Extract the first five characters
print(text[0:5])  # Output: "Hello" (slices from index 0 up to, but not including, index 5)

# Slice from index 7 to the end
print(text[7:])   # Output: "World!" (slices from index 7 to the end of the string)

# Slice from the beginning up to index 5
print(text[:5])   # Output: "Hello" (starts from the beginning and goes up to index 5)

# 2. Slicing with a Step

# Extract every second character
print(text[::2])  # Output: "Hlo ol!" (takes every second character from the string)

# Reverse the string
print(text[::-1])  # Output: "!dlroW ,olleH" (step -1 reverses the string)

# 3. Negative Indices

# Extract the last five characters
print(text[-5:])  # Output: "orld!" (slices from the fifth-last character to the end)

# Slice using negative indices
print(text[-7:-1])  # Output: "World" (slices from the 7th-last up to the 1st-last character)
