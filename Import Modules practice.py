# Modules: A file containing a set of functions you want to include in your application
# module is created by saving the file of code with .py extension
# example:
# def wishes(name):
    #print("Good Morning" + name)

# Now I can use mymodule(above wtitten file seperatly) by using import statement:
import mymodule

mymodule.wishes("Shiva")

# Variables inside a module: I have a code saved to mymodule.py file

import mymodule
a = mymodule.employee_1["Country"]
print(a)


# We can re-name our module by using "as" keyword:
import mymodule as em

a = em.employee_1["Age"]
print(a)

# Python has several in-built modules which we can import:
# Example:
import platform

y = platform.system()
print(y)

#Example:
import sys
print(sys.path)

# Example:
import random
fruits = ["Apple", "Mango", "Banana"]
x = random.choice(fruits)
print(x)

#Example:
import os
print(os.getcwd())

# To know the location of the in-built module:
import os
print(os.__file__)


# Example:
# lets get some maths parts now:
import math
rads = math.radians(90)
print(rads)
print(math.sin(rads))

# Example
# Dates and Time:
import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2016))

# dir() function is used to list all function names or variables inside a module:
# example:
import mymodule

b = dir(mymodule)
print(b)

# or

import platform

c = dir(platform)
print(c)

# We can use "from" to import any part from module:
# example:
from mymodule import employee_1
print(employee_1["Country"])





