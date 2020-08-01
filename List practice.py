#list
#An empty list can be created by using []
empty_list = [] #or
empty_list = list()
#we use [] to create the list
books = ["Biology", "Maths", "Physics", "chemistry"]
print(books)

print(len(books)) #len fuction to see the numer of items in the list

print(books[2]) #index of the list
print(books[-3])#Negative indexing
print(books.index("Maths")) # To find the index of our item in the list.

print(books[0:2]) # range function

# To check the presence or absence of an item in our  list we can use 'in' function
print("Physics" in books) #we get output as a bool value(True / False)

#list modification can be done as follows:
# 1. Add an item to our list..we can use append method.
books.append("History")
print(books)

# 2. To add item at a specific location to our list ..we can use insert method.
books.insert(1, "Geography")
print(books)

# 3. To add values or new list to our existing list by using Insert method.
magazines = ["Forbes", "Frontline", "Reader's Digest"]
books.insert(0, magazines)
print(books)

# 4. we can add the items of a new list to our old list by extend method.
books.extend(magazines)
print(books)

# 5. To remove items from the list we can use remove method
books.remove("History")
print(books)

# 6. we can also use pop method to remove values/ items at the end of list
books.pop()
print(books)
# we can get the value of the popped item
popped = books.pop()
print(popped)
print(books)

# 7. we can reverse of the list using reverse method
books.reverse()
print(books)

# 8. To sort the list we can use sort method
numbers = [8, 5, 2, 9, 7, 4]
books = ["Biology", "Maths", "Physics", "Chemistry"]
         
numbers.sort() # sorts the numbers in Ascending order 
books.sort() # sorts in alphabetical order. It is case sensitive
         
print(books)
print(numbers)
print(min(numbers)) #to print minimum number from the list
print(max(numbers)) #to print maximum number from the list
print(sum(numbers)) #to print sum of numbers from the list




