#============================================#
#             File Handling                  #
#============================================#
#Python has several functions for creating, reading, updating, and deleting files.
#File Handling
#The key function for working with files in Python is the open() function.
#The open() function takes two parameters; filename, and mode.
#There are four different methods (modes) for opening a file:
#    "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#    "a" - Append - Opens a file for appending, creates the file if it does not exist
#    "w" - Write - Opens a file for writing, creates the file if it does not exist
#    "x" - Create - Creates the specified file, returns an error if the file exists

#In addition you can specify if the file should be handled as binary or text mode
#    "t" - Text - Default value. Text mode
#    "b" - Binary - Binary mode (e.g. images)

#Opening A File

f = open("Demofile.txt")
#Path where the file exist also need to mention

f = open("C:\\Users\\lenovo\\Desktop\\Python_Files\\Demofile.txt")

#By Default, file will be opened as read and in text format

f = open("C:\\Users\\lenovo\\Desktop\\Python_Files\\Demofile.txt")
f = open("C:\\Users\\lenovo\\Desktop\\Python_Files\\Demofile.txt","rt")


#Both the above statement ae same and correct

#Reading the content of the file
#The open() function returns a file object, which has a read() method for reading the content of the file:

#Read Whole content of file
print(f.read())

#Reading part of file

print(f.read(5))

#This will read the first 5 characters of file
#O/P 
#Hello

#Read lines

print(f.readline())

#This will display the first line.

#To print the 2 lines we can write it twice
print(f.readline())
print(f.readline())


#Read the file line by line

for line in f:
    print(line)

for line in f:
    print(line,end ="")

#===========================================#
#               DELETE FILE                 #
#===========================================#
#
#To delete a file, you must import the OS module, and run its os.remove() function:

import os
os.remove("demofile.txt")

#To check if file Exists

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
  
#To Delete a folder

import os
os.rmdir("myfolder")




import csv
# with open('C:\\Users\\lenovo\\Desktop\\Python_Files\\Tab_Delimited.txt','rt')as f:
#     data = csv.reader(f)
#     for row in data:
#         print(row)
# data.close()

# Get the file from the location
file = open("C:\\Users\\lenovo\\Desktop\\Python_Files\\MyPlaylist.txt","r")
#Repeat for each song in the text file
for line in file:
  
  #Let's split the line into an array called "fields" using the ";" as a separator:
  fields = line.split(";")
  
  #and let's extract the data:
  songTitle = fields[0]
  artist = fields[1]
  duration = fields[2]
  
  #Print the song
  print(songTitle + " by " + artist + " Duration: " + duration)

#It is good practice to close the file at the end to free up resources   
file.close()


file = open("C:\\Users\\lenovo\\Desktop\\Python_Files\\MyPlaylist.txt","r")

#Repeat for each song in the text file
for line in file:
    fields = line.split(";")
    SongTitle = fields[0]
    Singer = fields[1]
    Duration = fields[2]
    print(SongTitle + " by " + Singer + " Duration: " + Duration)

file.close()


file_tab = open("C:\\Users\\lenovo\\Desktop\\Python_Files\\Tab_Delimited.txt","r")

for line in file_tab:
    fields = line.split("\t")
    print(line)
file_tab.close()


file_csv = open("C:\\Users\\lenovo\\Desktop\\Python_Files\\sample.csv","r")
for line in file_csv:
    fields = line.split(",")
    date = fields[0]

print(date)
# file_csv.close()


#Get the File from the Location
tab_file = open("C:\\Users\\lenovo\\Desktop\\Python_Files\\Tab_Delimited.txt","r")
for line in tab_file:
#Split the lines into array by the Separator (\t or Tab):
	fields = line.split("\t")
#print all content of the file
	print(line)
tab_file.close()


#Get the File from the Location
tab_file = open("C:\\Users\\lenovo\\Desktop\\Python_Files\\Tab_Delimited.txt","r")
for line in tab_file:
#Split the lines into array by the Separator (\t or Tab):
	fields = line.split("\t")
	column = fields[0]
#print all content of the file
print(column1)
tab_file.close()

tab_file = open("C:\\Users\\lenovo\\Desktop\\Python_Files\\Tab_Delimited.txt","r")
for line in tab_file:
    fields = line.split("\t")
    column1 = fields[0]
    print(column1)
# column01 = column1[1]
# print(column01)
tab_file.close()


tab_file = open("C:\\Users\\lenovo\\Desktop\\Python_Files\\Tab_Delimited.txt","r")
for line in tab_file:
#Split the lines into array by the Separator (\t or Tab):
	fields = line.split("\t")
	column1 = fields[0]
#print all content of the file
	print(column1)
tab_file.close()



file_csv = open("C:\\Users\\lenovo\\Desktop\\Python_Files\\sample.csv","r")
for line in file:
    fields = line.split(",")
print(line)
file_csv.close()


file_csv = open("C:\\Users\\lenovo\\Desktop\\Python_Files\\sample.csv","r")
for line in file_csv:
    fields = line.split(",")
    print(line)
print(fields[0])
file_csv.close()


import csv
filename = "C:\\Users\\lenovo\\Desktop\\Python_Files\\sample.csv"

with open(filename, 'r') as filehandle:
  for line in filehandle:
    fields = line.split(",")
    date = fields[0]
    id = fields[1]
    number = fields[2]
    color = fields[3]
    print(date)
    # print(line)
    print("============================")
    print("Date " + date + " ID " + id + " Number " + number + " Color " + color)
filehandle.close()



filename = "C:\\Users\\lenovo\\Desktop\\Python_Files\\Tab_Delimited.txt"

with open(filename,'r') as filehandle:
  for line in filehandle:
    fields = line.split('\t')
    Col1 = fields[0]
    Col2 = fields[1]
    Col3 = fields[2]
    print("Column 1: " + Col1 + " Column 2: " + Col2 + " Column 3: " + Col3)
filehandle.close()



filename = "C:\\Users\\lenovo\\Desktop\\Python_Files\\Tab_Delimited.txt"

with open(filename,'r') as filehandle:
  for line in filehandle:
    fields = line.split('\t')
    Col1 = fields[0]
    print("Column 1: " + Col1)
filehandle.close()



def square(num):
  return num**2

my_nums =[1,2,3,4,5]
for item in map(square, my_nums):
  print(item)
# item.close()


list(map(square,my_nums))

item.close()

def splicer(mystring):
  if len(mystring)%2 == 0:
    return 'EVEN'
  else:
    return mystring[0]

name=['Andy','EVE','sandy']

list(map(splicer,name))

type(name)



#To count the string length and find if it has even length or odd.

name=['Andy','Sandy','Nick','Joseph','Emillia']

#Step 1
#Creating a function that count the length of a string and return Even if even or first letter of string if not

def splicer1(mystring):
	if len(mystring)%2 == 0:
		return 'EVEN'
	else:
		return mystring[0]
		
#Step 2
#Mapping this function to each and every element of "name" List
list(map(splicer1,name))
# for item in map(splicer,name):
	# print(item)
