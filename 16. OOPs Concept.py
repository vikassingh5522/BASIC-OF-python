# Python is an object oriented programming language.

# Class : A Class is a blueprint or template for creating objects.

# Object : An Object is a real world entity.

# Note : When we create class there will be NO memory allocation but when we create object then memory will allocate.

# Create a Class
# To create a class, use the keyword class classname:

class MyClass:
    a = 5
        

# Creating Object and Accessing value from class
x = MyClass()    
print(x.a)

# x is the Object and we are accessing a value using object


class CollegeForm():
    def student_details(self):
        print("Your Name is:",self.name)
        print("Your Roll Number is:",self.roll_number)

ramesh = CollegeForm()
ramesh.name = "Ramesh Patil"
ramesh.roll_number = "10"

# Note : name and roll_number called as instance variable which we are using with object to enter data.

ramesh.student_details()
# Note : When Object calling function inside of class, default it will send value therefore self argument we need to mention to receive default value else error will show

ram = CollegeForm()
ram.name = "Ram"
ram.roll_number = "20"

ram.student_details()

# WAP to get addition of 2 numbers using class and object.

class addition():
    def add(self):
        a = 5
        b = 10
        c = a + b
# Note : a and b called as Member variable which we written in inside class
        print("Total is:",c)

num = addition()     
num.add()



# WAP for addition of 2 numbers with argument pass through function.

class addition():
    def add(self,a,b):
        self.a = a
        self.b = b
        c = a + b
# Note : a and b called as Member variable which we written in inside class
        print("Total is:",c)

num = addition()        
num.add(10,20)

# Constructor Function in Python or Special Function:

class addition():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        c = a + b
# Note : a and b called as Member variable which we written in inside class
        print("Total is:",c)

num = addition(10,20)        

# For constructor NO Need to call function, automatically inside constructor function will call

class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a + self.b
    def multi(self):
        return self.a * self.b
    def sub(self):
        return self.a - self.b

a = int(input("Enter 1st Number:"))
b = int(input("Enter 2nd Number:"))

obj = calculator(a,b)

choice = 1
while choice!=0:
    print("0.Exit:")
    print("1.Addition:")
    print("2.Multiplication:")
    print("3.Substraction:")
    choice = int(input("Enter Your Choice:"))

    if choice == 1:
        print()
        print("Addition of Entered Number is :",obj.add())
        print()
    elif choice == 2:
        print()
        print("Multiplication of Entered Number is :",obj.multi())
        print()
    elif choice == 3:
        print()
        print("Substraction of Entered Number is :",obj.sub())
        print()
    elif choice == 0:
        print()
        print("Exiting")
        print()
    else:
        print()
        print("You Entered Wrong Number.")
        print()



















