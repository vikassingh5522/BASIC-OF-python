# 2) Tuple:

# Tuples are used to store multiple datatypes items in a single variable.
# tuple items are ordered, immutable (un-changeable), and allow duplicate values.
# tuple are created using round brackets (or also called paranthesis)

student_names = ("ram", "ramesh", "suresh")
print(student_names)

# Note: print indexing value from list:
print(student_names[0]) 

# Note: Showing un-Changeable or called as immutable Tuple:
student_names = ("ram", "ramesh", "suresh")
student_names[0]="Rahul" 
print(student_names)

# It gives ERROR : as tuple is Immutable can not change element value
# TypeError: 'tuple' object does not support item assignment

# Adding Item in Tuple:
# as Tuple is Immutable means un-changable so we can not change tuple once it is creates,
# it means append() not available in tuple, but if we want to change tuple collection then we need to convert tuple into list and then we can use append() method and then again convert list to tuple

student_names = ("ram", "ramesh", "suresh")
print(student_names)

a = list(student_names)
a.append("Nikhil")
print(a)

student_names = tuple(a)
print(student_names)


# Add tuple to a tuple: 
# You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

student_names = ("ram", "ramesh", "suresh")
new_student = ("Aditya",)
student_names += new_student

print(student_names)

# Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

# Get the Length of tuple:

student_names = ("ram", "ramesh", "suresh")
print(len(student_names))

# Join two tuples:

student_names = ("ram", "ramesh", "suresh")

new_students= ("Nikhil","Praveen","Sham")

all_students = student_names + new_students

print(all_students)

# Unpacking a Tuple:
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple: 

fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

fruits = ("apple", "banana", "cherry","abc","xyz")

(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

# Note : Now red variable became list

# Using Asterisk* Tuple:

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(*green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Note: Now green variable is list

