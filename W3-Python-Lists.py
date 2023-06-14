# Python List/Array Methods 1

    #List Append Method 1.1
        #The append() method appends an element to the end of the list.

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

            #Parameters values 1.1.1
                # Parameters; elmnt	Required. An element of any type (string, number, object etc.)
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

        #List CLear Method 1.2
            #The clear() method removes all the elements from a list.
                #No parameters
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

        #List Copy Method 1.3
            #The copy() method returns a copy of the specified list.
                #No parameters
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

        #List Count Method 1.4
            #The append() method appends an element to the end of the list.
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)

            #Parameters values 1.4.1
                #Value - Required. Any type (string, number, list, tuple, etc.). The value to search for.
fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = fruits.count(9)
print(x)

        #List Extend Method 1.5
            #The extend() method adds the specified list elements (or any iterable) to the end of the current list.
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

            #Parameters values 1.5.1
                #Iterable - Required. Any iterable (list, set, tuple, etc.)
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

        #List Index Method 1.6
            #The index() method returns the position at the first occurrence of the specified value.
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

            #Parameters values 1.6.1
                #elmnt - Required. Any type (string, number, list, etc.). The element to search for
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)

#Note: The index() method only returns the first occurrence of the value.

        #List Insert Method 1.7
            #The insert() method inserts the specified value at the specified position.
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

            #Parameters values 1.7.1
                #pos - 	Required. A number specifying in which position to insert the value
                #elmnt - Required. An element of any type (string, number, object etc.)

        #List Pop Method 1.8
            #The pop() method removes the element at the specified position.
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

            #Parameters values 1.8.1
                #pos - 		Optional. A number specifying the position of the element you want to remove
                    #default value is -1, which returns the last item
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x)

#Note: The pop() method returns removed value.


        #List Remove Method 1.9
            #The remove() method removes the first occurrence of the element with the specified value.
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

            #Parameters values 1.9.1
                #elmnt - Required. Any type (string, number, list etc.) The element you want to remove


        #List Reverse Method 1.10
            #The reverse() method reverses the sorting order of the elements.
            #No parameters
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)


        #List Sort Method 1.11
            #The sort() method sorts the list ascending by default.
                #You can also make a function to decide the sorting criteria(s).
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

                #Parameters values 1.11.1
                    #reverse - Optional. reverse=True will sort the list descending. Default is reverse=False
                    #key - 	Optional. A function to specify the sorting criteria(s)

# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)

def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
print(cars)

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

print(cars)