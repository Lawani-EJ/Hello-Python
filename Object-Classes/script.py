class Car:
    def __init__(self,make,model,color):
        self.make = make
        self.model = model
        self.color = color
        # self.owner_no = 0

    def car_info(self):
        print("Make: ",self.make)
        print("Model: ",self.model)
        print("Color: ",self.color)
        # print("Number of owners",self.owner_no)
    
    # def sell(self):
    #     self.owner_no += 1

my_car = Car("Honda","Accord","Black")

my_car.car_info()
my_car.car_info()
# my_car.sell()


#Practice2
# class definiaiton
class Student:
    def __init__(self,firstname,lastname,age,sex):
        self.firstname = firstname
        self.lastname =lastname
        self.age = age
        self.sex = sex

# Method defination
    def introduce(self):
        print(f"Hello my name is {self.firstname} {self.lastname} and i am {self.age} years old")

#Create instances
Student1 = Student("Lawani Elyon","John",23,"M")
Student2 = Student("Gojo","Satorou",21,"M")
Student3 = Student("Hinata","Hyuga",20,"F")

# Execute the method
print(Student1.introduce()) 
print(Student2.introduce())
print(Student3.introduce())

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

# Encapsulation example
class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        self. __discount = 0.10
    
    def __repr__(self):
        return f"Book({self.title}, {self.quantity}, {self.author}, {self.price})"

book1 = Book('Book 1', 12, 'Author 1', 120)

print(book1.title)
print(book1.quantity)
print(book1.author)
print(book1.price)
# print(book1.__discount)

# Example2 using getters and setters
class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price  
        self.__discount = None  

    # Setter
    def set_discount(self, discount):
        self.__discount = discount

    # Getter    
    def get_price(self):
        if self.__discount:
            return self.price * (1 - self.__discount)  
        return self.price  
    
    def __repr__(self):
        return f"Book({self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()})"
    

single_book = Book("Two States", 1, "Chetan Bhagat", 200)
bulk_book = Book("Two States", 100, "Chetan Bhagat", 200)
bulk_book.set_discount(0.10)

print(single_book.get_price())  # 200
print(bulk_book.get_price())  # 180 (after 10% discount)
print(single_book)  # Displays book details
print(bulk_book)  

class Person:
    def __init__(self):
        self.__my_name = 111999  

    def get_my_name(self):
        return self.__my_name 

    def set_my_name(self, new_name):
        self.__my_name = new_name 

person = Person()

try:
    print(person.__my_name)
except AttributeError:
    print("Cannot access private variable directly!")


person.__my_name = 999111  # This creates a new public variable, not modifying the private one
print("After direct modification attempt:", person.get_my_name()) 

# Modify the private variable using the setter method
person.set_my_name(999111)
print("After using setter:", person.get_my_name())  # Now changed to 999111

# Doctyping
def multiply_numbers(a,b):
    """
    Multiplies two numbers and returns the result.

    Args:
    a(int): The first number.
    b(int): The second number.

    Returns:
    int: The product of a and b.
    """
    return a*b
print(multiply_numbers(3,5))

# Docstrings
def my_function():
    '''
    Demonstrating triple double quotes
    docstrings and does nothing really
    '''
    return None
print("Using __doc__ gives: ")
print(my_function.__doc__)

print ("Program One:For loop Method")
numx =[3,4,5,6,7,8,9,10]
cubes = []
for x in numx:
    cubes.append(x**3)
print ("OUTPUT.",cubes) 

print ("Program Two :Map Functionality,")
numx =[3,4,5,6,7,8,9,10]
def cubes(x):
    return x**3
zz = list(map(cubes,numx))
print("OUTPUT:",zz)