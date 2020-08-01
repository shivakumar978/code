# WHILE loop:
# With the while loop we can execute a set of statements as long as a condition is true
a = 1
while a < 8:
    a += 1 # If you dont use this loop will run (printing 1) forever
    print (a)
     

# BREAK statement:
# With the break statement we can stop the loop even if the while condition is true:
a = 1
while a < 8:
    a += 1
    if a == 4:
        break
    print(a)


# CONTINUE statement:
# with this we can stop the current iteration, and continue with the next:
a = 1
while a < 8:
    a += 1
    if a == 4:
        continue
    print(a)


#ELSE statement: used to run a block of statement when the condition is false
a = 1
while a < 8:
    a += 1
    print(a)
else:
    print("Invalid condition")
    







