#Python - If ... Else - Hoofdstuk 1

        #Python Conditions and If statements 1.1
    #Python supports the usual logical conditions from mathematics:
            #Equals: a == b
            #Not Equals: a != b
            #Less than: a < b
            #Less than or equal to: a <= b
            #Greater than: a > b
            #Greater than or equal to: a >= b

    #These conditions can be used in several ways, most commonly in "if statements" and loops.
        #An "if statement" is written by using the if keyword.
#Example
a = 33
b = 200

if b > a:
  print("b is greater than a")

    #In this example we use two variables, a and b,
      #which are used as part of the if statement to test whether b is greater than a.
        #As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater than a".

#Note: - Identation
  #When you are not using the the identation by an "If Statement", you will get an error
#Example - No tab function been used after the "If Statement"

#if b > a:
#print("b is greater than a")

        #Python - Elif 1.2
      #The elif keyword is Python's way of saying "if the previous conditions were not true,
        #then try this condition".
#Example
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

      #In this example a is equal to b, so the first condition is not true,
        #but the elif condition is true, so we print to screen that "a and b are equal".

        #Python - Else 1.3
      #The else keyword catches anything which isn't caught by the preceding conditions.
#Example
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Note: You can also have an else without the elif:
#Example
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

        #Python - Short Hand If 1.4
      #If you have only one statement to execute, you can put it on the same line as the if statement.
#Example
  #One line if statement:
a = 200
b = 33
if a > b: print("a is greater than b")

        #Python - Short Hand If .. Else 1.5
      #If you have only one statement to execute, one for if, and one for else,
        #you can put it all on the same line:
a = 2
b = 330
print("A") if a > b else print("B")

      #You can also have multiple else statements on the same line:
#Example
  #One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

        #Python - And 1.6
      #The and keyword is a logical operator, and is used to combine conditional statements:
#Example
  #Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

        #Python - Or 1.7
      #The or keyword is a logical operator, and is used to combine conditional statements:
#Example
  #Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

        #Python - Not 1.8
      #The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
#Example
  #Test if a is NOT greater than b:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

        #Python - Nested If 1.9
      #You can have if statements inside if statements, this is called nested if statements.
#Example
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

        #Python - The pass Statement 1.10
      #if statements cannot be empty, but if you for some reason have an if statement with no content,
        #put in the pass statement to avoid getting an error.
#Example
a = 33
b = 200

if b > a:
  pass
# having an empty if statement like this, would raise an error without the pass statement