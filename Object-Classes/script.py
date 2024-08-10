class Car(object):
    def __init__(self,make,model,color):
        self.make = make
        self.model = model
        self.color = color
        self.owner_no = 0

    def car_info(self):
        print("Make: ",self.make)
        print("Model: ",self.model)
        print("Color: ",self.color)
        print("Number of owners",self.owner_no)
    
    def sell(self):
        self.owner_no += 1

my_car = Car("Honda","Accord","Black")

my_car.car_info()
my_car.sell()
my_car.car_info()

#Practice2
class Student:
    def __init__(self,firstname,lastname,age,sex):
        self.firstname = firstname
        self.lastname =lastname
        self.age = age
        self.sex = sex

#Create instances
Student1 = Student("Lawani Elyon","John",23,"M")
Student2 = Student("Gojo","Satorou",21,"M")
Student3 = Student("Hinata","Hyuga",20,"F")
print(f"Hello {Student1.firstname} and your age is {Student2.age}")

#Method practice2
class Student:
    def __init__(self,firstname,lastname,age,sex):
        self.firstname = firstname
        self.lastname =lastname
        self.age = age
        self.sex = sex
    def fullname(self):
        return self.firstname + " " + self.lastname
    def student_details(self):
        return print(f"This students name is {self.fullname()} and his age is {self.age} and he is eligible for examination prcessing")
    
Student1 = Student("Lawani Elyon","John",23,"M")
Student2 = Student("Gojo","Satorou",21,"M")
Student3 = Student("Hinata","Hyuga",20,"F")

Student1.student_details()

#Inheritance practice2
#Parent class
class Bird:
    def __init__(self):
        print("Bird is Ready")
    
    def whoisThis(self):
        print("Bird")
    
    def swim(self):
        print("Swim Faster")

#Child class
class penguin:
    def __init__(self):
        #call the super function
        super().__init__()
        print("The Penguin is Ready")
    def whoisThis(self):
        print("Hi im Penguin")
    def run(self):
        print("And i run faster")

peggy = penguin()
print(peggy.whoisThis())
print(peggy.run())

#Checkpoint
class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
my_point = Point3D(1,2,3)
print(my_point.x,my_point.y,my_point.z)



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    
my_rectangle = Rectangle(3,4)

print(my_rectangle.area())
print(my_rectangle.perimeter())


#3. Write a Python  class named Circle constructed by its center O and radius r. Define two methods, area and perimeter, which will compute the area and the perimeter of the circle, and is Inside() method which allows you to test whether a point A(x, y) belongs to the circle C(O, r) or not.
import math
class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def isInside(self, a, b):
        distance = math.sqrt((a - self.x) ** 2 + (b - self.y) ** 2)
        return distance <= self.r

circle = Circle(0, 0, 5)

print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
print("Is (3, 4) inside the circle?", circle.isInside(3, 4))
print("Is (6, 8) inside the circle?", circle.isInside(6, 8))

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self,amount):
        return self.balance + amount
    def withdraw(self,amount2):
        return self.balance - amount2
    
my_bank = Bank("Elyon",3000)
print(my_bank.withdraw(500))
print(my_bank.deposit(30000))