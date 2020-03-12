#============================================#
#               DICTIONARY                   #
#============================================#
#A dictionary is a collection which is unordered, changeable and indexed. 
#In Python dictionaries are written with curly brackets, and they have keys and values.
#Creating A dictionary
#Suppose we have some data and their keys

user_id = 1001
message = "Hey There! this is John"
language = "english"
datetime = "20191120T123404Z"
location = (44.59033, -104.71546)

post = {
    "user_id" : 1001,
    "message" : "Hey There! this is John",
    "language" : "english",
    "datetime" : "20191120T123404Z",
    "location" : (44.59033, -104.71546)
}

#OR

post = {
"user_id" : 1001,
"message" : "Hey There! this is John",
"language" : "english",
"datetime" : "20191120T123404Z",
"location" : (44.59033, -104.71546)
}

#OR

post = {"user_id" : 1001,"message" : "Hey There! this is John","language" : "english","datetime" : "20191120T123404Z","location" : (44.59033, -104.71546)}

#Dictionary can also be created using dict() method

post2 = dict("Name" = 'Natasha',"Team" = 'Avenger','Secret'='BlackWidow')

post2 = dict(Name = 'Natasha',Team = 'Avenger',Secret='BlackWidow')
print(post2)

#While using {} braces to create dictionary, Keys are in "" quotes, but while using dict() constructor
#Keys have no quotes.

#Adding a new data into a dictionary

#adding "user_id" and location in post2

post2["user_id"] = "NTAVG"
post2['location'] = "12345.789"

#Above two values will be added in the post2 dictionary
#Key Thing here is while using adding a new key-Value pair, we are using [] and key-value are under "" or '' quotes.

#Accessing the data from a dictionary

#Similar to adding a data, we can use [] to access the data as well
#But if we try accessing a data which is not available, then we can get error
#To avoid any error popping up, we can use loop/in/exception

print(post2['Name'])

if 'address' in post2:
    print(post2['address'])
else:
    print('Address doesn\'t exist in the dictionary')
	
#Using try/except method
try:
    print(post2['Adress'])
except KeyError:
    print("Adress doesn't exist")
	
#With this ways, rather than getting Error, we can use our own messages to display

#Another way of accessing data without getting any error is to use 'get()' method
#If data exists, it will be displayed else it will print none

print(post2.get('location','No_data'))
#No_data/None/or whatever you wish to print.

#get() method takes 2 values, 1 is the key for which you want data, 
#The 2nd is the default value which will be printed
#if no data exist for the key you wished to see
#Here location is the key which we want to see the value, and No_data is the default 
#value that will display, If nothing related to location exists.

#Accessing value for all the keys in a dictionary

for key in post2.keys():
    value = post2[key]
    print(key, "=", value)

#Dictionaries contains unordered data so you may get data in the different order than you have added.

#Another way of getting all the data is to use items() method

for key,value in post2.items():
    print(key, '=', value)


#Modifying Values of a dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#We can change the value of this dictionary as below
print(thisdict)
thisdict["year"] = 2018
print(thisdict)

{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

#Earlier the year was 1964 but now the year became 2018

#Print all the key of a dictionary

for key in thisdict:
    print(key)

#brand
#model
#year

#Print all the values of a dictionary

for value in thisdict:
    print(thisdict[value])
	
#Ford
#Mustang
#2018

#values() method can also be used to get all values of a dictionary

for value in thisdict.values():
  print(value)

#Ford
#Mustang
#2018

#To find how many key-Value pair exist in a dictionary

print(len(post2)

#To view how many available method you can use on a dictionary

print(dir(post2))

#To remove an specific item
#pop()/del can be used

post2.pop('Secret')

del post2['Name']

#del keyword can delete the entire dictionary

del post2

#To remove the last inserted item
#popitem()

post2["Secret"] = "Black Widow"
print(post2)

#To remove the entire entries from a dictionary
#clear() method can be used

post2.clear()

#copying a dictionary

post3 = post2.copy()

#dict() can also be used to copy the dictionary

post4 = dict(post2)

#Nested Dictionary

#A dictionary can also contain dictionary within
#This is called Nested Dictionary

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 
print(myfamily)
#{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}


#Existing dictionaries can be merge together to form a single nested dictionary
#Lets Create 3 dictionary

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

#Now creating a single but nested dictionary from above 3 dictionaries.

child_details = {
"child1" : child1,
"child2" : child2,
"child3" : child3
}

print(child_details)
#{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}


#Dictionary Methods
#========================================================================================
#Method	 			Description
#========================================================================================
clear()			  Removes all the elements from the dictionary
copy()			  Returns a copy of the dictionary
fromkeys()		Returns a dictionary with the specified keys and values
get()			    Returns the value of the specified key
items()			  Returns a list containing a tuple for each key value pair
keys()			  Returns a list containing the dictionary's keys
pop()			    Removes the element with the specified key
popitem()		  Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. 
				      If the key does not exist: insert the key, with the specified value
update()		  Updates the dictionary with the specified key-value pairs
values()		  Returns a list of all the values in the dictionary
#========================================================================================
