
# A lambda function is a small called as one line or anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax : lambda arguments : expression

a = lambda b : b + 10
print(a(5))

# Get the sqaure number using Lambda Function:
sqr = lambda b : b * b
print(sqr(5))

# Multiple argument a with argument b and return the result:
x = lambda a, b : a * b

result = x(5,6)

print(result)

# Get the Cube of Number:
lambda_cube = lambda y: y*y*y
print(lambda_cube(3))


# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

def myfunction(a):
  return lambda b : a * b
  
multi = myfunction(2)

print(multi(5))



