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

# What are the elements on the first row and first and second columns?
print(A[0][0:2])

# What are the elements on the first and second rows and third column?
print(A[0:2, 2])

# Performance on some basic operations
# create a numpy array
X = np.array([[1,0],[0,1]])
print(X)
# create a second numpy array Y 
Y = np.array([[2,1],[1,2]])
print(Y)

# multiplying Y with 2
Z = 2 * Y
print(Z)

# Performing matrix operations
# create matrix A
A = np.array([[0,1,1],[1,0,1]])
print(A)

# create matrix B
B = np.array([[1,1],[1,1],[-1,1]])
print(B)

# calculate the dot product
Z = np.dot(A,B)
print(Z)

# calculate the sine of Z
Z_sin = np.sin(Z)
print(Z_sin)

# Calculating transposed matrix 
C = np.array([[1,1],[2,2],[3,3]])
print(C)
C_T = C.T
print(C_T)


# Class Quiz
# create an array and convert it to a Numpy Array
a = [[1,2,3],[4,5,6],[7,8,9]]
A = np.array(a)
print(A)
# caluclate that size of the array 
print(A.size)
# Now access the first row and second column of the array
print(A[0][1])
# Now you will perform a matrix multiplication of the array with B
B = np.array([[1,2],[3,4],[5,6]])
X = np.dot(A,B)
print(X)
