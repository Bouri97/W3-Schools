    # Python Sets - Hoofdstuk 1

        # Definition Set:
# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data,
    # the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

    # A set is a collection which is unordered, unchangeable*, and unindexed.

#  Note: Set items are unchangeable, but you can remove items and add new items.

    # Example
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: the set list is unordered, meaning: the items will appear in a random order.
# Refresh this page to see the change in the result.

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

        # Set Items 1.1
    # Set items are unordered, unchangeable, and do not allow duplicate values.

        # Unordered defenition;
    # Unordered means that the items in a set do not have a defined order.
    # Set items can appear in a different order every time you use them,
        #  and cannot be referred to by index or key.

        # Unchangeable defenition;
    # Set items are unchangeable, meaning that we cannot change the items after the set has been created.
    # Once a set is created, you cannot change its items, but you can remove items and add new items.

        # Duplicates Not Allowed defenition;
    # Sets cannot have two items with the same value.
    # Example, "apple" will be print once
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

    # Example
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

        # Get the Length of a Set 1.2
    # To determine how many items a set has, use the len() function.
# Example
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

        # Set Items - Data Types 1.3
    # Set items can be of any data type:
# Example
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

    # A set can contain different data types:
# Example
set1 = {"abc", 34, True, 40, "male"}
print(set1)

        # The set() Constructor 1.4
    # It is also possible to use the set() constructor to make a set.
# Example
thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.

# IMPORTANT!
    #Python Collections (Arrays)
    #There are four collection data types in the Python programming language:

    #List is a collection which is ordered and changeable. Allows duplicate members.
    #Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    #Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    #Dictionary is a collection which is ordered** and changeable. No duplicate members.

    #Python - Access Set Items, Hoofdstuk 2

        #Access Items, 2.1
    #You cannot access items in a set by referring to an index or a key.
    #But you can loop through the set items using a for loop,
        #or ask if a specified value is present in a set, by using the in keyword.

    thisset = {"apple", "banana", "cherry"}
    tropical = {"pineapple", "mango", "papaya"}

    thisset.update(tropical)

    print(thisset)
    #Example
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Example - True function;
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#Note: Change Items - Once a set is created, you cannot change its items, but you can add new items.

    #Python - Add Set Items, Hoofdstuk 3

        #Add Items 3.1
    #Once a set is created, you cannot change its items, but you can add new items.
        #To add one item to a set use the add() method.
#Example
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

        #Add Sets 3.2
    #To add items from another set into the current set, use the update() method.
#Example
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

        #Add Any Iterable 3.3
    #The object in the update() method does not have to be a set,
        # it can be any iterable object (tuples, lists, dictionaries etc.).
#Example
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

    #Python - Remove Set Items, Hoofdstuk 4

        #Remove Items 4.1
    #To remove an item in a set, use the remove(), or the discard() method.
#Example
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#Note: If the item to remove does not exist, remove() will raise an error.
#Example
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#Note: If the item to remove does not exist, discard() will NOT raise an error.
    #You can also use the pop() method to remove an item,
    # but this method will remove a random item, so you cannot be sure what item that gets removed.

    #The return value of the pop() method is the removed item.
#Example
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal

#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

#Example
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#Example - Comment toegevoegd, anders krijg je een error, door de "del-functie"
    #thisset = {"apple", "banana", "cherry"}
    #del thisset
    #print(thisset) #this will raise an error because the set no longer exists

    #Python - Loop Sets, Hoofdstuk 5

        #Loop Items 5.1
    #You can loop through the set items by using a for loop:
#Example
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

    # Python - Join Sets - Hoofdstuk 6

        #Join Two Set 6.1
    #There are several ways to join two or more sets in Python.
    #You can use the union() method that returns a new set containing all items from both sets,
        #or the update() method that inserts all the items from one set into another:
#Example - Union method
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#Example - Update method
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#Note: Both union() and update() will exclude any duplicate items.

        #Keep ONLY the Duplicates 6.2
    #The intersection_update() method will keep only the items that are present in both sets.
#Example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

    #The intersection() method will return a new set, that only contains the items that are present in both sets.
#Example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

        #Keep All, But NOT the Duplicates 6.3
    #The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
#Example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

    #The symmetric_difference() method will return a new set,
        #that contains only the elements that are NOT present in both sets.
#Example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
#Example
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)

#Note: False and 2 are NOT considered the same value.

    #Set Methods - Hoofdstuk 7

#Method - add()
    #Description; Adds an element to the set
#Example
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#Method - clear()
    #Description; Removes all the elements from the set
#Example
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#Method - copy()
    #Description; Returns a copy of the set
#Example
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

#Method - difference()
    #Description; Returns a set containing the difference between two or more sets
#Example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

#Method - difference_update()
    #Description; Removes the items in this set that are also included in another, specified set
#Example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

#Method - discard()
    #Description; Remove the specified item
#Example
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#Method - intersection()
    #Description; Returns a set, that is the intersection of two other sets
#Example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#Method - intersection_update()
    #Description; Removes the items in this set that are not present in other, specified set(s)
#Example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#Method - isdisjoint()
    #Description; Returns whether two sets have a intersection or not
#Example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

#Method - issubset()
    #Description; Returns whether another set contains this set or not
#Example
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

#Method - issuperset()
    #Description; Returns whether this set contains another set or not
#Example
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

#Method - pop()
    #Description; Removes an element from the set
#Example
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

#Method - remove()
    #Description; Removes the specified element
#Example
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

#Method - symmetric_difference()
    #Description; Returns a set with the symmetric differences of two sets
#Example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#Method - symmetric_difference_update()
    #Description; Inserts the symmetric differences from this set and another
#Example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#Method - union()
    #Description; Return a set containing the union of sets
#Example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

#Method - update()
    #Description; Update the set with the union of this set and others
#Example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)
