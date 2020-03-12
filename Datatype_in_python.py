#============================================#
#                 DATATYPES                  #
#============================================#
#Text Type:	string(str)
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview

#============================================#
#                 STRINGS                    #
#============================================#
#Text in python is termed as string
#There are 3 ways you can write String in Python
#way 1:
#Using ""  -Double Quotes
#Way 2:
#Using ''  -Single Quotes
#Way 3:
#Using """ -Triple Quotes(double)
#OR
#Using ''' -Triple Quotes(single)

#Example:

#Using "" Quotes

string1 = "This is a string in python"
print(string1)

#Using '' Quotes

string2 = 'This is a string in python'
print(string2)

#Both of the string are correct and work fine.
#But what if we have ' or " inside in the string somewhere.
#Then it will throw error

string3 = 'This isn't a proper string'
print(string3)
#This will fail because python will consider the '(Apostrophe) as the end of the String.

#To avoid this, we can use either escape character(\) or we can use "" quotes when we have single quotes inside or vice versa

#Using "" '' Single combination

string3 = "this isn't a python string"
print(string3)

#Using escape(\) sequence

string4 = 'This is a \'Book of Python\''
print(string4)

string5 = "This is a \"Book of Python\""
print(string4)

#Use \ before the quotes you want to escape/ignore

#Suppose we have multiple single and double quotes in the string.
#This is where we can use the """ -Triple Quotes or ''' triple single quotes to print it properly

multistring = """One of my favourite line from the Godfather is : 
"I'm going to make him an offer he can't refuse."
Do you know who said this?"""

#This is a string that have '/" quotes inside and also multiline

multistring1 = """One of my favourite line from the Godfather is : 
"I\'m going to make him an offer he can't refuse.\"
Do you know who said this?"""

#this String have \ char as well somewhere.
#This is how we can maniplate the String in python by using ',","",""",''',\ sequence.

#Certain operation like Character position, Slicing, Negative Indexing, Length, Strip etc can also be used on string

mystring="Aniket Singh"
print(mystring[1])
#This will return the char at position 1 i.e 'b'

mystring="Aniket Singh"
print(mystring[4:])
#This will print all the character from 4 to last

mystring="Aniket Singh"
print(mystring[0:5])
#This will print the character from 0 to 4 (5 will be excluding). (Python slicing print 0 to n-1)

#Negative Indexing
mystring="Aniket Singh"
print(mystring[-5:-2])
#kum
#Negative Indexing Starts from -1
k(-5)u(-4)m(-3)a(-2)r(-1)
#Starts from left

present='i' in mystring 
print(present)
#It will give True since alphabet 'i' is present in the string

present='v' in mystring 
print(present)
#It will return False since alphabet 'v' is present in the string

#Single or Double quotes, both will work

#Concatenation

#We can also add multiple strings using + symbol in python

constring = "Aniket" + "Singh"
print(constring)
#AniketSingh

constring = "Aniket"+" "+"Singh"
print(constring)
#Aniket Singh

constring = "Aniket" + " " + "Singh"
print(constring)
#Aniket Singh

#Spaces between + and the string is not mandatorily required.

#What if we have integer value and we need to concatenate
#In this case, we need to first convert the integer to String and then we can add the strings

firstName = "Aniket"
lastName = 'Singh'
age = 27

detail = firstName + lastName + age
#This will fail coz age is string

detail = firstName + lastName + str(age)
detail = firstName +" "+ lastName +" "+ str(age)
detail = firstName + " " + lastName + " " + str(age)

#Another way of doing this is using Format method

detail = firstName + " " + lastName + " " + format(age)

#Also we can use the format as placeholder
#We can use this to passed the value as an argument where placeholders {} are:

age = 27
Detail = "My name is Aniket and I am {}"
print(Detail.format(age))

#Multiple argument can be passed using Format method
name = "Aniket"
lastName = 'Singh'
age = 27
place = "Patna"
detail = "I am {} {} and I am {} year old from {}."
print(detail.format(name,lastName,age,place))
#Here we have passed the multile arguments in a string using format method.

#Index Number can also be used to pass the arguments in correct way if we are not sure how they have passed

name = "Aniket"
lastName = 'Singh'
age = 27
place = "Patna"
detail = "I am {1} {0} and I am {3} year old from {2}."
print(detail.format(lastName,name,place,age))
#Here we have passed the index number of each argument the way they have been used in the format operator.

#String Length
#len() operator can be used on string to get the length

mystring="Aniket Singh"
print(len(mystring))
#14

#strip() - To remove any whitespaces from the beginning or the end of the String

mystring=" Aniket Singh "
print(mystring.strip())
#Beginning and end (but not the spaces inside the string) whitespaces will get removed.

#To make the String Upper/Lower

mystring="Aniket Singh"
print(mystring.upper())
#print the string in Upper case

mystring="Aniket Singh"
print(mystring.lower())
#print the string in lower case

mystring=" Aniket Singh "
print(mystring.strip().upper())
#This will remove the whitespaces and will print the string in Upper case

#To replace a string with another String
mystring=" Aniket Singh "
print(mystring.replace("h","H"))
#h will be replace with H

mystring=" Aniket Singh "
print(mystring.replace('s','a'))
#s will be replace with a

#A String can also be splitted into multiple substrings

mystring="Aniket Singh"
print(mystring.split(" "))
#Above string splitted into 2 sub-strings 'Aniket' and 'Singh' based on the delimiter 'spaces'.

#There are several others method that can be used on string

Method	        Description
#=======================================================================================================
capitalize()	Converts the first character to upper case
casefold()	    Converts string into lower case
center()	    Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	        Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning


#============================================#
#                  NUMERIC                   #
#============================================#
#In Python 3, we have 3 different Number Datatypes
#int(Integer)
#float(Decimal)
#Complex

#Integer
#We don't have to specify explicitly whether a number is integer or float or complex,
#Python built in modules do this all stuff

value1 = 12
value2 = 10
value3 = 12.2 #Float Type
value4 = 10.0


We can check the type of it by using 'type'
type(value1)
type(value2)

#Operation on Number Datatype

#Addition

result = value1 + value2
print(result)

#Subtraction

result = value1 - value2
print(result)

#Multiplication

result = value1 * value2
print(result)

#Division 

result = value1 / value2
print(result)

#Modulus(To get the Remainder)

result = value1 % value2
print(result)

#Complex Number : Number that contains real and imaginary part.

z = 2 -6.1j
#where 2 is real and 6.1 is imaginary part
#To access the real and imaginary part we can do it as below

z.real
#2
z.imag
#6.1
