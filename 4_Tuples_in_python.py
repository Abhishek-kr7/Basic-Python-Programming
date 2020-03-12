#============================================#
#                  TUPLE                     #
#============================================#
#The Tuple contains sequence of data surrounded by paranthesis - '()'
#The Different between list and tuple can be said as
#list contains sequence of data surrounded by Brackets [] 
#while tuples contains sequence of data surrounded by ().
#Apart from this the major difference between list and tuple is :
#List occupy more memory for the data while tuples occupy less memory than list for same set of data

#Example :
List_numbers = [2,34,56,77]
tuples_numbers = (2,34,56,77)

#Both the list and tuples have same set of data but while checking for the space occupied by each one,
#For this first import the sys module
#We will use the getsizeof() function from sys module to find the size of list and tuple

import sys
list = [1,2,3,'a','b','c',True,7.789]
tups = (1,2,3,'a','b','c',True,7.789)

#we have same set of data in both the list and tuples

print("#list : ", sys.getsizeof(list))
print("#tups : ", sys.getsizeof(tups))
#O/P
#list :  68
#tups :  60

#As we can see, list consume more space than tuple for the same amount of data.

#Besides this we have a main difference between list and tuple is 
#List are Mutable, which means we can modify the items in a list
#Tuples are Immutable, which means we can not change the item of tuple, once created.
#=====================================================
#        LIST                     TUPLE
#=====================================================
#      Add data                  Cannot be
#      Remove data               Changed
#      Change data              And Are Immutable
#                            Can be created quickly
#=====================================================						  
#Also list has more functions to be applied while tuples have less function to be applied on
#To check the time list and tuples will take to create, we can use timeit module as below

import timeit
 list_time = timeit.timeit(stmt="[1,2,3,4,5]", number = 100000)
 tups_time = timeit.timeit(stmt="(1,2,3,4,5)", number = 100000)

#The above command will create the list and tuple with the same element for 1 million times and will calculate the time.

print("#List_time", list_time)
print("#Tups_time", tups_time)

#List_time 0.03128049403779341
#Tups_time 0.005062959604290276

#The time taken by the tuple to create a 1 million tuple for the same set of data is less than the list

#NOTE :
#To Know how many methods a particular command like list or tuple or any other method support, we can use dir() as below

print(dir(list)
print(dir(tuple))

#To know what a particular method will do
print(help(sys.getsizeof))


#Creating Tuples with 0, 1, 2, 3, .... element

empty_tuple = ()
test1 = ("a")
test2 = ("a","b")
test3 = ("a","b","c")

#O/P
#()
#a
#('a', 'b')
#('a', 'b', 'c')

#But test1 here is not looking like a tuple, and is like a simple string
#To make it a tuple, we need to add "," after the element

empty_tuple = ()
test1 = ("a",)
test2 = ("a","b")
test3 = ("a","b","c")

#Now the test1 with 1 element is also a tuple
()
('a',)
('a', 'b')
('a', 'b', 'c')

#Another way of creating a tuple
#Creating without the paranthesis

test1 = "a",
test2 = "a","b"
test3 = "a","b","c"

#This is a one way we can alos create tuples

#Tuple assignment 

survey = (27,"Delhi","Business")

age = survey[0]
place = survey[1]
job = survey[2]

print(age,place,job)

survey2 = (27,"Mumbai","Service")

age,place,job = survey2

print(age)
print(place)
print(job)

#Tuple assignment need a trailing comma(',') to assign it as tuple, 
#that is the reason we need a comma, when we hava tuple with 1 element

#Certain methods that we used in list can also be used in tuples as well

#length of tuple
print(len(test3))

#Concatenate

test4 = test2 + test3
print(test4)

#To print a tuple multiple time

print(test2 * 2)

#finding an element in a tuple

'a' in test2
#Print True if exist and False if not exist

#Converting a List into a Tuple

List1 = [1,2,3,4,5]
tuple1 = tuple(List1)
print(tuple1)    
#Now the tuple1 will have the data of List1
