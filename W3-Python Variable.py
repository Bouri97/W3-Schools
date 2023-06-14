#1.1 - Intro - Python Creating a variable
                #1.  Python has no command for declaring a variable.
                #2.  A variable is created the moment you first assign a value to it.

# Legal example 'creating variable'
x = 5
y = "John"
print("x")
print("y")

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4           # x of type is 'int'
y = "Sally"     # y of type is 'str'
print("x")

# If you want to specify the data type of a variable, this can be done with casting.
# Legal 'casting example'
x = str(3)      # x will be '3'
y = int(3)      # y wil be 3
z = float(3)    # z will be '3.0'

# You can get the data type of a variable with the type() function.
# 'Get the type' example
x = 5
y = "John"
print(type("x"))
print(type("y"))

# String variables can be declared either by using single or double quotes:
# Legal example ''Single or Double Quotes'
x = "John"
# Is the same as
x = 'John'

# Variable names are case-sensitive.
# Legal example 'case-sensitive'
a = 4
A = "Sally"
# A will not overwrite a


#1.2 - Intro - Python VARIABLE NAME:
        #1. A variable name must start with a letter or the underscore character
        #2. A variable name cannot start with a number
        #3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
        #4. Variable names are case-sensitive (age, Age and AGE are three different variables)
        #5. A variable name cannot be any of the Python keywords.

# Legal example
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal example
#2myvar = "John" # Illegal cause it starts with a number;
#my-var = "John" # Illegal cause it the variable is created with a -, only _ is correct
#my var = "John" # Illegal cause it my and var are not connected to each other;

# MULTI WORDS VARIABLE NAMES
    # Variable names with more than one word can be difficult to read.
        # There are several techniques you can use to make them more readable:

#1. Camel Case
    # each word, except the first one, starts with a capital letter;
      #  myVariableName = "John"

#2. Pascal Case
    # each word starts with a capital letter;
        #MyVariableName = "John"

#3. Snake Case
    # ech word is separated by an underscore character;
        #my_variable_name = "John"


#1.3 - Intro - Assign Multiple Values / Variables

# Python allows you to assign values to multiple variables in one line:
# Legal example 'Many values to Multiple Variables'
x, y, z = "Orange", "Blue", "Yellow"
print(x)
print(y)
print(z)
# NOTE: Make sure the number of variables matches the number of values, or else you will get an error.

# And you can assign the same value to multiple variables in one line:
# Legal example 'One Value to Multiple Variables'
x = y = z = "orange"
print(x)
print(y)
print(z)

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
# Legal example 'Unpack a Collection'
fruits = {"apple", "banana", "cherry"}
x, y, z = fruits
print(x)
print(y)
print(z)

#1.4 - Intro - Output Variable

# The Python print() function is often used to output variables.
# Legal example 1

x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, separated by a comma:
# Legal example 2

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:
# Legal example 3
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

# For numbers, the + character works as a mathematical operator:
# Legal example 4
x = 5
y = 10
print(x + y)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
# ILLEGAL example 5
x = 5
y = "John"
#print(x + y)
# Hiermee ontstaat er een fout, omdat je geen getal met een naam kunt plussen.

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
# Legal example 6
x = 5
y = "John"
print(x, y)
# Door de comma te plaatsen in plaats van een + teken, kun je verschillende type data combineren.

#1.5 - Intro - Global Variable

# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
# Legal example 1: 'Create a variable outside of a function, and use it inside the function'

x = "awesome"

def myfunc():
    print("My python is " + x)

myfunc()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.
# Legal example 1 : 'Create a variable inside a function, with the same name as the global variable'

x = 'fantastic'

def myfunc():
    x = 'great'
    print("My python is " + x)

myfunc()
print("My python is " + x)

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
# If you use the global keyword, the variable belongs to the global scope:
# Example 1: 'The Global Keyword'

def myfunc():
    global x
    x = 'great'

myfunc()
print("Python is " + x)

def myfunc():
    global z
    z = 'sad'

myfunc()
print ("Python is " + z)

# Also, use the global keyword if you want to change a global variable inside a function.
# Example 2: To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = 'awesome'

def myfunc():
    global x
    x = 'fantastic'

myfunc()
print("Python is " + x)

# De inside functie def, is in het bovenstaande geval leidend. Waardoor de outside varaibele 'awesome' komt te vervallen.
# Hieronder een voorbeeld zonder global, dat resulteert in de outside variabele 'awesome'

x = 'awesome'

def myfunc():
    x = 'fantastic'

myfunc()
print("Python is " + x)

# Excersise the end of the first chapter
# Create a variable as 'carname' and assign the value of 'volvo' to it.

x = 'Carname'
y = 'Volvo'
z = 'Audi'
a = 'BMW'
print("Carname is", y)

# Of

x = "Volvo"

def myfunc():
    print("carname is " + x)

myfunc()
print("carname is " + x)


















