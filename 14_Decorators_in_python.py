#============================================#
#               DECORATORS                   #
#============================================#
#Decorators in python is any object that takes a function as input, 
#add some functionality and then return the result.
#With the help of Decorators, we can call a function in another function

Decorators

1. Nested function
2. Function can return a function
3. Function name is a Reference
4. Function can be used as the parameters

#Function as a parameters
#A function can be called in another function as Parameter

def function1():
    """This is function that will be called in another function"""
    print("This is function 1 and will be called by function2 as parameter")


def function2(func):
    """This is the function that will call function 1 as a parameter"""
    print("This function will call the function 1")
    func()  #Calling func

# Calling function1 as parameter in function 2
function2(function1)

#Here we are not calling function1 in the function2. We are passing the function 
#as argument and using only the function as reference
#Function calling written as "function_name()" i.e function with () brackets.

#Modifying Using Decorators
#

def qAnswer():
    return "Sachin Temdulkar is a batsman"

#Now We want to write few other line before and after the output of this function
#Will create a decorator that takes a function. Add some string, run the function, add some more string and return the function.

def add_lines(func1):    We will pass function as an argument(func) here
    def execute_me_first():  #This function will be executed now
        print("Who is Sachin Tendulakar")  #This line will print before run the function passed as an argument
        func1()  #function passed as an argument will run
        print("Sachin have the Record of Highest number of Centuries") #This will be printed after completion of the above function
    return execute_me_first  #Will return the function written under add_lines

@add_lines
def qanswer():
    print("Sachin Temdulkar is a batsman")

qanswer()

#Now the output will be as below 
#Who is Sachin Tendulkar
#Sachin Tendulkar is a batsman
#Sachin have the Record of Highest number of Centuries


#Suppose we have a function which returns a greeting message.
#We want to get the result in Upper Case without changing the function
#This can be achieved by using decorators

def greet_msg():
    return"hi!, good morning"

#Since this will not print anything as it is having return key in it, to print this, either we can take a variable to store or print using print


print(greet_msg())

#Printing above msg using decorators

def strUpper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner


def greet_msg():
    return "hi!, good morning"

d = strUpper(greet_msg)
print(d())
#d here is now a reference so we will write it as "d()" while printing


in Decorators,
d = strUpper(greet_msg) will be removed by calling the strUpper function with @ Symbol as below

@strUpper


def strUpper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner


def greet_msg():
    return "hi!, good morning"

@strUpper
print(greet_msg())

#Example 2:

We have a function that takes 2 input and divide those values.
But when 0 passed for 2nd value, it will throw error
We are going to handle it with the decorators


def numDiv(a,b):
    return a/b

#When a = 4, b = 2 it works well but
#When a = 4, b = 0 it will throw error.

We will create a deocorator to handle this


def divDeco(func):
    def inner(x,y):
	    if y == 0:
		    return "Value cannot be 0"
		return func(x,y)
	return inner
#Now we will use this decorator for the numDiv function

@divDeco
def numDiv(a,b):
    return a/b
	
print(numDiv(4,0))

#Now when this function will run with b as 0, it will print "Value cannot be 0" instead of Traceback Error.


Example 3

def makeUpper(func):
    def takefunc():
        funcString = func()
        return funcString.upper()
    return takefunc


@makeUpper
def say_hi():
    return "hey there!, how are you"

print(say_hi())
