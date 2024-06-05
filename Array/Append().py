import array

# Create an array of integers
number_array = array.array("i", [1, 2, 3])

# Print the initial array
print("Original Array:")
for i in range(len(number_array)):
    print(number_array[i])

# Append a new element (4) to the array
number_array.append(4)

# Print the modified array
print("\nModified Array:")
for i in range(len(number_array)):
    print(number_array[i])
