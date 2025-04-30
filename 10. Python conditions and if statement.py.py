# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# These conditions can be used in several ways, most commonly in "if statements" and loops.
# "if statement" is written by using the if keyword.

# Simple If Statement

# if condition:
    # excute this block if condition is true else it will exit 


a = 10
b = 20
if b > a:
    print("b is greater than a") 


# Always remember Indentation means after we enter : it gives 4 left spaces and from that position only we need to write else indentation error will show

# if we did not maintain indentation gives error as:
# IndentationError: expected an indented block

# If-else Statement
# if condition:
    # excute this block if condition true
# else:  
    # excute this block if condition false

# Example 1
a = int(input("Enter 1st Number:"))
b = int(input("Enter 2nd Number:"))

if a > b:
  print("A is greater than B")
else:
    print("B is Greater than A")

# Example 2
age = int(input("Enter Your Age:"))

if age >= 18:
    print("Congratulations! You are Eligible for Voting..")
else:
    print("Sorry! You are not eligible for voting..")

# Example 3 -  WAP take any number from User and find out whether it is even or odd.
num = int(input("Enter Any Number:"))

if num % 2 == 0:
    print("Entered Number is Even")
else:
    print("Entered Number is Odd")


# Elif Statement: Else If Statement
# Syntax : 
# if condition:
#     execute block1
# elif condition:
#     execute block2
# else:
#     execute block3

a = int(input("Enter 1st Number:"))
b = int(input("Enter 2nd Number:"))

if a > b:
    print("A is greater than B")
elif a==b:
    print("A and B is Equal")
else:
    print("B is Greater than A")    


# Nested If Statement: 
# When you use if statement inside if statement called as Nested If

# Note: Nested if only works when if condition is true

# Syntax : 
# if condition:
#     execute block1
#     if condition:
#         execute block2
#     else:
#         execute block3

# Example 1: (Nested If)
a = 15

if a > 10:
    print("A is greater than 10")
    if a > 20:
        print("A is also greater than 20")
    else:
        print("A is not greater than 20")
else:
    print("A is Less than 10")

# Example 2: (Nested If)
# WAP for take 3 numbers from User and find out out of three numbers which number is Greater

a = 10
b = 30
c = 20

if a>b and a>c:
    print("1st Number is Greater than 2nd and 3rd Number")
elif b>c and b>a:
        print("2nd Number is Greater than 1st and 3rd Number")
elif a==b and a==c:
        print("All Numbers are Equal")
else:
        print("3rd Number is Greater than 1st and 2nd")















