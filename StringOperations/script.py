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
print(name[8:12])

#stride
#Getting every second element from the index 1,3,5
print(name[::2])
#Incoporating the slicing with stride, Getting every second element from the index 0-4
print(name[0:5:2])

#Concantenating two strings
statement = name + " " +"Is the best"
print(statement)

#Printing the string 3 times
print(3 * name)

#concantenating strings
name = name + " " + "Dances Pretty well."
print(name)

#Esacape Sequences
#New line escape sequence
print("Micheal Jackson \n is the best")

#New tab escape sequence 
print("Micheal Jackson \t is the best")

#Including backslash in string
print("Micheal Jackson is \\ the best")

#r tells python that the string should be displayed as a raw string
print(r"Micheal Jackson \ is the best")

#String method upper
#converts all the characters in a string to uppercase

a = "Thriller is his sixth studio album"
print("Before applying upper:", a)

b = a.upper()

print("After applying upper:", b)

#String method lower
#converting all the characters in the string to lowercase
a = "MICHEAL JACKSON IS THE BEST"
print("Before applying lower:", a)

b = a.lower()

print("After applying lower:", b)

#Replace method
a = "Micheal Jackson is the best0"
b = a.replace('Micheal',' KingKrule')
print(b)

#Replacing the old substrings with the new target substrings by removing several punctuations
test_string = "Hello! Micheal Jackson has: 42 Characters."
print (len(test_string))
b = test_string.replace('!',' ').replace(':',' ').replace('.', ' ')
print(b)

# Find Method
# The Find Method finds a sub-string.
#This FInds the substring in the string.
#Only the index of the first substring is going to be outputted

atrtist_name = "King Krule"
print(atrtist_name.find("Kr"))
print(atrtist_name.find("Krule"))

#If it can't find the substring in the string
# -1 is the output
print(atrtist_name.find("qwertyuiop"))

# The split method splits the string at the specified operator and returns, a list
# Splitting the substring into list
splitting_string = (atrtist_name.split())
print(splitting_string)