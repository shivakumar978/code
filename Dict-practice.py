#Dictionaries:
# Dict allow us to work with key:value pairs.
# In other programming language they are called as Hashmaps or associates of arrays
# Key: is an unique identifier, where we can find our data and value : is that data
# Examples:
staff = {"Name": "Mary", "Age": "27", "Designation": ["Teacher", "Doctor"]}
print(staff)

# If we need to get the value of one key:
print(staff["Age"])
print(staff["Designation"])

# Value can be of any data types: Mary = string, 27 = Integer, Designation = List
# keys can be any immutable data types.

# If we try to access a key that does not exist:
# For example try: print(staff["Salary"]) # we will get a KeyError
# Here we can avoid the display of KeyError when we access unexsisting Key by 'get' method
# Example:
print(staff.get("Salary"))
# we can also specify a default value for keys that dont exist:
print(staff.get("Salary", "Not Found"))


# New entries to our dicttionaries can be made by:
staff["Height"] = "5-feet 6-inches"
print(staff["Height"])


# We can update the value of the existing key:
staff["Name"] = "Mary Jane"
print(staff)
# we can also use "update" method to update the value
staff.update({"Age": "30"})
print(staff)

# We can delete a specific key and its value:
del staff["Height"]
print(staff)

# 'len' (length) fucntion is used to find the length of the key
print(len(staff))
# To see all the keys
print(staff.keys())
# To see all the values
print(staff.values())
# To see both Keys and values
print(staff.items())

# We can also loop through keys and values in our dict:
# If we loop through our list without using any method, then it will just loop through the keys 
for key in staff:
    print(key)
# In order to loop through keys and values, we need to use that item method:
for key, value in staff.items():
    print(key, value)

