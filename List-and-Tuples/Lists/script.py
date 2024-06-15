List = ["Micheal Jackson" ,10.1,1982]
print(List)
print(type(List))
print("Printing the same elements using negative and positive indexing: \n Positive index:",List[0], "\n Negative Index:",List[-3])
print("Printing the same elements using negative and positive indexing: \n Positive index:",List[1], "\n Negative Index:",List[-2])
print("Printing the same elements using negative and positive indexing: \n Positive index:",List[2], "\n Negative Index:",List[-1])

sampleList = ["Micheal Jackson", 10.1, 1982, [1,2], ("A",1)]
print(sampleList)
slicingList = ["Micheal Jackson", 10.1, 1982, "MJ", 1]
print(slicingList[3:5])

extendList = ["Michaeal Jackson", 10.2]
extendList.extend(['pop', 10])
print(extendList)

