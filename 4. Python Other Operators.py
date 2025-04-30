# 2) Python Assignment Operators:✅ 
#  Assignment operators are used to assign values to variables:

x = 5

print(x)

x += 3
# Note : It is the same as x = x+3
print(x)

x -= 3
print(x)

x *= 3
print(x)

x /= 3
print(x)


# 3) Python Comparison or Relational Operators Comparison operators are used to compare two values and returns Boolean Value True or False:

a=5
b=3
c= a==b

print(c)

# Other Relations Operator as:✅ 
# ==  !=  >   <   >=   <=


# 4) Python Logical Operators : Logical operators are used to combine conditional statements:✅ 

a = 5
b = a>4 and  a>2
print(b)

# Note : Returns True if both statements are true
# Note : Returns Boolean value

a = 5
b = a>4 or a<2
print(b)

# Note : Returns True if one of the statements is true

a = 5
b = not(a>4 and a>2)
print(b)

# Note : Reverse the result, returns False if the result is true


# 5) Python Identity Operators: Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

a = ["Rahul","Ramesh"]
b = ["Suresh","Ramesh"]
c =  a
print(c is a)

# Note: Returns True if both variables are the same object


a= ["Rahul","Ramesh"]
b= ["Suresh","Ramesh"]

c = b

print(c is not a)

# Note: Returns True if both variables are not the same object


# 6) Python Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

a = ["Suresh","Ramesh"]
print("Ramesh" in a)

# Note: Returns True if a sequence with the specified value is present in the object

a= ["Suresh","Ramesh"]
print("Rahul" not in a)

# Note: Returns True if a sequence with the specified value is not present in the object

# 7) Python Bitwise Operators Bitwise operators are used to compare (binary) numbers:

# In Python, bitwise operators are used to performing bitwise calculations on integers. The integers are first converted into binary and then operations are performed on bit by bit, hence the name bitwise operators. Then the result is returned in decimal format.

# Note: Python bitwise operators work only on integers.







