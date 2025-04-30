# 3) Set: 

# Set is a collection which is un-ordered, 
# Set is un-changeble, un-indexed and do not allow duplicate value
# set are created using curly braces {   }

# Un-ordered Set collection

student_names = {"ram", "ramesh", "suresh"}
print(student_names)

# Un-changeble - Immutable Set collection

student_names = {"ram", "ramesh", "suresh"}
student_names[0]="ram patil"
print(student_names)

# Can not add duplicate item

student_names = {"ram", "ramesh", "suresh"}
student_names.add("ram")
print(student_names)

# Note: Error not show but duplicate value did not add

# add new one item in set

student_names = {"ram", "ramesh", "suresh"}
student_names.add("nikhil")
print(student_names)

# Note: add() method permits only one argument means only one item you can add in set

# For Multiple items adding in set

student_names = {"ram", "ramesh", "suresh"}
student_names.update(["nikhil","venkatash","shirish"])
# Note: multiple names we need to add in list

print(student_names)



