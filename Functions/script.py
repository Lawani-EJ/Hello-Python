# a = 1
# def add1(b) :
#     return a+b
#     c = add1(10)

# def f(*x):
#     return sum(x)

def add(a) :
    """
    This function adds two numbers
    """
    b = a + 1
    print(a, "If you add one you get =  ", b)
    return b
add(1)

def multi(a, b) :
    """
    Multiply two numbers
    """
    c = a*b
    return(c)
    print('This is not printed')

result = multi(12,2)
print("When multiplying", 12 ,"and", 2  ,"you get the =",result,"as the result.")

def square(a):
    # Local variable
    b = 1
    c = a * a + b
    print(a, "if you sqaure", 6 ,"+ 1 you get = ",c)
    return(c)
square(6)

x = 3
y = square(x)
print(y)

def square(a):
    # local varaibles
    # varaibles that are defined inside a function
    b = 1
    c = a*a*+b
    print(a,"if you sqaure +1",c)

#Global variables
# variables that are defined outside a function
x = 3
z = square(x)
print(z)

def f():
    print("inside the function",s)

#Global variable
s = "I love studying"
f()
print("Outside function",s)

def f():
    s = "Me too!"
    print(s)

#Global variables
s = "I love studying"
f()     
print(s)

    # This function modifies the global variable 's'
def f():
    global s
    s += ' DANIEL'
    print(s)
    s = "Python is the best"
    print(s) 

# Global Scope
s = "Python is great!" 
f()
print(s)

#define a string that concantenates two strings
def con(a,b):
    return (a+b)
print(con("Hello","World"))
