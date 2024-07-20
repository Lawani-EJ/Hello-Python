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