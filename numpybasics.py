import numpy as np

# Create 1D array
list1D = [0, 1, 2, 3, 4]
array1D = np.array(list1D)

# Print the array and its type
print(type(array1D))
print(array1D)

# Add 33 to each and every items
array1D+3
print("\nOperation Performed:")
print(array1D)

# Create 2D array
list2D = [[1, 2, 3, 4], [1, 3, 5], [7, 8, 6]]
array2D = np.array(list2D)
print("\n2D Array:")
print(array2D)

# Assign datatype to ndarray or n-dimensional array
# Possible data types are 'float', 'int', 'str', 'bool' and 'object'
list2D = [[1, 3, 4], [1, 3, 5], [7, 8, 6]]
array2D = np.array(list2D, dtype='float')
print("\nFloat Data Type:")
print(array2D)

array2D = np.array(list2D, dtype='int')
print("\nInt Data Type:")
print(array2D)

array2D = np.array(list2D, dtype='str')
print("\nString Data Type:")
print(array2D)

array2D = np.array(list2D, dtype='bool')
print("\nBoolean Data Type:")
print(array2D)

list2D = [[1, 'a', True], ['b', True, 5], [False, 8.5, 'c']]
array2D = np.array(list2D, dtype='object')
print("\nObject Data Type:")
print(array2D)

# Get information about an array
print("\nShape: ", array2D.shape)
print("DataType: ", array2D.dtype)
print("Size: ", array2D.size)
print("Dimension: ", array2D.ndim)

# Extract 2 rows and columns
print("\nExtracted 2 Rows", array2D[:2, :2])

# Extract with boolean index
list2D = [[1, 2, 3], [1, 3, 5], [7, 8, 6]]
array2D = np.array(list2D)
b = array2D > 2
print("Boolean Index")
print(b)
print(array2D[b])

# Reverse only row positions
print("\nRow Position Reversed:")
print(array2D[::-1, ])

# Reverse row & column positions
print("\nRow & Column Position Reversed:")
print(array2D[::-1, ::-1])