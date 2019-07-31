# Functions

from math import sqrt  # Importing in-built functions from library
from random import randrange


def func(i):  # Defining the function
    print("Hello, I'm in a function!")
    print("Value passed is:", i)


func(8)  # Function call.

# Using in-built functions. eg. sqrt(). See line 3 to know how sqrt() is imported from math library.

print("Enter a value:")
n = eval(input())
print("The square root is:", sqrt(n))
print(type(sqrt(n)))

print("\nSome Pythagorean theorem now!")
print("Side 1:")
a = eval(input())
print("Side 2:")
b = eval(input())
print("\nThe hypotenuse is:", sqrt((a * a) + (b * b)))  # See how the sqrt() is called in this line

# The randrange function
print("\nThis is just a random value by computer:", randrange(1, 100))


# Assigning a value returned by function to a variable


def ret():
    print("\nReturning a value from a function...")
    print("Enter a value to return:")
    x = eval(input())
    return x


val = ret()
print("The value returned from function is:", val)


# Passing multiple parameters


def new(p, q, r):
    print("\nThe multiple parameters passed are:", p, q, r)


new(10, 20, 30)


# Default parameter


def another(i=10):  # Assigning a default argument to a function
    print("\nThe parameter is:", i)


another(8)
another()  # When no argument is passed the default argument will be used


# Passing function as an argument of another function

def add(x, y):
    return x + y


def show(f, x, y):
    return f(x, y)  # This is important.


print("\nThe sum is :", show(add, 3, 3))
