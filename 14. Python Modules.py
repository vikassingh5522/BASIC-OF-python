# A Module is a file which containing functions, that we can imported and use for our programs.

# Using Two Method we can use Modules as:
# 1) Built in Modules - Pre-Installed Modules in Python still we need to import in our current .py file

# 2) External Modules - We have to create module(file) and then import that module in our current file (.py) before use function which is available in created module

# 1) Built in Modules Examples:
# https://docs.python.org/3/py-modindex.html - All Built in Modules of Python

import time
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

import calendar
cal = calendar.month(2022,5)
print(cal)
# Month function takes 2 argument, Year and month

# 2) External Modules in Python:
# create a new file with extension .py and in that we can write functions
# Module name first character should be capital as My_module.py (M capital) or Abc.py (A capital)


# WAP Create a Module with square and cube function and get the result.

import My_Module
result = My_Module.sqr(5)
print(result)

import My_Module
result = My_Module.cube(5)
print(result)

# Allias Module Name to short name of module

import My_Module as m
result = m.sqr(3)
print(result)

# Variables in Module : we can save variable also as we save function similarly we can save variable and can use in programs.

import My_Module
print(My_Module.student_names["roll_number"])

# Using the dir() Function - Syntax - dir(module_name)
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

import My_Module
x = dir(My_Module)
print(x)


# Import From Module
# You can choose to import only parts from a module, by using the from keyword.

from My_Module import student_names

print(student_names["name"])










