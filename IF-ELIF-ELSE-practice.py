# Conditional Statements:

# IF:
# it only works / prints if the condition is True
# example:
country = "India"
if country == "India":
    print("I am an Indian")

# ELIF:
# it is preceeded with IF statement. When the IF condition is false the it comes into play:
hair_colour = "Blond"
if hair_colour == "Black":
    print("you have Black hair")
elif hair_colour == "Blond":
    print("You have Blond hair")


# ELSE:
# it only works when the IF condition is false:
hair_colour = "Red"
if hair_colour == "Black":
    print("you have Black hair")
elif hair_colour == "Blond":
    print("You have Blond hair")
else:
    print("you have other hair colour")

# Switch case statement: Its a way to check multiple values in other programming language.
# Python has no "switch case statement": because IF,ElIF and ELSE are enough to it.

# Lets us now see the Boolean operations: And, OR, & Not.
# AND: both the statements must be True
game = "Football"
watching_live = True

if game == "Football" and watching_live:
    print("Watching the match")
else:
    print("No match today")

# above if any statement was not correct("game" or "watching_live") then:
game = "Football"
watching_live = False

if game == "Football" and watching_live:
    print("Watching the match")
else:
    print("No match today")

# OR: either one of the statements can be True:
game = "Football"
watching_live = True

if game == "Football" or watching_live:
    print("Watching the match")
else:
    print("No match today")

          # or
game = "Football"
watching_live = False

if game == "Football" or watching_live:
    print("Watching the match")
else:
    print("No match today")
# in both cases either one statement is correct so we get "Watching the match"


# NOT: is used to switch a boolean. This means it will change a True to a False and a False to a True.
game = "Football"
watching_live = True

if not watching_live: # here Not has converted the True to a False, therefore we get "No match today"
    print("Watching the match")
else:
    print("No match today")

         #or

game = "Football"
watching_live = False 

if not watching_live: # here Not has converted the False to a True
    print("Watching the match")
else:
    print("No match today")
