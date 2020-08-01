# File Objects:
# To get a file object we can use built-in "open" command
f = open("if.py")
# To opem files from different directories we need to give the path
# If we need to specify why we open this file:
# Or else the file opens by default

f = open("if.py", 'r') # for reading a file
# f = open("if.py", 'w') # for writing a file
# f = open("if.py", 'a') # for appending a file
# f = open("if.py", 'r+') # for reading and writing

# by passing f = open("if.py", 'r'), the file id open:
# To print the name of the file :
print(f.name)

f.close() # to close the file that was opened.

# To print the mode of the file we can use:
f = open("if.py", 'r')
print(f.mode) # mode here = reading or writing or etc...
f.close()

# -------------------------------------

# In the above method  we need to close the files that were opened explicitly
# There we can use context manager to over come this:
with open("palindrome.py", 'r') as f:
    f_contents = f.read
    print(f_contents)







