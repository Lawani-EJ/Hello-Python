# My Python Learning Journey
## Hello Python (Introduction)
Welcome to my Python learning journey. As a computer-science student diving in the world of python.
This README provides an overview of the different python concepts and functionalities i have explored and implemented.

# Learning the basic operations
In learning the basic operaions i begun my learning journey, by learning the fundamental arithemetic operations.. These are very essential for any programming language.
```
# Addition
print(4 + 5)

# Subtraction
print(8 - 5)

# Multiplication
print(5 * 3)

# Division
print(10 / 2)
```
# List and Tuples
In managing and organizing code, list and tuples are important data structures these are powerful ordered collections.

1. Lists :
    - lists are mutable and they allow for dynamic modification of their elements
2. Tuples
    - tuples are immutable and they offer the added benefit of being faster and memory efficient.

## Lists
```# Accessing the last element in a tuple
A = (0, 1, 2, 3, 4, 5, 6)
print(A[6])
print(A[-1])

# Slicing a list
B = ["a", "b", "c", "d", "e", "f", "g"]
print(B[2:])
```
# Tuples
```
# Creating and indexing tuples
tuple1 = ("disco", 10, 1.5)
print(type(tuple1))
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

# Negative indexing
print(tuple1[-1])
print(tuple1[-2])
print(tuple1[-3])

# Concatenation of tuples
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)

# Slicing tuples
print(tuple2[0:3])
print(tuple2[3:4])
print(tuple2[3:5])
print(tuple1[0:2])

# Sorting tuples
tuple3 = (0, 9, 6, 5, 10, 8, 9, 6, 2)
tupleSort = sorted(tuple3)
print(tupleSort)

# Nesting tuples
NestTuple = (1, 2, ("pop", "rock"), (3, 4), ("disco", (1, 2)))
print(NestTuple[0])
print(NestTuple[1])
print(NestTuple[2])
print(NestTuple[3])
print(NestTuple[4])
print("Element 2, 0 of Tuple:", NestTuple[2][0])
print("Element 2, 1 of Tuple:", NestTuple[2][1])
print("Element 3, 0 of Tuple:", NestTuple[3][0])
print("Element 3, 1 of Tuple:", NestTuple[3][1])
print("Element 4, 0 of Tuple:", NestTuple[4][0])
print("Element 4, 1 of Tuple:", NestTuple[4][1])
```
# String
In python string manipulation involve various operations that help modify and prcess strings. This is important because they are essential for data manipulation, text processing and generating dynamic content.

### Example
```
# String slicing and indexing
Numbers = "0123456"
print(Numbers[::2])
print("0123456".find('1'))

name = "Micheal Jackson"
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

# String concatenation
statement = name + " " + "Is the best"
print(statement)

# Repeating strings
print(3 * name)
name = name + " " + "Dances Pretty well."
print(name)

# Escape sequences
print("Micheal Jackson \n is the best")
print("Micheal Jackson \t is the best")
print("Micheal Jackson is \\ the best")
print(r"Micheal Jackson \ is the best")

# String methods
a = "Thriller is his sixth studio album"
print("Before applying upper:", a)
b = a.upper()
print("After applying upper:", b)

a = "MICHEAL JACKSON IS THE BEST"
print("Before applying lower:", a)
b = a.lower()
print("After applying lower:", b)

a = "Micheal Jackson is the best0"
b = a.replace('Micheal', 'KingKrule')
print(b)

test_string = "Hello! Micheal Jackson has: 42 Characters."
print(len(test_string))
b = test_string.replace('!', ' ').replace(':', ' ').replace('.', ' ')
print(b)

# String find method
artist_name = "King Krule"
print(artist_name.find("Kr"))
print(artist_name.find("Krule"))
print(artist_name.find("qwertyuiop"))

# String split method
splitting_string = artist_name.split()
print(splitting_string)
```

# RegEx (Regular Expressions)
regex in python are used in matching strings of text i.e characters, patterns or patterns of characters.

```
import re

# Search method
sl = "This is me testing RegEx!"
pattern = r"testing"
search_result = re.search(pattern, sl)
if search_result:
    print("Match Found!!!")
else:
    print("Match Not Found!")

# Matching digits
my_pattern = r"\d\d\d\d\d\d\d\d\d\d"
text1 = "My Phone Number is 1234567890"
match = re.search(my_pattern, text1)
if match:
    print("Phone number found!!!", match.group())
else:
    print("No Match!")

# Finding non-word characters
my_pattern2 = r"\W"
text2 = "Hello-world!!!"
matches = re.findall(my_pattern2, text2)
print("Matches:", matches)

# Find all occurrences
s2 = "Micheal Jackson was a singer and Known as the King of Pop!!"
the_result = re.findall("as", s2)
print(the_result)

# Split method
splitting_array = re.split("\s", s2)
print(splitting_array)

# Sub method
my_pattern3 = r"King of Pop"
replacement = "legend"
new_string = re.sub(my_pattern3, replacement, s2, flags=re.IGNORECASE)
print(new_string)

# Search for digits
the_pattern = "House number-20111"
the_pattern = re.search("\d", the_pattern)
if the_pattern:
    print("Digit found in the Pattern")
else:
    print("Digit not Found in the Pattern!")

# Replace substring
strl = "The quick brown fox jumps over the lazy dog."
strl2 = r"fox"
replacement_word = "bear"
new_strl = re.sub(strl2, replacement_word, strl, flags=re.IGNORECASE)
print(new_strl)

# Find all occurrences of a substring
strl3 = "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
finding = re.findall("woo", strl3)
print(finding)
```

###  As I continue to learn and grow, I look forward to diving deeper into more advanced topics and further enhancing my programming skills.

# Thank you 🙌👌


