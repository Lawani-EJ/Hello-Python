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

# Class questions
# Question 2
# Write a Python program to get a list, sorted in increasing order by the last element in each tuple, from a given list of non-empty tuples.
Sample_List = ([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]) 
Sample_List.sort(key = lambda x:x[-1])
print(Sample_List)

# Question 3 
# Write a Python program that combines two dictionaries by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

CombinedDictionary = (d1 | d2)
print(CombinedDictionary)

# Question 1 
# Write a Python program that multiplies all the items in a list.
import math
Sample_list= [2, 3, 6]
print(math.prod(Sample_list))

# Question 5
# Write a program to sort a tuple by its float element.
# For example: 
list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
list.sort(reverse=True)
print(list)

# Question 6
# Write a Python program to create a set.
SampleSets = {0,1,2,3,4,5}
# Write a Python program to iteration over sets.
for SampleSet in SampleSets:
    print(SampleSet)
# Write a Python program to add members in a set
SampleSets.add("Micheal")
SampleSets.add("Thriller")
# and to remove items from a given set.
SampleSets.remove("Thriller")
print(SampleSets)