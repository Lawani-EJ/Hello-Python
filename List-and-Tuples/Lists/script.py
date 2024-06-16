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

appendList = ["Michaeal Jackson", 10.2]
appendList.append(["a","b","c"])
print(appendList)

changeList = ["disco", 10, 1.2]
print("Before change:", (changeList))
changeList[0] = "funk"
print("After Change:",(changeList))
print("Before delete:", (changeList))
del(changeList[0])
print("After Delete:",(changeList))

splitString = "Hello,World,Python"
print(splitString.split(','))
print(type(splitString.split(',')))

copyList = ["hard Rock", 10, 1.3]
copiedList = copyList
print("Copy the list",copyList)
print("copied List",copiedList)
print ("copiedList[0]",copiedList[0])
copyList[0] = "Bannana"
print ("copiedList[0]",copiedList[0])

print ("copiedList[0]",copiedList[0])
copyList[0] = "hard rock"
print ("copiedList[0]",copiedList[0])
