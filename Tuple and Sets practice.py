#Tuples:
#Tuples cannot be modified because they are immutable
#Tuples are represented by using ()
tuple_1 = ("Biology", "Chemistry", "Physics", "Maths")
#Empty Tuple can be created by using ()
empty_tuple = () #or
empty_tuple = tuple()

#Sets:
#Set is represented by using {}
#Emptry set is "NOT" created using {}...instead a "dict" is created
#so to create an empty set we need to use  function
empty_set = set()
#Sets prints the output in differnt oder. The position of items in the set keeps changing
set_1 = {"Biology", "Chemistry", "Physics", "Maths"}
#It is used to see if an value is a part of set or not
#It is also used remove duplicate values..because sets dont allow duplicates.
#For example:
set_2 = {"Biology", "Chemistry", "Physics", "Maths", "Biology"}
print(set_2) # Here "Biology is printed only once ....because no duplicates.

#It is used to see if a value is a part of a Set. This is called as "Membership Test"
#Sets are used to see what values they share with other sets.

# 1. Intersection method is used to see the common items in 2 sets.

science_books = {"Biology", "Basic Maths", "Physics", "Basic computers", "Chemistry"}
arts_books = {"Accounts", "Economics", "Basic computers", "Design", "Basic Maths"}
print(science_books.intersection(arts_books))

# 2. Difference method is used to see exslusive items differing from one set to another set
print(science_books.difference(arts_books))

# 3. Union method to see combined courses present in both the sets.
print(science_books.union(arts_books))






