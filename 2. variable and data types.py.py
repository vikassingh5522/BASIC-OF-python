# Type Casting - 
# Changing data type Forsecully into another Data type

a = int(2.8) 
print(a)

# Note : When we take input from user For Arithmatic Operations we need to type casting into integer
# as using input() data received as string and arithmatic operations we can not do with string and integers
# Example : a = int(input("Enter First Number:")) 

b = float(2)
print(b)

c = str(2)
print(c)


# Python Operators are used to perform operations on variables and values. 
# There are 7 Python operators in the following groups: 

# 1. Arithmetic operators ✅ 
# 2. Assignment operators ✅ 
# 3. Relational or Comparison operators ✅ 
# 4. Logical operators ✅ 
# 5. Identity operators ✅ 
# 6. Membership operators ✅ 
# 7. Bitwise operators✅ 

# 1. Arithmetic operators 
# Addition of two Numbers:

a = 5
b = 5
c = a + b
print("Total is:",c)

# Take Any Two numbers from User and Perform Addition Program:

a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = a + b
print("Total is:",c)

# Substraction of two Numbers:

a = 5
b = 2
c = a-b
print("Total is:",c)

# Take Any Two numbers from User and Perform Substraction Program:

a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c = a - b
print("Total is:",c)

# Multiplication: 
# Take Any one number from User and get the Square of that number:

num = int(input("Enter Any Number:"))
sqr = num * num
print("Square of Entered Number is:",sqr)


# Division:

a=int(input("Enter Any Number:"))
b=int(input("Divided By:"))
c = a/b
print("Division Number is:",c)


# Modulus:

a = 7
b = 2

c = a % b
print("Modulus is:",c)


# Exponentiation:

a = 2
b = 5
c = a ** b
print("Exponentiation is:",c)


# Floor division:

apple = 7
men = 3
floor= apple // men
print("Floor division is:",floor)
