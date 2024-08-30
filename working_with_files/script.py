# importing the required library
import urllib .request
# setting up the URL
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
# Downloading the file
urllib.request.urlretrieve(url, filename)

print("Download done")

example1 = "example1.txt"

# Reading the example file 
file1 = open(example1, "r")
# printing the path of the file 
print(file1.name)
print(file1.mode)

FileContent = file1.read()
print(FileContent)
print(type(FileContent))

# Reading with (with) statement
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

    # Verifying if the file is closed 
    print(file1.closed)

# Reading the first 4 characters 
with open(example1, "r") as file1:
    Content = file1.read(4)
    print(Content)

#Reading the certain amount of characters
with open(example1, "r") as file1:
    Content1 = file1.read(4)
    Content2 = file1.read(4)
    Content3 = file1.read(7)
    Content4 = file1.read(15)

    print(Content1)
    print(Content2)
    print(Content3)
    print(Content4)

#Reading a one line
with open(example1, "r") as file1:
    ContentLine = "First Line " + file1.readline()
    print(ContentLine)

# passing arguments specifying the number of character to be read
with open(example1, "r") as file1:
    ArgumentContent1 = file1.readline(20)
    ArgumentContent2 = file1.read(20)
    print(ArgumentContent1)
    print(ArgumentContent2)

# iterating in each line 
with open(example1, "r") as file1:
    i = 0;
    for line in file1:
        print("Iteration", str(i), ": ", line)
        i = i + 1

# reading through all the lines and saving them as a list 
with open(example1, "r") as file1:
    FileAsList = file1.readlines()
    print(FileAsList[0])
    print(FileAsList[1])
    print(FileAsList[2])