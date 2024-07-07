# age = 19
age = 17
if age < 18:
    print("You cannot Enter the Concert")
    # print("You can Enter")

user_age = 18
if user_age > 18:
    print("You are eligible to visit this website")
else:
    print("You are not eligible to vist the site")

    user2_age = 15 
    if user2_age > 18:
        print("You are eligible to visit this website")
    elif user2_age == 18:
        print("You are eligible to visit this website proceed to login!!!")
    else:
        print("You are not eligible to visit this website")
        print("Exit page!!")


album_year = 1983
album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
    print ("Do something")


album2_year = 1985
if album2_year > 1980:
        print("Album year is greater than 1980")
else :
     print("This album is less than 1980")
     print("Do something")

album3_year = 2000
if (album3_year > 1980) and (album3_year < 2021) :
    print("Album Year was Between 1980 and 2021")
    print("Loading..........")
    print("Doing Some stuff")

album4_year = 2023
if (album4_year < 2021) or (album4_year > 2022):
     print ("Thea Album Was Not Made in 2023")
else :
     print("The Album Was Made in 2023")

album5_year = 2024
if not (album5_year == 2021):
     print("Album 5's year is not 2021 it's 2024")