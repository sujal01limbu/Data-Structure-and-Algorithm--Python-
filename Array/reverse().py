
import array

# Create an array of integers
number_array = array.array("i", [1,2,3,4])

# Print the initial array
print("Original array: ",end= " ")

for i in range(len(number_array)):

    print(number_array[i],end=" ")

print()

#Using reverse() to reverse the array
number_array.reverse()

#Modified Array
print("Modified Array: ", end=" ")

for i in range(len(number_array)):

    print(number_array[i],end=" ")
