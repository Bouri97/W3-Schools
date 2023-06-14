# String 1.0

# Strings in python are surrounded by either single quotation marks, or double quotation marks. 1.1

# 'hello' is the same as "hello".
# You can display a string literal with the print() function:

print("Hello")      # Beiden hetzelfde
print('Hello')      # Beiden hetzelfde

# Assign String to a Variable 1.2
    # Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello"
print(a)

# Multiline Strings 1.3
    # You can assign a multiline string to a variable by using three quotes:

a = """Ik ben Rick Bouckaert ben inmiddels 26 jaar,
ik ben werkzaam als WOZ=taxateur
Inmiddels doe ik er ook ander werk bij"""
print(a)

# De 3 """ maken het mogelijk om een langer verhaal, met een drietal lijnen te verwerk onder een str."""

# Or three single quotes:
a = '''Ik ben Rick Bouckaert ben inmiddels 26 jaar,
ik ben werkzaam als WOZ=taxateur
Inmiddels doe ik er ook ander werk bij!'''
print(a)

# Note: in the result, the line breaks are inserted at the same position as in the code.

# Strings are Arrays 1.4
    # Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
    # However, Python does not have a character data type, a single character is simply a string with a length of 1.
    # Square brackets can be used to access elements of the string.

# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello,World!"
print(a[1])

# Looping Through a String 1.5
    # Since strings are arrays, we can loop through the characters in a string, with a for loop.
    # Loop through the letters in the word "banana":

for x in "Banana":
    print(x)

# String Length 1.6
    # To get the length of a string, use the len() function.
    # The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))

# Check String 1.7
    # To check if a certain phrase or character is present in a string, we can use the keyword in.
    # Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)

    # Use it 'if' statement 1.7.1

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is represent.")

    # Use it 'not in' statement 1.7.2
    # Check if "expensive" is NOT present in the following text:

txt = "The best thins in life are free!"
print("expensive" not in txt)

    # Use it 'if not in' statement 1.7.3
    # print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensivee" not in txt:
    print("No, 'expensive' is not present!")

# Modify Strings Hoofdstuk 2
    # Upper case 2.1
        # The upper() method returns the string in upper case:
        # Example
a = "Hello, World!"
print(a.upper())

    # Lower Case 2.2
        # The lower() method returns the string in lower case:
        # Example
a = "Hello, World!"
print(a.lower())

    # Remove Whitespace 2.3
    # Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
    # The strip() method removes any whitespace from the beginning or the end:
    # Example
a = " Hello, World! "
print(a.strip())            # Returns in to "Hello, World", without a whitespace

    # Replace String 2.4
    # The replace() method replaces a string with another string
    # Example
a = "Hello, World!"
print(a.replace("H", "J"))      # The H will change into J

    # Split String 2.5
    # The split() method returns a list where the text between the specified separator becomes the list items.
    # Example
a = "Hello, World!"
print(a.split(","))         # Returns ['Hello', 'World!']

# String Concatenation, Hoofdstuk 3
    # To concatenate, or combine, two strings you can use the + operator.
    # Example
        # Merge variable a with variable b into variable c:
a = "Hello "
b = "World"
c = a + b
print(c)

    # Example
        # To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)


# String Format, Hoofdstuk 4
    # As we learned in the Python Variables chapter, we CANNOT combine strings and numbers like this:
    # Example
            # age = 36
            # txt = "My name is John and i am " + age " old "
            # print(txt)

    # But we CAN combine strings and numbers by using the format() method!
    # The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
    # Example
age = 36
txt = "My name is Rick, and I am {} old"
print(txt.format(age))

    # The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of {} for {} dollars"
print(myorder.format(quantity, itemno, price))

    # You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity = 3            # = 0
itemno = 567            # = 1
price = 49.95           # = 2
myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))

# Escape Character, Hoofdstuk 5
    # To insert characters that are illegal in a string, use an escape character.
    # An escape character is a backslash \ followed by the character you want to insert
    # An example of an ILLEGAL character is a double quote inside a string that is surrounded by double quotes:

# You will get an ERROR if you use double quotes inside a string that is surrounded by double quotes:
    # txt = "We are the so called "Vikings" from the north"
    # print(txt)

# To fix this problem, use the escape character \":
# The escape character allows you to use double quotes when you normally would not be allowed
txt = "We are the so called \"Vikings\" from the north"
print(txt)

# Escape Characters
        # CODE                         # RESULT
#1        \'                          # Single quote
#2        \\                          # Backslash
#3        \n                          # New line
#4        \r                          # Carriage Return
#5        \t                          # Tab
#6        \b                          # Backspace
#7        \f                          # Form Feed
#8        \ooo                        # Octal value
#9        \xhh                        # Hex value

#1 - Example
txt = 'It\'s alright.'
print(txt)

