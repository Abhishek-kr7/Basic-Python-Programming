#=========================================#
#            LOOPS IN PYTHON              #
#=========================================#
Python has two primitive loop commands:

#while loops
#for loops
#=========================================#
#            FOR LOOP PYTHON              #
#=========================================#
#For Loop in Python
#A for loop is used for iterating over a sequence 
#(that is either a list, a tuple, a dictionary, a set, or a string).
#For loop can be used on list or tuple or Dictionary
#Using list or tuple or dictionary
#List
x = [1,34,45.78,'Abhishek']
for item in x:
	print(item)

#Tuple
x = (1,34,45.78,'Abhishek')
for item in x:
	print(item)

#set
x = {1,34,45.78,'Abhishek'}
for item in x:
	print(item)

#Accessing Dictionary items using for loop
#there is little difference while accessing dictionary data
#if we try to access like we did using list, it won't give the data we want
mydict = {
"Name" : "Natasha",
"Team" : "Avenger",
"City" : "Manhattan"
}

for item in mydict:
    print(item)
	
#Name
#Team
#City

This will only return keys and not values.

#To get the key-value we can use items() as below

for item in mydict.items():
    print(item)

#To get values only, we can use value()

for value in mydict:
    print(mydict[value])

#Using Range in For Loop

#Accessing items from list of list

list1 = [["Hindi",5],["English",2],['Math',7],["Physics", 3]]

for item in list1:
    print(item)
#This will print each sublist as a single item.
#['Hindi', 5]
#['English', 2]
#['Math', 7]
#['Physics', 3]

#To access the items of sublist , we can do as below

for item, count in list1:
    print('Book is', item ,'and total number is ', count)
#O/P
#Book is Hindi and total number is  5
#Book is English and total number is  2
#Book is Math and total number is  7
#Book is Physics and total number is  3


#Similarly for tuples as well it will work like list

tuple1 = (("Hindi",5),("English",2),('Math',7),("Physics", 3))
for item in tuple1:
    print(item)

#('Hindi', 5)
#('English', 2)
#('Math', 7)
#('Physics', 3)

tuple1 = (("Hindi",5),("English",2),('Math',7),("Physics", 3))
for item,count in tuple1:
    print(item,count)

#Hindi 5
#English 2
#Math 7
#Physics 3

#Example : get all the values from a list which is numeric and greater than 6

list2 = ['Stark', 7, 'Manhattan',3, 49, 'Eighty Seven']
for item in list2:
    if item.isnumeric() and item >6:
        print(item) 
#Above code will return error. coz isnumeric() can be applied on string. so we will convert the each item as string
#To overcome use str function to convert the item into string and then apply isnumeric() 
for item in list2:
    if str(item).isnumeric() and item >6:
        print(item) 

#7
#49

for i in range(10):
	print(i)
#This will print the number starting from 0 to 9

for i in range(1,10):
	print(i)
#It will print the number starting from 1 till 9

#Specifying Specific Interval
for i in range(1,21,2):
	print(i)
#It will skip the 2nd number after each number
#1,3,5,7 etc

#To print even/Odd Number using For Loop
#We can either use Mod function or Range function for this

#Even Number
for i in range(0,20,2):
	print(i)
#This will print even number but will include 0 in it
 
for i in range(2,21,2):
	print(i)
#This will print even number from 0,20

#Odd Number
for i in range(1,20,2):
	print(i)
#This will print odd number from 1 to 20

#Using Mod(%) Function
#If number%2 == 0 then it will be Even else Odd

for i in range(1,21):
	if i%2==0:
		print(i)
#This will print only Even Number from 1 to 20

for i in range(1,21):
    if i%2 != 0:
	    print(i)
#This will print odd number from 1 to 20



#======================================================#
#                  WHILE LOOP                          #
#======================================================#

#While loop is like a counter. It will perform a task n number till its count matches to a values
#Since It act as a counter, we need to initialize the counter value when we use While Loop
#Note : - while True OR while 1, Both of the statement is same.
#To Print a list string 5 Times
i=1
LIST=["Hi","Hello"]
#To print this list using While, we will initialize a counter at the top
#i = 1

while i<=5:
	print(LIST)
