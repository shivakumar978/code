a = 9 #integer value
print(a)
print(id(a))
print(type(a))


b = 22.7 #float value
print(b)
print(id(b))
print(type(b))

#simple Arthematic operators
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(11 // 5) #floor division
print(10 ** 5) #Exponent
print(11 % 5) #Modulus(simply the remainder)

a = 2
a = a + 1
print(a)

#or

a = 2
a += 1
print(a)

#lets check some built in functions
print(abs(-45)) #abs = absolute value and it just removes the negative sign.
print(round(22.78))# rounds up to the nearest integer
print(round(22.789, 1)) #rounds upto 1 decimal points
print(round(22.789, 2))#rounds upto 2 decimal points

#lets check out some comparison operators which give us Boolean values
a = 9
b = 5

print(a == b) #Equal
print(a != b) #Not Equal
print(a > b) #greater than
print(a < b) #less than
print(a >= b) #greater than or equal to
print(a <= b)#less than or equal to

#converting strings to Integers.(also called as casting)
a = "50"
b = "70"
print(a + b)# here we get the result as 5070 which is string concatination.

print(int(a) + int(b)) #we need to use int class to convert the string into integer

