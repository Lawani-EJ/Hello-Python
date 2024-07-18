count = 1 
while count <= 5:
    print(count)
    count += 1

dates = [1982,1980,1973,2000]
i = 0
year = dates[0]

while (year != 1973):
    print(year)
    i = i+1
    year = dates[i]

print("It  took ",  i , "Repititions to exit this loop")