#But this will run as infinite loop.
#To stop this we will keep incrementing value after each print of LIST
    i=i+1
#Or i+=1 it will also work

i=1
LIST=["Hi","Hello"]
while i<=5:
    print(LIST)
	i=i+1
#Summary of above explanation

#What if we want to print the iteration number with the string or list or whatever

i=1
while i<=5:
    print("Abhishek",i)
    i=i+1
#This will print the string "Abhishek" with its Iteration
#Abhishek 1
#Abhishek 2
#Abhishek 3
#Abhishek 4
#Abhishek 5

#We can also print this in Reverse order as well

i=5
while i>=1:
    print("Abhishek",i)
    i=i-1
#It will print as below
#Abhishek 5
#Abhishek 4
#Abhishek 3
#Abhishek 2
#Abhishek 1

#While inside a while loop
#Suppose we want to print below pattern 4 times
#Abhishek Kumar Kumar Kumar Kumar

i = 1
j = 1
while i<5:
    print("Abhishek ")
    while j<5:
        print("Kumar ")
        j = j+1
    i = i + 1
    print()
#But this will print Abhishek in 1 line and then Kumar in next 4 line
#To print it in a single line we will use end="" while printing the String

i = 1
j = 1
while i<=5:
    print("Abhishek ",end="")
    while j<=5:
        print("Kumar ",end"")
        j = j+1
    i = i + 1
    print()
#But this will also print only the first line correct
#Abhishek Kumar Kumar Kumar Kumar 
#Abhishek 
#Abhishek 
#Abhishek 

#To print the Correct way, we need to initialize j within the first while loop

i = 1
while i<5:
    print("Abhishek",end="")
    j = 1
    while j<=5:
        print("Kumar",end"")
        j = j+1
    i = i + 1
    print()
#Now the pattern will be correct

#Abhishek Kumar Kumar Kumar Kumar 
#Abhishek Kumar Kumar Kumar Kumar 
#Abhishek Kumar Kumar Kumar Kumar 
#Abhishek Kumar Kumar Kumar Kumar 
#Abhishek Kumar Kumar Kumar Kumar
#print() will go to the next line after each completion of inside and outside both while loop

#============================================#
#          BREAK/CONTINUE/PASS               #
#============================================#
#BREAK - Used to exit or break a loop/iteration after matching a certain condition.

i = 0
while True:
    print(i)
	i = i+1
#This type of loop will be an infinite loop
#If we want to break this loop after reaching a certain number, we can introduce break

i = 0
while True:
    if i==14:
        break
    print(i)
    i = i+1
#This was an infinite loop but when i reaches 14, the loop will break.

#Using For Loop
for i in range(1,20):
    if i == 11:
        break
    print(i)
#The loop will break if i becomes equal to 11.

#We have a vending machine which has some limited stock of candies
#We need to break if stock exceed
#Continue if Stock is available

#Take the input from the user 

available = 5
x = int(input("Enter the number of candies you want"))

i = 1
while i <=x:
    if i>available:
        break
        print("Out of Stock")
    print("Candy",i)
    i=i+1
print("bye")

#As soon as it will reach the max available limit, it will exit the while loop.
#Since available is 5 only, It will print candy 5 times and will exit the while loop.

#CONTINUE
#It will continue the operation if certain condition matches

for i in range(1,20):
    if i%3==0:
        continue
    print(i)
#This will print all the number except those which are divisible by 3 between 1 to 19

#PASS
#This is Handy in condition where we wnat to ignore or just pass a loop

for i in range(1,25):
    if i%2!=0:
        pass
    else:
        print(i)
#This will pass all the number which are not divisible by 2

#============================================#
#                 CONTINUE                   #
#============================================#

#This will make the loop continue untill it matches a certain condition.

while 1:
    inp = int(input("Enter a Number\n"))
    if inp > 50:
        print("Congrats!! You have a number greater than 50\n")
        break
    else:
        continue
#The loop will continue if number less than or equals 50 but it will break when
#Number entered greater than 50


#============================================#
#                    PASS                    #
#============================================#
#There are cases when we need to pass certain part of the loop
#Pass exactly used for this purpose.
