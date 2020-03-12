#Lists are just like the arrays, declared in other languages. 
#Lists need not be homogeneous always which makes it a most powerful tool in Python. 
#A single list may contain DataTypes like Integers, Strings, as well as Objects.
#Lists are also very useful for implementing stacks and queues. Lists are mutable, 
#and hence, they can be altered even after their creation.

#List can be created using [] brackets.

#Creating a blank list

# Creation of List  
  
# Creating a List 
myList = [] 
print("Intial blank List: ") 
print(myList) 

#O/P :

#Intial blank List: 
#[]


#This is a blank List with no element
#-------------------------------------------------------
#Creating a list inside List or a multidimensional List

listList=[['ABC',123],['DEF',456]]
print(listList)

#O/P :
#[['ABC', 123], ['DEF', 456]]

#We have 2 Sublist inside a list.

#-------------------------------------------------------

#Creating a list with Duplicate Values
# (Having duplicate values) 
dupList = [1, 2, 4, 4, 3, 3, 3, 6, 5] 
print("\nList with the use of Numbers: ") 
print(dupList)  

#O/P :
#List with the use of Numbers: 
#[1, 2, 4, 4, 3, 3, 3, 6, 5]

#-------------------------------------------------------

#Creating a list with mixed elements.

myList=['ABC','DEF',123,'JKL']
print(myList)

#O/P:
#['ABC', 'DEF', 123, 'JKL']

#This list contains both string and numeric data.

#-------------------------------------------------------

#=======================================================
#Extracting Data from a list
#=======================================================

#Fetching the first element from a list.
#Indexing starts from 0 so first element will be at 0th 
#Position in the List

myList=['ABC','DEF',123,'JKL']
print(myList[0])

#O/P : 
#ABC

#Fetching the Fourth element from a list.

myList=['ABC','DEF',123,'JKL']
print(myList[3])

#---------------------------------------------------------

#Accessing element from a sublist inside List or a Multidimensional list.

listList=[['ABC',123],['DEF',456]]
print(listList[0][1])

#O/P :
#123
#The 2nd element of the first Sublist is 123

print(listList[1][0])

#O/P :
#DEF
#The First element of the 2nd Sublist is DEF.


#List Manipulation

#Converting a list into a String

myList = ['List', 'Manipulation' , 'From', 'List', 'To', 'String']
for element in myList:
print(element, end="")

#O/P :
#ListManipulationFromListToString

#end="" This will replace the , with No-Space

print(element, end=" ")

#O/P :

#List Manipulation From List To String

#Join can also be used here to make it a string

#Operations on List

nums = [12,34,56,77,89]
print(nums)

names = ['Abhishek', 'Abhay', 'Aditya', 'Biman']
print(names)

#Both the list can be kept in a single list as well

namenum = [nums,names]
print(namenum)

#List can also contain different DataTypes element

misc = [12.4, 'Abhi', 78, 'Kumar']
print(misc)

#This list contains int,float,string type of data.

#Inserting a new element in list

nums.append(45)
print(nums)

#45 will be appended in the list at last

#To add in between, we can use insert
#To insert a number at 2th index position
nums.insert(2,55)
print(nums)

#append will insert at the end and inser will insert in the middle or specific position in a List.

#To remove an element
#We can use pop for removing based on index values

nums.pop(2)
print(nums)

#It will remove the element at 2nd position.
#If no position mentioned in pop, the last element will get removed.

nums.pop()
print(nums)

#Delete from a specific position to a specific position

del nums[2:]
print(nums)

#Element from index 2 to last will be removed

#To add multiple element in the list

nums.extend([12,45.67])
print(nums)

#All the new elements will get added

#Minimum/Maximum element of a list

print(min(nums))
print(max(nums)

#Sort all the element in a list

nums.sort()
#All the elements will get sorted.

print(nums)
#Will print the sorted list now.


#To check if a secify item is there in a list or not.

a = 12 in nums
print(a)
#True if present and False if not


or we can use loop as well

if 12 in nums:
    print('yes')

#This will print yes if 12 exist else no o/p

if 12 in nums:
    print('yes')
else:
    print('No')
#Yes if Exist and No if not Exist in the list.
