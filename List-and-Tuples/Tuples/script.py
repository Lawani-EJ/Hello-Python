# in python there are different data types these are integers, floats and strings
# these data types can be contained in a tuple
# first tuple
tuple1 = ("disco",10,1.5)
print(type(tuple1))

# Indexing, in indexing, each element of a tuple can be accesed via index.
# printing the variable of each index

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

# Negative indexing
print(tuple1[-1])
print(tuple1[-2])
print(tuple1[-3])

# concantination of tuples
tuple2 = tuple1 + ("hard rock" ,10)
print(tuple2)
print(type(tuple2))

# Slicing in tuples
# when slicing tuples we can obtain new tuples with the corresponding elements
print(tuple2[0:3])
print(tuple2[3:4])
print(tuple2[3:5])
print(tuple1[0:2])

# Sorting in tuples
tuple3 = (0,9,6,5,10,8,9,6,2)
print(tuple3)
# sorting the tuples in a value and saving it in a new tuple
tupleSort = sorted(tuple3)
print(tupleSort)
# When this result is printed out in the terminal it automatically sorts out the numbers

# Nesting in tuples
NestTuple = (1,2,("pop","rock"),(3,4),("disco",(1,2)))
#In creating the nested tuple, the tuple includes other tuples, and it can be obtained through the index
# printing the elements on each index of the tuple
print(NestTuple[0])
print(NestTuple[1])
print(NestTuple[2])
print(NestTuple[3])
print(NestTuple[4])

# also noting the use of the second index to access the other tuples
print("Element 2, 0 of Tuple: ",   NestTuple[2][0])
print("Element 2, 1 of Tuple: ",   NestTuple[2][1])
print("Element 3, 0 of Tuple: ",   NestTuple[3][0])
print("Element 3, 1 of Tuple: ",   NestTuple[3][1])
print("Element 4, 0 of Tuple: ",   NestTuple[4][0])
print("Element 4, 1 of Tuple: ",   NestTuple[4][1])