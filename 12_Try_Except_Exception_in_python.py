#============================================#
#                 EXCEPTION                  #
#============================================#
#try
#except
#finally
#else
#raise
#

#try block may or may not raise exception
#Exception can be handled by specific exception as well as we can use common exception method to print any exception
#When Handling Specific Error, We can use the name of that Error in the Except block like
#ValueError
#ZeroDivisionError etc..

#If we don't know a specific error, we can use the function 'Exception' in the Except block


try:
    statements(s)

except e1:
    statement(s)
except e2:
    statement(s)
except :
    statement(s)
else:
    statement(s)

#If any exception raised in try block, then except e1 block will run,
#If 2 except block doesn't match, then default except block will run
#If no exception in try block then else block will run

#Example for try except


print("This is test")
print(10/0)
print("Rest of the block")

#When this code will run, it will fail on the 2nd line and terminated, thus the last one won't run

#To handle this, we will use Try

try:
    n = int(input("Enter a number: "))
    print(10/n)
except ZeroDivisionError:
    print("You Have Entered Zero!, Performing division by default value 5")
    print(10/5)

print("Running rest of the Code")


#Function that takes user input to perform division

def userEntry():
    n = int(input("Enter a number:"))
    print(10/n)

try:
    userEntry()
except ZeroDivisionError:
    print("You Have Entered Zero!, Performing division by default value 5")
    userEntry()



try:
    n = int(input("Enter a number: "))
    print(10/n)
except Exception:
    print("You Have Entered Zero!, Performing division by default value 5")
    print(10/5)

print("Running rest of the Code")

#To print the the exception along with your message

try:
    n = int(input("Enter a number: "))
    print(10/n)
except Exception as e:
    print("You Have Entered Zero!, e")
    print(10/5)

print("Running rest of the Code")
#This will result in your message as well as exception message.

#While handling file or database connection where we need to open a file or connection and then close that.
#We can not write it in try or except block
#When we open/Close resource in the try block, it will run when no error occurs but 
#the close resource part will fail, as the loop will jump to except block before running the close block.
#We can also not  write the cose resource in Except block as it will run only when Error will Occur.

#Rather we have a finally function available to handle that

#Resource block in try

a = 5
b = 0

try:
    print("Resource Open")
	print(a/b)
	print("Resource Closed")
except Exception as e:
    print("Hey!, Number cannot be divided by 0!!", e)

#Resource Open
#Hey!, Number cannot be divided by 0!! division by zero


#Resource Block in try/Except

a = 5
b = 2

try:
    print("Resource Open")
	print(a/b)

except Exception as e:
    print("Hey!, Number cannot be divided by 0!!", e)
    print("Resource Closed")

#CLose block not executed as the data was correct
#Resource Open
#2.5

#finally block will execute in both the cases. Whether any Error occurs or whether there is no error
#So if we have to close any file or any connection, we can write that in the finally Block


a = 5
b = 2

try:
    print("Resource Open")
	print(a/b)

except Exception as e:
    print("Hey!, Number cannot be divided by 0!!", e)
   
finally:
    print("Resource Closed")
	
#When i/p is Correct

#Resource Open
#2.5
#Resource Closed


#When i/p is wrong

#Resource Open
#Hey!, Number cannot be divided by 0!! division by zero
#Resource Closed


a = 5
b = 2

try:
    print("Resource Open")
	print(a/b)
    c = int(input("Enter a Number :")
	print(c)

except ZeroDivisionError as e:
    print("Hey!, Number cannot be divided by 0!!", e)
except ValueError as e:
    print("The Entered input in Invalid", e)
except Exception as e:
    print("Something went Wromg!!" , e)
finally:
    print("Resource Closed")

#Resource Open
#Hey!, Number cannot be divided by 0!! division by zero
#Resource Closed
#Function that check for the availability of file and return/log error if not.


import logger
import time
logging.basicConfig(filename='C:\\Users\\lenovo\\Desktop\\Python_Files\\log.txt', level=logging.DEBUG)
logger = logging.getlogger()

def read_file_time(path):
    """Return the contents of the file and measure time required"""
	start_time = time.time()
	try:
	    f = open(path, mode ='rb')
		data = f.read()
		return data
	except FileNotFoundError as e:
	    logger.error(e)
		raise
		else:
		f.close()
		finally:
		stop_time = time.time()
		dt = stop_time - start_time
        logger.info("Time required for {file} = {time}".format(file = path,time = dt))


#Running the Code  
#When File Exist

data = read_file_time("C:\\Users\\lenovo\\Desktop\\SongsForJarvis\\chakna_chakna.mp3")
#No Error occurs and total time looged in the file log.txt

#When File doesn't Exist

data = read_file_time("C:\\Users\\lenovo\\Desktop\\SongsForJarvis\\chakna_chakna1.mp3")
#Error occurs and total time logged in the file log.txt
