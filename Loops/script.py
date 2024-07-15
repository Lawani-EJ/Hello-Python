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
N = len (dates)
for i in range (N):
    print(dates[i])

    for x in range(0,8):
        print(x)

for year in dates:
    print(year)

squares = ["red","Yellow","Green","Blue"]
for i in range(0,5):
    print("Before number square: ", i , "was" , squares[i])
    squares[i] = "white"
    print("Now after number square: ", i, "is", squares[i])

for i , square in enumerate(squares):
    print(i,square)