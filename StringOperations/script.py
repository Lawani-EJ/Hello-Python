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

#Importing the re built-in-method
import re

#RegEx Method
#In python RegEx(Short for Regular Expression) is a tool for handling and matching strings
#The RegEx provides several functions for working with regular expressions
#These include search,split,findall and sub.
sl = "This is me testing RegEx!"

#Define the pattern to search for 
pattern = r"testing"

#Using the search() function to search for the pattern in the string
search_result = re.search(pattern, sl)

#Checking if a match was found 
if search_result:
    print("Match Found!!!")
    print("Thank You!")
else:
    print("Match Not Found!")

import re
# more RegEx examples
# \d Matches any digit character (0-9)
my_pattern = r"\d\d\d\d\d\d\d\d\d\d"
text1 = "My Phone Number is 1234567890"
match = re.search(my_pattern, text1)

if match:
        print("Phone number found!!!", match.group())
else:
     print("No Match!")
# the regular expression pattern is defined as r"\d\d\d\d\d\d\d\d\d\d", which uses the \d special sequence to match any digit character (0-9), and the \d sequence is repeated 10 times to match the ten consecutive didigts
# More examples
# \w special sequence 
# \w mathces any non-word character

import re
my_pattern2 = r"\W"
text2 = "Hello-world!!!"
matches = re.findall(my_pattern2,text2)

print("Mathces:",matches) 
# the /W expression is used to match any non-word character,these are characters that are not letters (a-z) (A-Z) (0-9) and (_)


# findall method
# the findall method is able to find all the occurances of a specified pattern in a string
import re
s2 = "Micheal Jackson was a singer and Known as the King of Pop!!"
# using the find all method to find the ocurrances of the letter 'as' in the string
the_result = re.findall("as",s2)
print(the_result)

# the split method
# the split function splits a string into an array of substrings based on a specific pattern
# using the split function to split the string by the "\s"
splitting_array = re.split("\s",s2)

# printing out the the split array, the split array contains all the substrings, split by whitespace characters
print(splitting_array)

# the sub function
# the sub function of a regular expression in python is used to replace all occurances of a pattern in a string with a specified replacement
# Defining the regular expression pattern to search for
my_pattern3 = r"King of Pop"

# Defining the replacement string 
replacement = "legend"

# using the sub function to replace the pattern with the replacement string
new_string = re.sub(my_pattern3, replacement, s2, flags=re.IGNORECASE)

#In printing the new_string the new string contains the original string with the pattern replaced by the replacement string
print(new_string)

# Finding the four consectuive digit characters using \d and the search function
import re
the_pattern = "House number-20111"
the_pattern = re.search("\d",the_pattern)
if the_pattern:
     print("Digit found in the Pattern") #When the pattern is "House number-20111" having a digit number
else:
     print("Digit not Found in the Pattern!") #When the pattern is "House number" not having a digit number

# For the string strl, replacing the sub-string fox with bear using the sub
import re
strl = "The quick brown fox jumps over the lazy dog."
strl2 = r"fox"
replacement_word = "bear"
new_strl = re.sub(strl2,replacement_word,strl, flags=re.IGNORECASE)
print(new_strl)

# finding all occurances in a string
import re
strl3 = "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
finding = re.findall("woo",strl3)
print(finding)