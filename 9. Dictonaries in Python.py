# 4) Dictonaries: 

# Dictionary is a collection which is ordered, 
# dictionary items are Mutable (changeable) and do not allow duplicates.
# dictionary are created using curly braces {   }
# Dictionaries are used to store data values in key:value pairs "" : ""

# Note : As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are un-ordered.

# Create and print a dictionary:

mobile = {
    "brand":"apple",
    "model":"iphone12",
    "Year":"2022",
        }
print(mobile)

# Accessing Value using key from dictionary:

mobile= {"brand":"apple",
         "model":"iphone12",
        "Year":"2022",
        }

print(mobile["brand"])

# Dictionary is changable : We can change value by its keys:

mobile= {"brand":"apple",
         "model":"iphone12",
        "Year":"2021",
        }

mobile["Year"]= "2022"
print(mobile["Year"])

# Adding new item in Dictionary

mobile= {"brand":"apple",
         "model":"iphone12",
        "Year":"2022",
        }

mobile["color"]="Black"
# Note: keys are case sensetive 

# Duplicates Not Allowed in Dictionary
# Duplicate keys will overwrite existing key value

mobile= {"brand":"apple",
         "model":"iphone12",
        "Year":"2022",
        "Year":"2023",
        }

print(mobile)


# Removing one item from Dictionary
# For removing item pop("key name") method is used with one argument

mobile= {"brand":"apple",
         "model":"iphone12",
        "Year":"2022",
        }

mobile.pop("Year")
#  Note: keys are case sensetive 
# or we can use del keyword also
del mobile["model"]

print(mobile)

# Clearing data from Dictionary:
# No argument pass in clear() method

mobile= {"brand":"apple",
         "model":"iphone12",
        "Year":"2022"
        }

mobile.clear()
print(mobile)

# deleting Dictionary:

mobile = {"brand":"apple",
         "model":"iphone12",
        "Year":"2022",
        }

del mobile
print(mobile)

# Copy Dictionary into another dictionary:

mobile= {"brand":"apple",
         "model":"iphone12",
        "Year":"2022",
        }

phone = mobile.copy()
print(phone)


# Nested Dictionaries:
# A dictionary can contain dictionaries, this is called nested dictionaries.

myfamily = {
  "child1" : {
    "name" : "Rahul",
    "year" : "2004",
  },
  "child2" : {
    "name" : "Pooja",
    "year" : "2007",
  },
  "child3" : {
    "name" : "Ramesh",
    "year" : "2011",
             }
}


print(myfamily)

# Or, if you want to add three dictionaries into a new dictionary
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Rahul",
  "year" : "2004",
}
child2 = {
  "name" : "Pooja",
  "year" : "2007",
}
child3 = {
  "name" : "Ramesh",
  "year" : "2011",
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3,
}

print(myfamily)






