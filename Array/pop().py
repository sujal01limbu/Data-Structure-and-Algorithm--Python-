
import array

# Create an array of integers
number_array = array.array("i", [1,2,3,4])

# Print the initial array
print("Original array: ",end= " ")

for i in range(len(number_array)):

    print(number_array[i],end=" ")

print()

#Using pop to remove element from array
print("The pop element is : ",end=" ")
print(number_array.pop(2))


#Modified Array
print("After Popped Array: ", end=" ")

for i in range(len(number_array)):

    print(number_array[i],end=" ")
