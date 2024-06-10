Numbers = "0123456"

Numbers[::2]
print(Numbers[::2])

"0123456".find('1') 
print("0123456".find('1'))

name = "Micheal Jackson"
name

print(name[0])
print(name[6])
print(name[13])

print(name[-1])
print(name[-15])
print(len(name))

print(name[0:4])
print(name[8:12])

print(name[::2])
print(name[0:5:2])

statement = name + " " +"Is the best"
print(statement)

print(3 * name)

name = name + " " + "Dances Pretty well."
print(name)

print("Micheal Jackson \n is the best")

print("Micheal Jackson \t is the best")

print("Micheal Jackson is \\ the best")

print(r"Micheal Jackson \ is the best")

a = "Thriller is his sixth studio album"
print("Before applying upper:", a)

b = a.upper()

print("After applying upper:", b)

a = "MICHEAL JACKSON IS THE BEST"
print("Before applying lower:", a)

b = a.lower()

print("After applying lower:", b)

a = "Micheal Jackson is the best0"
b = a.replace('Micheal',' KingKrule')
print(b)

test_string = "Hello! Micheal Jackson has: 42 Characters."
print (len(test_string))
b = test_string.replace('!',' ').replace(':',' ').replace('.', ' ')
print(b)


atrtist_name = "King Krule"
print(atrtist_name.find("Kr"))
print(atrtist_name.find("Krule"))

print(atrtist_name.find("qwertyuiop"))

splitting_string = (atrtist_name.split())
print(splitting_string)

import re

sl = "This is me testing RegEx!"

pattern = r"testing"

search_result = re.search(pattern, sl)

if search_result:
    print("Match Found!!!")
    print("Thank You!")
else:
    print("Match Not Found!")

import re
my_pattern = r"\d\d\d\d\d\d\d\d\d\d"
text1 = "My Phone Number is 1234567890"
match = re.search(my_pattern, text1)

if match:
        print("Phone number found!!!", match.group())
else:
     print("No Match!")

import re
my_pattern2 = r"\W"
text2 = "Hello-world!!!"
matches = re.findall(my_pattern2,text2)

print("Mathces:",matches) 

import re
s2 = "Micheal Jackson was a singer and Known as the King of Pop!!"
the_result = re.findall("as",s2)
print(the_result)

splitting_array = re.split("\s",s2)

print(splitting_array)

my_pattern3 = r"King of Pop"

replacement = "legend"

new_string = re.sub(my_pattern3, replacement, s2, flags=re.IGNORECASE)

print(new_string)

import re
the_pattern = "House number-20111"
the_pattern = re.search("\d",the_pattern)
if the_pattern:
     print("Digit found in the Pattern") 
else:
     print("Digit not Found in the Pattern!") 

import re
strl = "The quick brown fox jumps over the lazy dog."
strl2 = r"fox"
replacement_word = "bear"
new_strl = re.sub(strl2,replacement_word,strl, flags=re.IGNORECASE)
print(new_strl)

import re
strl3 = "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
finding = re.findall("woo",strl3)
print(finding)

practice = "Lizz"
print(practice[0:2])

var = '123456789'