#2 - Example
txt = "This will insert one \\ (backslash)"
print(txt)

#3 - Example
txt = "Hello\nWorld!"
print(txt)

#4 - Example
txt = "Hello\rWorld!"
print(txt)

#5 - Example
txt = "Hello\tWorld!"
print(txt)

#6 - Example
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)

#7 - Example
txt = "Hello\fWorld!"
print(txt)

#8 - Example
txt = "Hello \bWorld!"
print(txt)

#9 - Example
#A backslash followed by three integers will result in a octal (zijn de cijfers 0 t/m 7) value:
txt = "\110\145\154\154\157"
print(txt)

#10 - Example
#A backslash followed by an 'x' and a hex number represents a hex value (getallen reeks die gekoppeld zijn aan een kleur(groen, rood en blauw):
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

# String Methods - Hoofdstuk 6
# NOTE: All string methods return new values. They do not change the original string.

# capitalize()	            Converts the first character to upper case
txt = "python is FUN!"
x = txt.capitalize()
print(x)

# casefold()	            Converts string into lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

# center()	                Returns a centered string
    # length	Required. The length of the returned string
    # character	Optional. The character to fill the missing space on each side. Default is " " (space)
txt = "banana"
x = txt.center(20, "O")
print(x)

# count()	                Returns the number of times a specified value occurs in a string
    # value	Required. A String. The string to value to search for
    # start	Optional. An Integer. The position to start the search. Default is 0
    # end	Optional. An Integer. The position to end the search. Default is the end of the string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

# encode()	                Returns an encoded version of the string
    # encoding	Optional. A String specifying the encoding to use. Default is UTF-8
    # errors	Optional. A String specifying the error method. Legal values are:
            # 'backslashreplace'	- uses a backslash instead of the character that could not be encoded
            # 'ignore'	- ignores the characters that cannot be encoded
            # 'namereplace'	- replaces the character with a text explaining the character
            # 'strict'	- Default, raises an error on failure
            # 'replace'	- replaces the character with a questionmark
            # 'xmlcharrefreplace'	- replaces the character with an xml character
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

# endswith()	            Returns true if the string ends with the specified value
    # value	Required. The value to check if the string ends with
    # start	Optional. An Integer specifying at which position to start the search
    # end	Optional. An Integer specifying at which position to end the search
txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

# expandtabs()	            Sets the tab size of the string
    # tabsize	Optional. A number specifying the tabsize. Default tabsize is 8
txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

# find()	                Searches the string for a specified value and returns the position of where it was found
    # value	Required. The value to search for
    # start	Optional. Where to start the search. Default is 0
    # end	Optional. Where to end the search. Default is to the end of the string
txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)

# format()	                Formats specified values in a string

# format_map()	            Formats specified values in a string
# index()	                Searches the string for a specified value and returns the position of where it was found
# isalnum()	                Returns True if all characters in the string are alphanumeric
# isalpha()	                Returns True if all characters in the string are in the alphabet
# isdecimal()	            Returns True if all characters in the string are decimals
# isdigit()	                Returns True if all characters in the string are digits
# isidentifier()	        Returns True if the string is an identifier
# islower()	                Returns True if all characters in the string are lower case
# isnumeric()	            Returns True if all characters in the string are numeric
# isprintable()	            Returns True if all characters in the string are printable
# isspace()	                Returns True if all characters in the string are whitespaces
# istitle()	                Returns True if the string follows the rules of a title
# isupper()	                Returns True if all characters in the string are upper case
# join()	                Joins the elements of an iterable to the end of the string
# ljust()	                Returns a left justified version of the string
# lower()	                Converts a string into lower case
# lstrip()	                Returns a left trim version of the string
# maketrans()	            Returns a translation table to be used in translations
# partition()	            Returns a tuple where the string is parted into three parts
# replace()	                Returns a string where a specified value is replaced with a specified value
# rfind()	                Searches the string for a specified value and returns the last position of where it was found
# rindex()	                Searches the string for a specified value and returns the last position of where it was found
# rjust()	                Returns a right justified version of the string
# rpartition()	            Returns a tuple where the string is parted into three parts
# rsplit()	                Splits the string at the specified separator, and returns a list
# rstrip()	                Returns a right trim version of the string
# split()	                Splits the string at the specified separator, and returns a list
# splitlines()	            Splits the string at line breaks and returns a list
# startswith()	            Returns true if the string starts with the specified value
# strip()	                Returns a trimmed version of the string
# swapcase()	            Swaps cases, lower case becomes upper case and vice versa
# title()	                Converts the first character of each word to upper case
# translate()	            Returns a translated string
# upper()	                Converts a string into upper case
# zfill()	                Fills the string with a specified number of 0 values at the beginning









































