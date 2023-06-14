#1.1 - Python - Built in Data Types
    # Variables can store data of different types, and different types can do different things.
    # Python has the following data types built-in by default, in these categories:

# Different types:
    #text type: str
    #numeric types: int, float, complex
    #sequence types: list, tuple, range
    #mapping type: dict
    #set types: set, frozenset
    #boolean type: bool
    #binary type: bytes, bytearray, memoryview
    #none type: NoneType

# Getting the Data Type
# You can get the data type of any object by using the type() function:
# Example 1 - Print the data type of the variable x:

x = 5
print(type(x))

# Setting the Data type
# Below this line an example per data type;
                                                #DataType

x = "Hello World"                               #str
print(type(x))

x = 20                                          #int
print(type(x))

x = 20.5                                        #float
print(type(x))

x = 1j                                          #complex
print(type(x))

x = ["apple", "peer", "mango"]                  #list
print(type(x))

x = ("apple", "peer", "mango")                  #tuple
print(type(x))

x = range(8)                                    #range
print(type(x))

x = {"name" : "John", "age" : 36}               #dict
print(type(x))

x = {"apple", "peer", "mango"}                  #set
print(type(x))

x = frozenset({"apple", "peer", "mango"})       #frozenset
print(type(x))

x = True                                        #bool
print(type(x))

x = b"Hello"                                    #bytes
print(type(x))

x = bytearray(5)                                #bytearray
print(type(x))

x = memoryview(bytes(5))                        #memoryview
print(type(x))

x = None                                        #NoneType
print(type(x))

# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:
# Legal example of specify the data type:

x = str("Hello World")
print(x)

x = int(5)
print(x)

x = float(20.5)
print(x)

x = complex(3j)
print(x)

x = list(("apple", "peer", "mango"))
print(x)

x = tuple(("apple", "peer", "mango"))
print(x)

x = range(5)
print(x)

x = dict(name="John", age=36)
print(x)

x = set(("apple", "peer", "mango"))
print(x)

x = frozenset(("apple", "peer", "mango"))
print(x)

x = bool(4)
print(x)

x = bytes(5)
print(x)

x = bytearray(5)
print(x)

x = memoryview(bytes(5))
print(x)
