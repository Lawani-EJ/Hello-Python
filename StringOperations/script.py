#Considering the following string
#"01234567"

Numbers = "0123456"

#When obtaining the even elements
#We can perform the string operations

Numbers[::2]
print(Numbers[::2])

#Another sring manipulation can be performed 
#In getting the result of the following line of code

"0123456".find('1') 
print("0123456".find('1'))

#Indexing of string
name = "Micheal Jackson"
name

print(name[0])
print(name[6])
print(name[13])

#Negative Indexing
print(name[-1])
print(name[-15])
print(len(name))

#slicing
#Taking the slice on the varaible name from the index 0 - 3
print(name[0:4])
##Taking the slice on the varaible name from the index 8 - 11
name[8:12]

#stride
#Getting every second element from the index 1,3,5
print(name[::2])
#Incoporating the slicing with stride, Getting every second element from the index 0-4
print(name[0:5:2])
