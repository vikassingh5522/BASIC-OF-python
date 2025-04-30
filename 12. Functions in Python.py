# A function is a block of code which only runs when it is called to run specific task.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Two types of Function:
# 1) Built in Function - example - print(), type(), input(), etc. 
# 2) User Defined Function

# 1) Built in Function:

a=10
b=20

c = max((a,b))
print(c)

a=10
b=20

c = sum((a,b))
print(c)

name = ("Enter Your Name:")

print(type(name))


# Creating our own Function:
# In Python a function is defined using the def keyword

def my_function():
    name = "Hello World!"
    print(name)

# Indentation will be check - 4 left spaces after function start
# Calling a Function: To call a function, use the function name followed by parenthesis

my_function()

# WAP to get square of Number using Function:
a = 5
def new_function():
    result = a*a
    print("a variable Square is:",result)
    

new_function()

# Creating Function with Arguments
# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

def my_function(fname):
    print("Hello ", fname)

    
my_function("Aditya")
my_function("Ramesh")
my_function("Suresh")


# WAP for Using function get the total and percentage of 5 subjects marks

def percentage(total):
    per = total/500*100
    return per


c_lang = 80
java = 60.76
testing = 85.76
python = 90.50
php = 75

tot = sum((c_lang,java,testing,python,php))

result = percentage(tot)
print("Total Marks are:",tot)
print("Your Percentage is:",round(result,2))






