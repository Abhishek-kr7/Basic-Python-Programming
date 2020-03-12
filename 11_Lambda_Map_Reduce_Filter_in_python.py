#============================================#
#       Lambda/Map/Filter/Reduce             #
#============================================#

#============================================#
#                   Lambda                   #
#============================================#
#Lambda Functions are also known as anonymous function
#def keyword used to create the function while 
#lambda keyword used to create anonymous or lambda function

#Syntax
lambda argument(s): expression

#The lambda function can have any number of arguments but it will allways return one expression.

#To add 10 in a number passed in as an argument

x = lambda a: a + 10

print(x(5))

ab = lambda a,b : a * b

print(ab(5,6))

abc = lambda a,b,c : a + b + c
print(abc(12,12,24))

#In programs where sometime we don't have to create function from certain task, 
#we use lambda that act as a runtime function.

#======================================================================================================

#============================================#
#                     Map                    #
#============================================#

#The map() function executes a specified function for each item in a iterable. 
#The item is sent to the function as a parameter.

map(function, iterables)

#We have a list

FruitList = ["Apple",'Apricot',"Banana",'Guava']

#To calculate the length we can apply loop as well

for fruit in FruitList:
    print(len(fruit)
#OR

#we can create a function that will calculate the len

def fruitlen(fruit):
    return len(fruit)
	
#OR
 
#We can use map to apply this function on each element in the list

#With the help of map function, rather than writing multiple lines of code, 
#we can do it in a single line

fruitLen = map(fruitlen,FruitList)
print(fruitlen)

flen = map(fruitLen, FruitList)
print(flen)
#O/P
#<map object at 0x021601B0>

#Note : When you appliy map function on a list or iterables, we get a map object in return and not the result output.
#This is highly efficient when dealing with the larger datasets where data could be in millinons.
#We can convert into these map anytime in list or tuple to view the data.


#we will convert the map object flen into list

FrLen = list(flen)
#[5, 7, 6, 5]

#Example 2

def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)

#map() function required a function, so it is widely used with lambda function

#Squaring the element of a tuple

numbers = (1,2,3,4,5)

result = map(lambda x : x**2,numbers)
print(result)

#Note : This will not result the output. Infact it will return map object
#To print the result, convert the map object into the list

print(list(result))

#Multiply each of the number by 2
A = [1,2,3,4]
results = map(lambda x: x*2, A)
print(results)
print(list(results))

#Map/labda with loop

A = [1,2,3,4]
# results = list()
results = []
for x in A:
    results.append((lambda x:x**2)(x))
print(results)

#A list of elements can be directly pass inside a map as it takes multiple iterable
result1 = map(lambda x : x+ 5,(1,2,3))
print(result1)
print(list(result1))

#You need to convert the mapped object to view the result


#filter() in python
#The filter() method filters the given sequence with the help of a function that tests 
#each element in the sequence to be true or not.

#filter(function, sequence)
#Parameters:
#function: function that tests if each element of a 
#sequence true or not.
#sequence: sequence which needs to be filtered, it can 
#be sets, lists, tuples, or containers of any iterators.
#Returns:
#returns an iterator that is already filtered.

#We have a function that checks whether a list or tuples contain any of the available 
#alphabet which is there in the function
def alpha(alpha):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (alpha in letters):
        return True
    else:
        return False

sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

#To filter out all the element from sequence 

filtered = filter(alpha,sequence)

print(list(filtered))

#Filters are more often used with lambda function
#To filter all the number which is greater than 4

seq = [0, 1, 2, 3, 5, 8, 13]

result = filter(lambda x: x > 4 , seq)
print(list(result))

# result contains odd numbers of the list 
result = filter(lambda x: x % 2, seq) 
print(list(result)) 
  
# result contains even numbers of the list 
result = filter(lambda x: x % 2 == 0, seq) 
print(list(result)) 

#======================================================================================================

#============================================#
#                   Reduce                   #
#============================================#

#The reduce(fun,seq) function is used to apply a particular function passed
#in its argument to all of the list elements mentioned in the sequence passed along.
#We need to import functools as it is defined in that module

import functools

List = [1,2,3,4,5]
#To sum all the element of the list

#One way is to use sum() method here

List = [1,2,3,4,5]

print(sum(List))


#Another method we have is to use reduce() function.
adds = functools.reduce(lambda a,b : a + b, List)
print(adds)


#How reduce works:
#In a List if we want to add all numbers, the first 2 numbers will get added first. 
#Then the resultant value will be added with the 3rd numbers
#List = [1,2,3,4,5] adding all element

#First
#1 + 2
#This will result in 3
#Now this 3 will be added to the next element i.e 3
#3+3 = 6 
#Now 6 will be added to next available number i.e 4
#6 + 4 = 10 
#Now 10 will be added to the next available number i.e 5
#10 + 5 = 15 
#And the total sum is 15

#Finding a biggest element from a tuple

Tuple1 = (15,27,23.5,67,99)

big1 = functools.reduce(lambda a,b: a if a>b else b, Tuple1)
print(big1)

#reduce() can also be combined with operator functions like add,mul etc
#To use operator first import operator

import operator

myList = [1,3,5,8,10]
#To add all the number of list
print(functools.reduce(operator.add,myList))
#To Multiply all the Numbers of list
print(functools.reduce(operator.mul,myList))
#To Concatenate all the word of a list
wordList = ['Python','For','Beginners']
#To concatenate all the words
print(functools.reduce(operator.add,wordList))

#accumulate() function is also available for summation purpose
#But there is a difference in both of these functions

#reduce() is defined in “functools” module, accumulate() in “itertools” module.
#reduce() stores the intermediate result and only returns the final summation value. 
#Whereas, accumulate() returns a list containing the intermediate results. 
#The last number of the list returned is summation value of the list.
#reduce(fun,seq) takes function as 1st and sequence as 2nd argument. 
#In contrast accumulate(seq,fun) takes sequence as 1st argument and function as 2nd argument.


import itertools 
import functools
lis = [ 1, 3, 4, 10, 4 ]

# priting summation using accumulate() 
print ("The summation of list using accumulate is :",end="") 
print (list(itertools.accumulate(lis,lambda x,y : x+y))) 
  
# priting summation using reduce() 
print ("The summation of list using reduce is :",end="") 
print (functools.reduce(lambda x,y:x+y,lis)) 

#The summation of list using accumulate is :[1, 4, 8, 18, 22]
#The summation of list using reduce is :22
