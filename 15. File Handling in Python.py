# File Handling in Python:
# File handling is an very important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files.

# Two Types of Files :
# 1) Text Files (Ex. .txt) represent as "t"
# 2) Binary Files (Ex. .jpg, .dat) represent as "b"

# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists


# Creating a File
a = open("demo.txt","x")


# Writing a File which we create
a = open("demo.txt","w")
a.write("Hi Students")
a.close()

# using "w" mode we can create file also if not exist with same name
# "w" mode overwrtie the data

# Append file - add data into existing file

a = open("demo.txt","a")
a.write("\n Next line")
a.close()


# Opening a File:
open("demo.txt","r")

# Reading a File:

a = open("demo.txt","r")
myfile = a.read()
print(myfile)
a.close()

# Opening a Website link using open()
import webbrowser as wb
wb.open('https://elitesoftwares.co.in/')

# Note : Using webbrowser module name we can open website link in Browser

# Reading a file line by line
a = open("demo.txt","r")
print(a.readline())
print(a.readline())
a.close()


# Getting file data using For loop
a = open("demo.txt","r")
for x in a:
    print(x)
a.close()


# With Statement also we can read file

with open("demo.txt","r") as a:
    print(a.read())

# Rename or Delete File:
# There is no function for rename file name, therefore we need to copy data of file1 into file2 and then delete file1

# For Rename or Delete file you need to import one module that os

import os
old_file = "test.txt"
new_file = "new_test.txt"

with open(old_file) as f:
    data = f.read()

with open(new_file,"w") as f:
    f.write(data)

f = open(new_file,"r")
print(f.read())


# Deleting File
# To delete a file, you must import the OS module, and run its os.remove() function:

import os

os.remove("test.txt")


# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

















