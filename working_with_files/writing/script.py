# writing a line to a file 
exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")

# Reading the file checking it works
with open(exmp2, 'r') as testWrite:
    print(testWrite.read())