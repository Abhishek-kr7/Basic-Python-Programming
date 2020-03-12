#============================================#
#                 DATETIME                   #
#============================================#
#Python gives you three classes for working with dates and times: 
#the date, time and datetime classes.  All three classes are found in the datetime module.
#import the datetime module

import datetime
#Creating a variable with specific date 1956-01-31
gvr = datetime.date(1956,1,31)

print(type(gvr))
#<class 'datetime.date'>

#Now we can access the day,month,year from the gvr

print(gvr.year)
print(gvr.month)
print(gvr.day)

#1956
#1
#31

#Subtracting or adding dates

#timedelta will be used to add/subtract dates

#Suppose initial date is '2018-04-23'
#To know what will be the date when 100 days added in it.

initial_date = datetime.date(2018,4,23)
#now create an object with the timedelta for 100 days

add_date = datetime.timedelta(100)

print(initial_date + add_date)

#2018-08-01  will be the date after adding 100 days in 2018-4-23

print(initial_date - add_date)
#2018-01-13  will be the date after subtracting 100 days from 2018-4-23

#Note : Default date format in python is yyyy-mm-dd (1956-01-31)

#1956-01-31 to print this as day-name, Month-Name, Day, year

print(gvr.strftime(%A, %B, %d, %Y))

#Tuesday, January, 31, 1956

#Printing a date in a variable
#Date should be inside {} while print with the string and then use format method to print it

NEWDATE = "GVR was born on {:%A, %B %d, %Y}."
print(NEWDATE.format(gvr))

#GVR was born on Tuesday, January 31, 1956.


#Independence day
#15-08-1947

inddate = datetime.date(1947,8,15)
print(inddate)

ind_date = datetime.date(1947,8,15)
ind_time = datetime.time(22,15,0)
ind_datetime = datetime.datetime(1947,8,15,22,15,0)
print(ind_date)
print(ind_time)
print(ind_datetime)

#Now we have combined the date and time of independence day in a single object(ind_datetime)
#From this Single object we can call each value 
#Printing the datetime content one by one.
print(ind_datetime.day)
print(ind_datetime.year)
print(ind_datetime.month)
print(ind_datetime.hour)
print(ind_datetime.minute)
print(ind_datetime.second)

#Accessing current datetime

now = datetime.datetime.now()

#2019-11-27 12:13:51.654130

#Using various directive
print(now.strftime("%A"))
print(now.strftime("%a"))
print(now.strftime("%H"))
print(now.strftime("%y"))
print(now.strftime("%p"))

#Wednesday
#Wed
#12
#19
#PM

#Formatting Date time with strptime
#Converting a string into Date format

moon_landing = "7/20/1969"
moon_date = datetime.datetime.strptime(moon_landing, "%Y/%m/%d")
print(moon_date)
print(type(moon_date))

#1969-07-20 00:00:00
#<class 'datetime.datetime'>
#Note that the date is not a string anymore and has converted into a date object

#===========================================================================================
#Directive			Description													Example	
#===========================================================================================
%a				Weekday, short version											Wed	
%A				Weekday, full version											Wednesday	
%w				Weekday as a number 0-6, 0 is Sunday							3	
%d				Day of month 01-31												31	
%b				Month name, short version										Dec	
%B				Month name, full version										December	
%m				Month as a number 01-12											12	
%y				Year, short version, without century							18	
%Y				Year, full version												2018	
%H				Hour 00-23														17	
%I				Hour 00-12														05	
%p				AM/PM															PM	
%M				Minute 00-59													41	
%S				Second 00-59													08	
%f				Microsecond 000000-999999										548513	
%z				UTC offset														+0100	
%Z				Timezone														CST	
%j				Day number of year 001-366										365	
%U				Week number of year, Sunday as the first day of week, 00-53		52	
%W				Week number of year, Monday as the first day of week, 00-53		52	
%c				Local version of date and time									Mon Dec 31 17:41:00 2018	
%x				Local version of date											12/31/18	
%X				Local version of time											17:41:00	
%%				A % character													%
#===========================================================================================
