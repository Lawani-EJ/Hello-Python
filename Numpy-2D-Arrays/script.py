import numpy as np

# Create a list
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
print(a)
A = np.array(a)
print(A)
# Show the numpy array dimensions
print(A.ndim)
# Show the numpy array shape
print(A.shape)
# Show the numpy array size
print(A.size)

# Access the element on the second row and third column
print(A[1, 2])
# Access the element on the second row and third column
print(A[1][2])
# Access the element on the first row and first column
print(A[0][0])
