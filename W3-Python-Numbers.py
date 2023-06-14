#1.1 - Python - Numbers

# There are three numeric types in Python:

# 1.     int
# 2,     float
# 3.     complex

# Variables of numeric types are created when you assign a value to them:

x = 1       #int
y = 2.8     #float
z = 1j      #complex

# To verify the type of any object in Python, use the type() function:
# Example

print(type(x))
print(type(y))
print(type(z))

# INT
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x = 1
y = 11156564666
z = -3256517

print(type(x))
print(type(y))
print(type(z))

# FLOAT 1.1
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = 1.1
y = 1.0
z = -35.39

print(type(x))
print(type(y))
print(type(z))

# FLOAT 1.2
# Float can also be scientific numbers with an "e" to indicate the power of 10

x = 35e3
y = 12E9
z = -87.1e700

print(type(x))
print(type(y))
print(type(z))

# COMPLEX 1.3
# Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y = 5j
z = -8j

print(type(x))
print(type(y))
print(type(z))

# Type conversation 1.5
# You can convert from one type to another with the int(), float(), and complex() methods:
# Example

x = 1 #int
y = 2.8 #float
z = 3j #complex

# convert from int to float
a = float(x)

# convert from float to int
b = int(y)

# convert from int to complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Note: You cannot convert complex numbers into another number type.

# Random numbers 1.6
# Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used to make random numbers:

import random
print(random.randrange(1,10))





