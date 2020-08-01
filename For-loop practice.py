# Loops and Iterations:

# FOR-Loop: A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc. 
sports = ["Hockey", "Football", "Basketball", "Tennis"]
for x in sports:
    print(x)
# No indexing variable is needed before  the start
# We can also loop through a string
for x in "Basketball":
    print(x)

# ------------------------------------------------------------------------------
   
# "Break statement": we can stop the loop
sports = ["Hockey", "Football", "Basketball", "Tennis"]
for x in sports:
    print(x)
    if x == "Basketball":
        break # here "Basketball is included and then break

         # or
         
sports = ["Hockey", "Football", "Basketball", "Tennis"]
for x in sports:
    if x == "Basketball":
        break
    print(x) # here "Basketball" is not included

# ----------------------------------------------------------------------------------

# "Continue statement": we can stop the current iteration of the loop, and continue with the next
sports = ["Hockey", "Football", "Basketball", "Tennis"]
for x in sports:
    if x == "Basketball":
        continue # here "Basketball" is not printed but continues from "Tennis"
    print(x)

#---------------------------------------------------------------------------
    
# Range Function: To loop through a set of code a specified number of times, we can use the range() function
# Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(8):
    print(x)
# Note that range(8) is not the values of 0 to 8, but the values 0 to 7
# It is possible to specify the starting value by adding a parameter:
for x in range(3, 8):
    print(x) # range(3, 8), which means values from 3 to 8 (but not including 8)
# It is possible to specify the increment value by adding a third parameter:
for x in range(5, 50, 5):
    print(x)

# --------------------------------------------------------------------------------

# Else in For loop:  it is used to specify a block of code to be executed when the loop is finished

sports = ["Hockey", "Football", "Basketball", "Tennis"]
for x in sports:
    print(x)
else:
    print("Finished printing")

# --------------------------------------------------------------------------------

# Nested Loops: loop with in a loop
# The "inner loop" will be executed one time for each iteration of the "outer loop":
nation = ["India", "Finland", "Lithuania", "Afghanistan"]
sports = ["Hockey", "Pesapallo", "Basketball", "Buzkashi"]
for x in nation:
    for y in sports:
        print(x,y)
