# Python Collections : 4 Types of Collections as:
# 1) List   [] braket 
# 2) Tuple ( ) braket
# 3) Set
# 4) Dictionaries


# 1) List:

# Lists are used to store multiple datatypes items in a single variable.
# List items are ordered, changeable (Mutuable), and allow duplicate values.
# Lists are created using square brackets

student_names = ["ram", "ramesh", "suresh", 10, 10.5]
print(student_names)

# Note: print indexing value from list:
print(student_names[0]) 

# Note: Showing Changeable list:
student_names = ["ram", "ramesh", "suresh"]
student_names[0]="Rahul" 
print(student_names)

# Note: Adding new item in list and list allow duplicate value:
# Note: Using append("one argument allow only") method we can add one item in list at a time

student_names = ["ram", "ramesh", "suresh"]
student_names.append("suresh")
print(student_names)

# List is Ordered means
# it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.


# Removing item in list:
# Note: Using remove("one argument allow only") method we can remove one item in list at a time

student_names = ["ram", "ramesh", "suresh"]
student_names.remove("suresh")
print(student_names)

# Note : remove() method case sensetive

# Clearing the List:

student_names = ["ram", "ramesh", "suresh"]
student_names.clear()
print(student_names)


# deleting List:

student_names = ["ram", "ramesh", "suresh"]
del student_names
print(student_names)

# List() Constructor: Using list() constructor we can also create list

student_names = list(("ram", "ramesh", "suresh"))
student_names.append("Nikhil")
print(student_names)


