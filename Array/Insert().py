
import array

# Create an array of integers
number_array = array.array("i", [1,2,3,4])

# Print the initial array
print("Original array: ",end= " ")

for i in range(len(number_array)):

    print(number_array[i],end=" ")

number_array.insert(3,5)

print()

#Insert Array
print("Inserted Array: ", end=" ")

#Modified Array
for i in range(len(number_array)):

    print(number_array[i],end=" ")
