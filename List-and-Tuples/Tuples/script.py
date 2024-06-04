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