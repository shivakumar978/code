a = "Hello World"
print(a)
b = """today the world
looks so clean and fresh"""
print(b)
print(len(a))
#length of the string
print(a[1])
#index with in the string
print(a[0:5])
#range with in the string
print(a.lower())
print(a.upper())
print(a.count('Hello'))
print(a.count('o'))
print(a.count('l'))
print(a.find('Hello'))
print(a.find('shiva'))
#when a character is not present in our string we get a value of -1 as output.
new_a = a.replace('World', 'Python')
print(new_a)

text = "Good Morning"
name = "Shiva"
wishes = text + ' ' + name
# simple string concatination 
print(wishes)

wishes = text + ' ' + name + ', ' + "Have a Nice day!"
print(wishes)

wishes = f"{text}, {name}, have a nice day!"
#formated string where I have used {} for each of variable I have defined.
print(wishes)

#with formated string I can alter/change,  each of the variable defined earlier. For example
wishes = f"{text.upper}, {name.upper}, have a nice day!"
print(wishes)
#in the above case we can also see where the changes in the id location are made.



