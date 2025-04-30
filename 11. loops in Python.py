# Looping Statement : While Loop and For Loop 
# excecute block of statements till condition is false

# While Loop:

a = 1
while a <= 10:
    print(a)
    a += 1
    

#   Indentation is important : increament value should be just below to print() method

# Branching Statement : Break, Continue and Return
# Break
# With the break statement we can stop the loop even if the while condition is true:

a = 1
while a <= 10:
  print(a)
  if a==5:
    break
  a += 1

# Note: Indentation required for break after every : you need to maintain indentation 

# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:

a = 0
while a <= 10:
  a += 1
  if a==5:
    continue
  print(a)
  

# Note: when a=5 then execution will jump and again starts with while loop


# For Loop:

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)

# Looping Through a String

for x in "banana":
    print(x)


# Use Break statement in For loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x =="banana":
        break
  
# The range() Method:
# Retuns a sequence of numbers, default starts with 0 and increament by 1

for x in range(10):
    print(x)

# range(start indexing position,end indexing position) - (end position is not included)

for x in range(2,7):
    print(x)

# WAP for take any number from user and show table of that entered number:

num = int(input("Enter Any Number:"))

for x in range(1,11):
    result = num * x
    print(num,"*",x,"=",result)




