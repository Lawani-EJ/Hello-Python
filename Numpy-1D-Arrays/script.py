# Class Question What is the result of the following operations
# Provide Answers 
import numpy as np
result1 = np.array([1,-1]) * np.array([1,1])
print(result1)
result2 = np.dot(np.array([1,-1]),np.array([1,1]))
print(result2)

a = [1,2,3,4,5]
# cast the following list into a numpy array 
x = np.array(a)
# find the type of x using the function type() 
print(type(x))
# find the shape of the array 
print(x.shape)
# find the mean of the array 
print(x.mean)
# find the type of data in the array 
print(x.dtype)
