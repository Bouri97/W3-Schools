#Python - Python Dictionaries - Hoofdstuk 1

        #Dictionary 1.1
    #Dictionaries are used to store data values in key:value pairs.
    #A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
    #Dictionaries are written with curly brackets, and have keys and values:

#Example
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

        #Dictionary Items - 1.2
    #Dictionary items are ordered, changeable, and does not allow duplicates.
    #Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#Example
thisdict = {
  "brand": "Audi",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["model"])

#Ordered or Unordered?
    #Python version 3.7, dictionary are ordered
    #Python version 3.6, dictionary are unordered

        #When we say that dictionaries are ordered, it means that the items have a defined order,
            # and that order will not change.

        #Unordered means that the items does not have a defined order,
            # you cannot refer to an item by using an index.

#Changeable
    #Dictionaries are changeable, meaning that we can change,
        # add or remove items after the dictionary has been created.

        #Duplicates Not Allowed 1.3
    #Dictionaries cannot have two items with the same key:
#Example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

        #Dictionary Length 1.4
    #To determine how many items a dictionary has, use the len() function:
#Example - If you chose twice for "x-variable" then it will result in 1 (len)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020,
  "amount": 7,
  "person": "man"
}
print(len(thisdict))

        #Dictionary Items - Data Types 1.5
    #The values in dictionary items can be of any data type:
#Example
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

        #Type() 1.6
    #From Python's perspective, dictionaries are defined as objects with the data type 'dict':
        #<class 'dict'>
#Example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

        #The dict() Constructor 1.7
    #It is also possible to use the dict() constructor to make a dictionary.
#Example
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Note: Dictionary is a collection which is ordered** and changeable. No duplicate members.

#Python - Acces Dictionary Items - Hoofdstuk 2

      #Accessing Items 2.1
    #You can access the items of a dictionary by referring to its key name, inside square brackets:
#Example
  #Get the value of the "model" key:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

    #There is also a method called get() that will give you the same result:
#Example
  #Get the value of the "model" key:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)

      #Get Keys 2.3
    #The keys() method will return a list of all the keys in the dictionary.
#Example
  #Get a list of the keys:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)

    #The list of the keys is a view of the dictionary,
      #meaning that any changes done to the dictionary will be reflected in the keys list.
#Example
  #Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change

car["color"] = "white"
print(x) #after the change

      #Gets Values 2.4
    #The values() method will return a list of all the values in the dictionary.
#Example
  #Get a list of the values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)

    #The list of the values is a view of the dictionary,
      #meaning that any changes done to the dictionary will be reflected in the values list.
#Example
  #Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change

car["year"] = 2020
print(x) #after the change

#Example
  #Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change

car["color"] = "red"
print(x) #after the change

      #Get Items 2.5
    #The items() method will return each item in a dictionary, as tuples in a list.
#Example
  #Get a list of the key:value pairs
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()
print(x)

  #The returned list is a view of the items of the dictionary
    #meaning that any changes done to the dictionary will be reflected in the items list.
#Example
  #Make a change in the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change

car["year"] = 2020
print(x) #after the change

#Example
  #Add a new item to the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change

car["color"] = "blue"
print(x) #after the change

      #Check if Key Exists 2.6
    #To determine if a specified key is present in a dictionary use the in keyword:
#Example
  #Check if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


#Python - Change Dictionary Items - Hoofdstuk 3

      #Change Values 3.1
    #You can change the value of a specific item by referring to its key name:
#Example
  #Change the "year" to 2018:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

      #Update Dictionary 3.2
    #The update() method will update the dictionary with the items from the given argument.
    #The argument must be a dictionary, or an iterable object with key:value pairs.
#Example
  #Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)


#Python - Add Dictionary Items - Hoofdstuk 4

        #Adding Items 4.1
    #Adding an item to the dictionary is done by using a new index key and assigning a value to it:
#Example
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

      #Update Dictionary 4.2
    #The update() method will update the dictionary with the items from a given argument.
    #If the item does not exist, the item will be added.
    #Note: The argument must be a dictionary, or an iterable object with key:value pairs.
#Example
  #Add a color item to the dictionary by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)


#Python - Remove Dictionary Items - Hoofdstuk 5

      #Removing Items 5.1
    #There are several methods to remove items from a dictionary:
#Example
  #The pop() method removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#Example
  #The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#Example
  #The del keyword removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#Example
  #Note: The del keyword can also delete the dictionary completely:
#thisdict =	{
  #"brand": "Ford",
  #"model": "Mustang",
  #"year": 1964
#}
#del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists.

#Example
  #The clear() method empties the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


#Python - Loop Dictionaries - Hoofdstuk 6

      #Loop Through a Dictionary 6.1
    #You can loop through a dictionary by using a for loop.
    #When looping through a dictionary, the return value are the keys of the dictionary
      #but there are methods to return the values as well.
#Example
  #Print all key names in the dictionary, one by one:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

#Example
  #Print all values in the dictionary, one by one:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

#Example
  #You can also use the values() method to return values of a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)

#Example
  #You can use the keys() method to return the keys of a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)

#Example
  #Loop through both keys and values, by using the items() method:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)


#Python - Copy Dictionaries - Hoofdstuk 7

      #Copy a Dictionary 7.1
    #You cannot copy a dictionary simply by typing dict2 = dict1,
      #because: dict2 will only be a reference to dict1
        #and changes made in dict1 will automatically also be made in dict2.

    #There are ways to make a copy, one way is to use the built-in Dictionary method copy().
#Example
  #Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

  #Another way to make a copy is to use the built-in function dict().
#Example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Python - Nested Dictionaries - Hoofdstuk 7

      #Nested Dictionaries 7.1
    #A dictionary can contain dictionaries, this is called nested dictionaries.
#Example
  #Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

    #Or, if you want to add three dictionaries into a new dictionary:
#Example
  #Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

      #Access Items in Nested Dictionaries 7.2
    #To access items from a nested dictionary, you use the name of the dictionaries,
      #starting with the outer dictionary:
#Example
  #Print the name of child 2:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])

