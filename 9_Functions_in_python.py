def hello():
    """This function will print the Hello Message when called"""
    print('Hey there! Hello')

# hello()

def hello_user(user):
    '''This function will take a parameter or name and will print hello with
    the parameter/name'''
    print("Hello",user, "How are you")

hello_user('abhi')

print(help(hello_user))


def mycountry(country='India'):
    """This function will print the country name which has been passed as parameter
	If Nothing passed, then default value as 'India' will be Printed"""
    print('My country is :' ,country)

mycountry('America')
mycountry()

def myfood(food):
    """This function will take list as input will print all the items"""
    for item in food:
        print('You can have ' + item)

fruits = ['Apple','Banana','Cherry']
myfruits = tuple(fruits)
print(myfruits)

myfood(myfruits)


def multipliers(x):
    return x**5

print(multipliers(5))



import math

def sphereVol(r):
    """This function will take a parameter as r and calculate Volume of Sphere with that r value"""
    return 4/3 * math.pi * r**3

# print(sphereVol(3))

# print(help(sphereVol))


def tri_area(b,h):
    """This Function will take 2 parameter as base and height and will return the area of triangle"""
    return 0.5 * b * h

# print(tri_area(3,5))


def centi(feet=0, inch=0):
    """This function will take feet/inch or both
	1 feet = 12 inches
	1 inch = 2.54 cm
	and will convert into centimeter
	This function parameter have 0 as default value assigned"""

    feet_to_cm = feet * 12 * 2.54
    inch_to_cm = inch * 2.54
    return feet_to_cm + inch_to_cm

print(centi(5))
print(centi(feet = 5))
print(centi(inch = 10))
print(centi(inch = 10, feet = 5))

def g(y, x = 0,):
    print(x + y)

print(g(4,5))

print(g(x = 5))
