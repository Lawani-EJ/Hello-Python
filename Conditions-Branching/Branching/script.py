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

#given quiz
#There are 2 sisters Annie and Jane born in 1996 amd 1999 respectively. They want to know who was born in a leap year Write an if else statement to determine  who was born in a leap year
Annie = 1996
Jane = 1999

if Annie %4 == 0:
     print("Annie was born in a leap year!")
elif Jane %4 == 0:
    print("Jane was born in a leap year!")
else:
     print("None of them were born in a leap year!") 

#quiz2
# In a school canteen children under the age of 9 are only given milk porridge  for breakfast children from 10-14 are given a sandwich and children from 15-17 are given a burger.
# The canteen master asks the age of the student and gives them breakfast accordingly . Sam's age is 10 using an if-else statement dtermine what the canteen master will serve him 
#Solution
Milk_porridge = 9
Sandwich = 14
Burger = 17

Sam = 10

if Sam > Milk_porridge:
     print("Sam takes milk porridge for breakfast!")
elif Sam > Sandwich:
     print("Sam takes Sanwich for brakfast!")
elif Sam > Burger:
     print("Sam Takes Burger for beakfast!")

# Correction
age = 10

if age <= 9:
    print("You will get a bowl of porridge!")
elif age >=10 and age <= 14:
     print("You will get a sandwich!")
elif age >= 15 and age <= 17:
    print("You will get a burger!")