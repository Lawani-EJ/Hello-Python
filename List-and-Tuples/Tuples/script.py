tuple1 = ("disco",10,1.5)
print(type(tuple1))

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

print(tuple1[-1])
print(tuple1[-2])
print(tuple1[-3])

tuple2 = tuple1 + ("hard rock" ,10)
print(tuple2)
print(type(tuple2))

print(tuple2[0:3])
print(tuple2[3:4])
print(tuple2[3:5])
print(tuple1[0:2])


tuple3 = (0,9,6,5,10,8,9,6,2)
print(tuple3)
print(len(tuple3))

tupleSort = sorted(tuple3)
print(tupleSort)

NestTuple = (1,2,("pop","rock"),(3,4),("disco",(1,2)))

print(NestTuple[0])
print(NestTuple[1])
print(NestTuple[2])
print(NestTuple[3])
print(NestTuple[4])

print("Element 2, 0 of Tuple: ",   NestTuple[2][0])
print("Element 2, 1 of Tuple: ",   NestTuple[2][1])
print("Element 3, 0 of Tuple: ",   NestTuple[3][0])
print("Element 3, 1 of Tuple: ",   NestTuple[3][1])
print("Element 4, 0 of Tuple: ",   NestTuple[4][0])
print("Element 4, 1 of Tuple: ",   NestTuple[4][1])

print(NestTuple[2][1][0])
print(NestTuple[2][0][0])
print(NestTuple[2][1][1])
print(NestTuple[4][1][0])
print(NestTuple[4][1][1])
print(NestTuple[4][0][1])

genres_tuples = ("pop","rock","soul","hard-rock","soft-rock","R&B","progressive rock","disco")
print(len(genres_tuples))