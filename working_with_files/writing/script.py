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
