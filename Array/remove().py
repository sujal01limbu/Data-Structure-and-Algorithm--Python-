
import array

# Create an array of integers
number_array = array.array("i", [1,2,3,4])

# Print the initial array
print("Original array: ",end= " ")

for i in range(len(number_array)):

    print(number_array[i],end=" ")

print()

#Using remove to remove first occurence of element from array
number_array.remove(1)



#Modified Array
print("Modified Array: ", end=" ")

for i in range(len(number_array)):

    print(number_array[i],end=" ")
