# Python Tuples 1

    # Tuple 1.1
        # Tuples are used to store multiple items in a single variable.
        # Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are
            #1. List
            #2. Set
            #3. Dictionary
        # A tuple is a collection which is ordered and unchangeable.
        # Tuples are written with round brackets.

            #Example
thistuple = ("apple", "banana", "cherry")
print(thistuple)

    # Tuple Items
        # Tuple items are ordered, unchangeable, and allow duplicate values.
        # Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

    # Tuple Ordered
        # When we say that tuples are ordered, it means that the items have a defined order, and that order will not change

    # Tuple Unchangeable
        # Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

    # Allow Duplicates
        # Since tuples are indexed, they can have items with the same value:

            # Example
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

    # Tuple Length
        # To determine how many items a tuple has, use the len() function:

        # Example
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))

    # Create Tuple With One Item
        # Example
            # One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple

thistuple = ("apple")
print(type(thistuple))

   # Tuple Items - Data Types
        # Tuple items can be of any data type:
            # String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

        # A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

    # type()
        # From Python's perspective, tuples are defined as objects with the data type 'tuple':
            # <class 'tuple'>

        # Example
            # What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

    # The tuple() Constructor
        # It is also possible to use the tuple() constructor to make a tuple.

    # Example
thistuple = tuple(("apple", "banana", "cherry"))    # # note the double round-brackets
print(thistuple)

# Access Tuple, Hoofdstuk 2

    # Access Tuple Items 2.1
        # You can access tuple items by referring to the index number, inside square brackets:

    # Example
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Note: The first item has index 0.

    # Negative Indexing 2.2
        # Negative indexing means start from the end.
        # -1 refers to the last item, -2 refers to the second last item etc.

    # Example
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


    # Range of Indexes 2.3
        # You can specify a range of indexes by specifying where to start and where to end the range.
        # When specifying a range, the return value will be a new tuple with the specified items.

    # Example
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#This will return the items from position 2 to 5.

    #Remember that the first item is position 0,
    #and note that the item in position 5 is NOT included

#Note: The search will start at index 2 (included) and end at index 5 (not included).

        # By leaving out the start value, the range will start at the first item:
    # Example
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

        # By leaving out the end value, the range will go on to the end of the list:
    # Example
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

    # Range of Negative Indexes 2.4
        # Specify negative indexes if you want to start the search from the end of the tuple:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Negative indexing means starting from the end of the tuple.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,

    # Check if Item Exists 2.5
        # To determine if a specified item is present in a tuple use the in keyword:
    # Example
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


    # Update Tuples, hoofdstuk 3
        # Tuples are unchangeable, meaning that you cannot change, add, or remove items once
        # the tuple is created.
         # But there are some workarounds.


     # Change Tuple Values 3.1
        # Once a tuple is created, you cannot change its values. Tuples are unchangeable,
        # or immutable as it also is called.
        # But there is a workaround. You can convert the tuple into a list, change the list,
        # and convert the list back into a tuple.

    # Example
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

    # Add Items 3.2
        # Since tuples are immutable, they do not have a built-in append() method,
        # but there are other ways to add items to a tuple.

        # 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
    # Example
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)

      # 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item,
      # (or many), create a new tuple with the item(s), and add it to the existing tuple:
  # Example
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
# Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

  # Remove Items 3.3
# Note: You cannot remove items in a tuple.

    # Tuples are unchangeable, so you cannot remove items from it,
    # but you can use the same workaround as we used for changing and adding tuple items:
  # Example
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

    # Python - Unpack Tuples, Hoofdstuk 4

      # Unpacking a Tuple 4.1
        # When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
      # Example
fruits = ("apple", "banana", "cherry")
print(fruits)

    # But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
  # Example
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Note: The number of variables must match the number of values in the tuple, if not,
# you must use an asterisk to collect the remaining values as a list.

    # Using Asterisk* 4.2
        # If the number of variables is less than the number of values,
        # you can add an * to the variable name and the values will be assigned to the variable as a list:
    # Example
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

      # If the asterisk is added to another variable name than the last,
      # Python will assign values to the variable until the number of values left matches the number of variables left.
  # Example
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

     # Python - Loop Tuples, Hoofdstuk 5

      # Loop Through a Tuple 5.1
        # You can loop through the tuple items by using a for loop.
    # Example
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

    # Loop Through the Index Numbers
      # You can also loop through the tuple items by referring to their index number.
      # Use the range() and len() functions to create a suitable iterable.
    # Example
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

    # Using a While Loop 5.2
      # You can loop through the tuple items by using a while loop.

      # Use the len() function to determine the length of the tuple, then start at 0 and loop your way
      # through the tuple items by referring to their indexes.

      # Remember to increase the index by 1 after each iteration.
  # Example
  thistuple = ("apple", "banana", "cherry")
  i = 0
  while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

      # Python - Join Tuples, Hoofdstuk 6

        # Join Two Tuples
        # To join two or more tuples you can use the + operator:
