# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello"

# Assign String to a Variable

a = "Hello"
print(a)

a = input("Enter Training Name:")
print("Training Name is :", a)


# Multiline Strings:
a='Hello\
World'

a = ''' Hello
Python
World '''

# Python Slicing Strings:
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

# Get the characters from position 2 to position 5 (not included)

b = "Hello, World!"

print(b[2:5])

# Note: Indexing starts with 0

# String Methods:

# 1) len()

data = "Python Training and Internship"
a = len(data)
print(a)

# Note: one argument will be pass that is variable name
# Note: It will show you count of string which is available in variable

# 2) lower()

data = "Python Training and Internship"
a = (data.lower())
print(a)

# 3) upper()

data="Python Training and Internship"
a=(data.upper())
print(a)

# 4) replace("replacing word","new word which you want replace")
# Note: 2 Arguments will pass in replace() method

data = "Python Training and Internship"
a = (data.replace("Training","Industrial Training"))  
print(a)

# Note: word is case sensetive, exact you need to write in method then only it will change

# 5) split()

data="Python Training and Internship"
a=(data.split())  
print(a)

# 6) capitalize()
# Note : convert string first character capital other all words will be small letter

data="python Training and Internship"
a=(data.capitalize())  
print(a)

# 7) title()
# Note : convert first character capital of every word of string

data="Python training and internship"
a = (data.title())  
print(a)

# 8) center(one argument will be pass that is width)
# Note : From left side of the screen in the output how far you want to display string
# that time you will use this center() method and width in pixel from left side

data="python Training and Internship"
a=(data.center(50))  
print(a)

# 9) endswith("one argument will be pass that words which we want to find in double quote")

# Note: It returns Boolean value True or False
# Note: searching word is case sensetive

data="python Training and Internship"
a=(data.endswith("ship"))  
print(a)

# 10) find("one argument will be pass that words which we want to find in double quote")

# Note: It returns on which position that word is present that number assign to variable
# Note: searching word is case sensetive

data="python Training and Internship"

a = (data.find("and"))  

print(a)


# 11) index("one argument will be pass that words which we want to find in double quote")

# same as find() method

# 12) isalpha() method retuns true if string contain only characters space also not allowed if space found then returns false

# Boolean value return

data="Python Training and Internship"
a=(data.isalpha())  
print(a)

# 13) isdigit() method retuns true if string contain only digits space also not allowed if space found then returns false

# Boolean value return

data="12345"
a=(data.isdigit())  
print(a)

# 14) isspace() method retuns true if string contain only space else return false

# Boolean value return

data=" "
a=(data.isspace())  
print(a)

# 15) istitle() method check each word first character capital or not if yes then return true else false

# Boolean value return

data = "Python Internship"
a = (data.istitle())  
print(a)

# 16) count("one argument pass - which word we are searching in string it will check how many times present in string and that number gives to variable")

# Note: words should be case sensetive

data = "Python Training and DJango Training Internship"
a = (data.count("Training"))  
print(a)

# 17) join(one argument pass and that is variable name on which you want to perform join() method)

# Note: Use to add special characters or any word after each element of string
# Note: list is iterable means changable therefore use with list

list = ["Python","DJango","Web Development"]

a="--".join(list)

print(a)





