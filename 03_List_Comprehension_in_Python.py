#============================================#
#             LIST COMPREHENSION             #
#============================================#

#Similar to the list, list comprehension are 
#also the collection of data inside a []
#But in List Compression, we will have expression with 
#for loop/if statement rather than the data directly


List: [1,2,'a',32.3]

List_Comprehension : [ expr for val in collection ]
#This means that the expr with for loop will be applied on all the data in collection

#If we want to apply the loop on certain type of data in a collection of data 
#then we can have if loop in it as well after the for loop

List_Comprehension : [ expr for val in collection if <test>]

#We can have multiple if clause can also exist

[ expr for val in collection if <test> and <test2> ]

#Example:

#Creating a list of squares of each number from 1 to 100

#Using List
squares = []
for i in range(1,101):
    squares.append(i**2)
print(squares)

#Note: Exponential in python is represented as ** so 2square2 can be written as 2**2

#Using Comprehension list

squares2 = [i**2 for i in range(1,101)]
print(squares2)

#Works same as the above. But the code is of 1 line only.

#Creating a list of data from range 1 to 100 while dividing number fromm 5
#Modulus(%) will be used here

#Using List

remainder = []
for i in range(1,101):
    remainder.append(i**2 % 5)
	
print(remainder)

#Using list Comprehension

remainder1 = [i**2 % 5 for i in range(1,101)]
print(remainder1)

#Both the code will have same output.

#Fetching specific detail from the list

movies = ['Star wars','Gandhi','Shawshank','Superman','Saw','War','Zorro']

#To fetch all the movies that start with S

#will create blank list 

smovies = []

for item in movies:
    if items.startswith('S'):
	smovies.append(items)

print(smovies)

#Using List Comprehension

smovies = [items for items in movies if items.startswith('S')]

#Same Data but code became a single line

#A more complicative list When List is tuple
movies = [('Star wars',1997),('Gandhi',2001),('Shawshank',1989),('Superman',2014),('Saw',2001),('War',2019),('Zorro',2002)]
#fetching all the movies released before 2002

newmovies = []

for name,year in movies:
    if year < 2002
	newmovies.append(name)
print(newmovies)

#To print both Name, year < 2002
#make (name,year) as single value while appending in th newmovies list.

for name,year in movies:
    if year < 2002
	newmovies.append((name,year))
print(newmovies)

#Using List Comprehension

mymovies = [name,year for (name,year) in movies if year < 2002]
print(mymovies)


mymovies = [(name,year) for (name,year) in movies if year < 2002]
print(mymovies)


#Scalar Multiplication
multi = []
v = [2, -3, 1]
#To multiply each number by 4
for item in v:
    item = item * 4:
	multi.append(item)
print(item)

#Using list Comprehension

multilist = [4*item for item in v]
print(multilist)

multilist = [item * 4 for item in v]
print(multilist)

#Cartisian Product

#Suppose we have 2 sets A and B then the cartisian pair will be set of pair of each element from both set

A = {1,3}
B = {4,5}

AXB = {(1,4),(1,5),(3,4),(3,5)}

A = [1,3,5,7]
B = [2,4,6,8]

#Using List

for a in A:
    for b in B:
        listcart.append((a,b))
print(listcart)

#Using List Comprehension
cart_prod = [(a,b) for a in A for b in b]
print(cart_prod)
