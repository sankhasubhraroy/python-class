# List is a dynamic array. We can store all types of items inside this
# List can contain duplicate values
# List in python is mutable (we can not modify the items)

# Declaring a list
arr = ["Hii", 25, 23.9, True]
print(arr)

# Accessing elements of a list
print("The first element: ", arr[0])
print("The last element: ", arr[len(arr) - 1])
print("The last element: ", arr[-1])

# Checking the type of element
print("The type first element: ", type(arr[0]))

# Creating a list by converting a tuple
arr2 = list((1, 6, 8, 3, "John"))
print(arr2)

# Creating list with repeated elements
arr3 = [4] * 10
print(arr3)

# Adding elements to the end of a list
arr3.append(7)
print(arr3)

# Adding elements in a particular index
arr3.insert(3, 6)
print(arr3)

# Adding multiple elements at the end of a list
arr3.extend([1, 8, 3, 9])
print(arr3)

# Updating a list
arr3[1] = 2
print(arr3)

# Removing the first occurrence from a list
arr3.remove(2)
print(arr3)

# Removing the last element from a list