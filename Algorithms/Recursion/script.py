# The factorial of a number natural number n is the product of all natural numbers less than or equal to n: n*(n-1)*(n-2)*(n-3)*....*3*2*1 
# for example if n = 6 
# 6! = 6*5*4*3*2*1
# if we have a recursive function f we'd want to calculate 6! :
# 6! = f(6)
# f(6) = 6*f(5)
# f(5) = 5*f(4), so f(6) = 6*5*f(4)
# f(4) = 4*f(3), so f(6) = 6*5*4*f(3)
# f(3) = 3*f(2), so f(6) = 6*5*4*3*f(2)
# f(2) = 2*f(1), so f(6) = 6*5*4*3*2*f(1)
# f(1) = 1, so f(6) = 6*5*4*3*2*1.

def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n*recursive_factorial(n-1)
    
# Defined a function that takes input n and it will return n*recursive_factorial(n-1) 

factorial = 1
num = int(input("Enter a number"))

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
         factorial*=i
    print("The factorial of",num,"is",factorial)