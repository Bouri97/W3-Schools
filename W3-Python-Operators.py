#Python Operators 1
    #Operators are used to perform operations on variables and values.
    #In the example below, we use the + operator to add together two values:

#Example
print(10+5)

#Python divides the operators in the following groups:

#Arithmetic operators
    #Arithmetic operators are used with numeric values to perform common mathematical operations:

    #Name = Addition
        #Operator = '+'
        #Example = x + y
x = 5
y = 3

print(x + y)

    #Name = Subtraction
        #Operator = '-'
        #Example = x -y
x = 5
y = 3

print(x - y)

    #Name = Multiplication
        #Operator = '*'
        #Example = x * y
x = 5
y = 3

print(x * y)

    #Name = Division
        #Operator = '/'
        #Example = x / y
x = 5
y = 3

print(x / y)

    #Name = Modulus
        #Operator = %
        #Exmaple = x % y
x = 5
y = 3

print(x % y)

    #Name = Exponentiation
        #Operator = '**'
        #Example = x ** y
x = 5
y = 3

print(x ** y)

    #Name = Floor Division
        #Operator = '//'
        #Example = x // y
x = 15
y = 2

print(x // y)
#the floor division // rounds the result down to the nearest whole number

#Assignment operators
    #Assignment operators are used to assign values to variables:

    #Operator - ' = '
    #Example - x = 5
    #Same as - x = 5
x = 5
print(x)

    #Operator - ' += '
    #Example - x += 3
    #Same as - x = x + 3
x = 5
x += 3
print(x)

    #Operator - ' -= '
    #Example - x -= 3
    #Same as - x = x - 3
x = 5
x -= 3
print(x)

    #Operator - ' *= '
    #Example - x *= 3
    #Same as - x = x * 3
x = 5
x *= 3
print(x)

    #Operator - ' /= '
    #Example - x /= 3
    #Same as - x = x / 3
x = 5
x /= 3
print(x)

    #Operator - ' %= '
    #Example - x %= 5
    #Same as - x = x % 3
x = 5
x%=3
print(x)

    #Operator - ' //= '
    #Example - x //= 5
    #Same as - x = x // 5
x = 5
x//=3
print(x)

    #Operator - ' **= '
    #Example - x **= 5
    #Same as - x = x ** 5
x = 5
x **= 3
print(x)

    #Operator - ' &= '
    #Example - x &= 3
    #Same as - x = x & 3
x = 5
x &= 3
print(x)

    #Operator - ' |= '
    #Example - x |= 5
    #Same as - x = x | 5
x = 5
x |= 3
print(x)

    #Operator - ' ^= '
    #Example - x ^= 3
    #Same as - x = x ^ 3
x = 5
x ^= 3
print(x)

    #Operator - ' >>= '
    #Example - x >>= 5
    #Same as - x = x >> 5
x = 5
x >>= 3
print(x)

    #Operator - ' <<= '
    #Example - x <<= 5
    #Same as - x = x << 5
x = 5
x <<= 3
print(x)

#Comparison operators
    #Comparison operators are used to compare two values:

    #Name = Equal
        #Operator = '=='
        #Example = x == y
x = 5
y = 3
print(x == y)
# returns False because 5 is not equal to 3

    #Name = Not Equal
        #Operator = '!='
        #Example = x != y
x = 5
y = 3
print(x != y)
# returns True because 5 is not equal to 3

    #Name = Greather than
        #Operator = '>'
        #Example = x > y
x = 5
y = 3
print(x > y)
# returns True because 5 is greater than 3

    #Name = Less than
        #Operator = '<'
        #Example = x < y
x = 5
y = 3
print(x < y)
# returns False because 5 is not less than 3

    #Name = Greater than or equal to
        #Operator = '>='
        #Example = x >= y
x = 5
y = 3
print(x >= y)
# returns True because five is greater, or equal, to 3

    #Name = Less than or equal to
        #Operator = '<='
        #Example = x <= y
x = 5
y = 3
print(x <= y)
# returns False because 5 is neither less than or equal to 3

#Logical operators
    #Logical operators are used to combine conditional statements:

    #Description = 	Returns True if both statements are true
        #Operator = 'and'
        #Example = x < 5 and x < 10
x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

    #Description = 	Returns True if one of the statements is true
        #Operator = 'or'
        #Example = x < 5 or x < 10
x = 5
print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

    #Description = 	Reverse the result, returns False if the result is true
        #Operator = 'not'
        #Example = not(x < 5 and x < 10)
x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result
# returns False because not is used to reverse the result

#Identity operators
    #Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object
    #with the same memory location:

    #Description = Returns True if both variables are the same object
        #Operator = 'is'
        #Example = x is y

    #Description = Returns True if both variables are not the same object
        #Operator = 'is not'
        #Example = x is not y

x = ("Apple, Banana")
y = ("Apple, Banana")
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y
    # even if they have the same content

print(x == y)
# to demonstrate the difference between "is" and "==":
    # this comparison returns True because x is equal to y

#Membership operators
    # Membership operators are used to test if a sequence is presented in an object:

    #Description = Returns True if a sequence with the specified value is present in the object
        #Operator = 'in'
        #Example = x in y

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

    #Description = Returns True if a sequence with the specified value is present in the object
        #Operator = 'in'
        #Example = x not in y

x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list

#Bitwise operators

