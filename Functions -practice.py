# Functions: A function is a block of code which only runs when it is called
# In Python a function is defined using the def keyword
# You can pass data, known as parameters, into a function.
# A function can return data as a result
def my_function():
    pass
print(my_function) # The function not exwcuted. It only gives us the location of the fiunction

# In order to execute it we need give ()
print(my_function()) # The output has NONE as return value since function has no vale yet

# --------------------------------------

def my_function():
    print("Hello Shiva")

my_function()

# The benefit of functions is, it allows us to reuse our code with repeating ourselves
def my_function():
    print("Hello *Shiva")

my_function()
my_function()
my_function() # just to print our function multiple times

# I see any error(*) in the string, so we can correct it only once and run it instead of correcting it multiple times

def my_function():
    print("Hello Shiva") # I have corrected it here

my_function()
my_function()
my_function()

# This is called as keep your code 'dry'(dont repeat yourself).

#---------------------------------------------------------------

# Arguments: Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.
def my_func(name): # function with one argument
    print(name + "Kumar")
my_func("Shiva")
my_func("Satish")

#---------------------------------------------------------------------

# Parameter and Argument almost mean the same:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# A Function must be called with correct number of arguments:
# example for 2 arguments inside the function:
def my_func(name, last_name): 
    print(name + " " + last_name)
my_func("Shiva", "Kumar") # if we call more or less arguments then we will get an error

# If you do not know how many arguments that will be passed into your function
# simply add a * before the parameter name in the function definition:
# Example:
def my_function(*brothers):
    print("My brother is " + brothers[2])
my_function("Satish", "Suresh", "Ramesh")

# -----------------------------------------------------------------------

# Default Parameter Values:
def my_func(fruit = "Mango"):
    print("I Like "+ fruit)
my_func("Apple")
my_func("Banana")
my_func() # If we call the function without arguments, it uses the default value
my_func("Grapes")

# ------------------------------------------------------------------------

# Passing a list to the Argument:
def my_function(vegetables):
    for x in vegetables:
        print(x)
vegetables = ["Carrot", "Potato", "Brinjal"]
fruits = ["Mango", "Banana", "Apple"]
my_function(fruits) # only the list you call with in the function is taken into account

#------------------------------------------------------------------

# Return: it is used to by the function to return a value:
def my_func(x):
    return 3 * x
print(my_func(9))
print(my_func(5))

#-------------------------------------------

# pass: If the function is empty then use the pass statement to avoid errors

# *args= arguments
# **kwargs = keyword arguments
# example:
def staff_info(*args, **kwargs):
    print(args)
    print(kwargs)

staff_info("Technical", "Non-Teachnical", name= "Shiva", salary= "5k")

# for the above example we can unpack the list by using *for args
# and to unpack dict we can use **kwargs

def staff_info(*args, **kwargs):
    print(args)
    print(kwargs)
jobs = ["Technical", "Non-Technical"]
info = {'name': "Shiva", 'salary': "5k"}

staff_info(jobs, info) # here the list and dict are not unpacked
staff_info(*jobs, **info) # here  we can see them unpacked.









