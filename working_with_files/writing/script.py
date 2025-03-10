# writing a line to a file 
exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A \n")

# Writing multiple lines into that file 
with open(exmp2, 'w') as writefile:
    writefile.write("This is line B \n")
    writefile.write("This is line C \n")
    writefile.write("This is line D \n")

# Reading the file checking it works
with open(exmp2, 'r') as testWrite:
    print(testWrite.read())

# Writing a list into that text file 
Lines = ["This is list A \n", "This is list B \n", "This is list C \n",]
with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        # print(line)
        writefile.write(line)

# Verifying and reading if writing has been implemented successfully
with open('Example2.txt', 'r') as testList:
    print(testList.read())

# Appending
with open('Example2.txt', 'a') as performAppend:
    performAppend.write("This is line C \n")
    performAppend.write("This is line D \n")
    performAppend.write("This is line E \n")
    performAppend.write("Im just testing \n")

# Veryfying and reading if appending has been perforomed 
with open('Example2.txt','r') as testAppend:
    print(testAppend.read())

# an additional mode
# a+ : Appending and Reading. Creates a new file, if none exists. 

with open('Example2.txt', 'a+') as testWritefile:
    testWritefile.write("This is the second time testing \n")
    print(testWritefile.read())

# Copying a file
# Copying a file into another
with open('Example2.txt', 'r') as readThefile:
    with open('Example3.txt', 'w') as writeThefile:
        for line in readThefile:
            writeThefile.write(line)

# Now verifying if the copy has been successfully executed
with open('Example3.txt', 'r') as testThefile:
    print(testThefile.read())
