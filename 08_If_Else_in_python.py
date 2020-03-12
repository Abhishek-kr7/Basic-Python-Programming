#============================================#
#             IF..THEN..ELSE                 #
#============================================#

#Python supports the usual logical conditions from mathematics:

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

#These conditions can be used in several ways, most commonly in "if statements" and loops.

#An "if statement" is written by using the if keyword.

a  = 30
b = 40

if a == b:
    print('numbers are equal')
elif a > b:
    print('a is greater than b')
else:
    print('b is greater than a')


#Short hand if
#If there is only one statement then it can be written in a single line

if a > b: print("A is greater than B")

#Short hand if..else
a = 40
b = 50

print('numbers are equals') if a == b else print('Numbers are not equal')

#Short hand if..else statement with 3 conditions
a = 30
b = 40

print('a greater than b') if a>b else print("A equals B") if a==b else print('a less than b')

#if..else with AND conditions

a = 200
b = 300
c = 400


if a > b and a>c:
   print('a is biggest of all')
elif a<b and c<b:
    print('b is the biggest of all')
elif c>a and c>b:
    print('c is biggest of all')
else:
    print('all the numbers are equal')

#if..else with OR conditions

a = 300
b = 400
c = 600

if b > a and b > c:
    print('b is the greatest number')
elif b > a or b > a:
    print('b is atleast greater than one of the 3 numbers')

#Nested if 

a = int(input('Enter a Number : \n'))
if a > 20:
   print('a is greater than 20')
   if a == 25:
       print('a is equal to 25')
   if a > 30:
       print('A is even greater than 30')
else:
    print('A is less than 20')
#
