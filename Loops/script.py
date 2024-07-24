#First introduction class with loops an while loops
A = [3,4,5]
for i in A:
    print(i)


x = 3
y = 1
while(y!=x):
    print(y)
    y = y+1

dates = [1980,1982,1973]
N = len(dates)
for i in range (N):
    print(dates[i])

    for x in range(0,8):
        print(x)

for year in dates:
    print(year)

squares = ["red","Yellow","Green","Purple","Blue"]
for i in range(0,5):
    print("Before number square: ", i , "was" , squares[i])
    squares[i] = "white"
    print("Now after number square: ", i, "is", squares[i])

for i , square in enumerate(squares):
    print(i,square)

# class quiz
# Write a loop that iterates through the elements of 5 and -5

for i in range(-4,5):
    print(i)

#create a list and print out the elements in that list using a for loop
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
print(type(Genres))

for genre in Genres:
    print(genre)

#Create a while loop that displays all the values for the rating of an album playlist's rating list
PlaylistRatings = [10,9.5,10,8,7.5,5,10,10]
#if the score is less than 6 exit the loop 
i = 0
rating =  PlaylistRatings[0]
while(i < len(PlaylistRatings) and rating >=6):
    print(rating)
    i = i+1
    rating = PlaylistRatings[i]
    

# Create a while loop that will copy the strings 'orange' of this given list squares to the provided list that is given below 
squares = ['orange', 'orange', 'purple', 'blue', 'orange']
new_squares = []
# make sure it exits the loop if the value on the list isn't orange
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
    print(new_squares) 

# Your little brother has just learned multiplication tables in school. Today he has learned tables of 6 and 7 help him memorise both the tables by printing them using a for loop 
print("The multiplication table of 6 = ")
for i in range (10):
    print("6*",i,"=",6*i)
print("The multipluication table of 7 = ")
for i in range (10):
    print("7*",i,"=",7*i)

# Your brother needs to write an essay on the animals he saw at the zoo whose names are made of 7 letters help him find those animals through a while loop and create a seperate list for such animals
Animals = ["lion","giraffe","gorilla","parrots","crocodile","deer","swan"]
New = []
i = 0
while i<len(Animals):
    j = Animals[i]
    if(len(j)==7):
        New.append(j)
        i = i+1
        print(New)
