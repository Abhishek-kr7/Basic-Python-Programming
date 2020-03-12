#==============================================#
#         if __name__ == "__main__"            #
#==============================================#
#Lets create 2 .py files.
#mymath.py

def add(a,b):
    """Function that will add the 2 passed parameters"""
    return a + b

#Print the output of function when passed 2 parameters
print(add(5,4))

#mytest.py

import mymath

print(mymath.add(5,7))


#When we run the mytest.py file, the output will be 
#9
#12

#But we have executed only mytest.py
#To ovrcome this, we use 'if __name__ == "__main__" in the mymath.py file


#if __name__ == "__main__"  -- It means that run the code written below this line only when __name__ becomes the file name.
#This will happen only when we will run the file itself and not from another file after importing.

#mymath.py

def add(a,b):
    """Function that will add the 2 passed parameters"""
    return a + b
if __name__ == "__main__":
    #This line directs that the below code will be executed only when this py file will be run.
    #That is only when __name__ will become __main__
    #Print the output of function when passed 2 parameters
    print(add(5,4))


#mytest.py

import mymath
print(mymath.add(5,7))

#Now if we run the mytest.py file, the output of mymath won't be printed or we can say that, 
#codes below __name__ line won't be imported.

#Printing the value of __name__
def add(a,b):
    """Function that will add the 2 passed parameters"""
    return a + b

print(__name__)
if __name__ == "__main__":
    #This line directs that the below code will be executed only when this py file will be run.
    #That is only when __name__ will become __main__
    #Print the output of function when passed 2 parameters
    print(add(5,4))
	
#__main__
#9

#So here __name__ becomes __main__ therefore the code below executes.

#Running mytest.py where we are importing the mymath.py features.

import mymath

print(mymath.add(5,7))

#mymath
#12

#So the __name__ here is mymath which is not equal to __main__ and hence code below __name__ in mymath won't get executed.
