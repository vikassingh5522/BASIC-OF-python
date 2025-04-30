1
# old_age = input("enter your age :")
# new_age = int("old_age") +2
# print("new_age")



2
# x =input ("enter the x number:")
# y =input ("enter the y number:")
# sum =int(x)+int(y)
# # print (sum)




3
# name = "vikas "
# # print(name.find ("s"))

# print(name.replace("vikas", "king"))

# print(name)


4
# name ="the rock"
# print ("w" in name)

5
# result=(3+6)*5
# result =(55-100)/9
# print(result)

6
# c = str(2)
# print(c)

7
# apple = 7
# men = 3
# floor= apple // men
# print("Floor division is:",floor)


8
# a = ["Rahul","Ramesh"]
# b = ["Suresh","Ramesh"]
# c = a
# print(c is a)

9
# a = input("Enter Training Name:")
# print("Training Name is :", a) 

10
# print(3==3)

# print(3==2)

# print(3 != 2)   
# # ! opposite hoota hai valu ka



11 # logic gate 
    # and , or , and
    # AND == T T KA T OR F F KA F
    # OR ==  T F KA T  OR  {F F KA F  OR  T T KA T}
# print(2>3 or 2>1 )
# print(2>3 or 1<2)
    # AND ==  T T KA T {ONLY TT KA T BAKI SA SAB F}  AND F T KA F
    
    
12
   #if  = eles statement
# age = 20
# if age>18:    # stating conditions  
#     print("you are an adult")
#     print("you can vote")

# elif age <18 and age> 3 : # true or false
#      print("you are in school  ")
  
# else :      #end conditions
#     print("you are small  ")
    
# print("thank you")    
   
12.1
#  let build the calculator  (mini project)
# first = input("Enter first number: ")
# operator = input("Enter the operator (+, -, *, /, %): ")
# secound = input("Enter second number: ")

# first = int(first)
# secound = int(secound)

# if operator == "+":
#     result = first + secound
#     print("Result:", result)
# elif operator == "-":
#     result = first - secound
#     print("Result:", result)
# elif operator == "*":
#     result = first * secound
#     print("Result:", result)
# elif operator == "/":
#     if secound != 0:
#         result = first / secound
#         print("Result:", result)
#     else:
#         print("Cannot divide by zero")
# elif operator == "%":
#     result = first % secound
#     print("Result:", result)
# else:
#     print("Invalid operation")

13
 #range -----it is key bord 
# number =range(6)
# print(number)

14
  #loop   (while)
# i = 1
# while i <= 6:
#     print (i)   
#     i =i+1

#  inter view Q
# i = 1
# while i <= 600:
#     print (i * "*")   
#     i =i+1

# opposide side
# i = 6
# while i >= 0:
#     print (i * "*")   
#     i =i-1

14.1 
#  for loop **************************************** in list  eg:-
# for item in range(5):
#       print(item+1)
 
# 15                  ---------------------()---tuple
#                      --------------------[]---list 
#                       -------------------{}--- set 
#    list  eg
1
# marks =(5,2,6,8,99)
# print (marks[4])
2
# marks =[10 ,44,55,88,99]
# print(marks[1:2])
    
3 
# marks =(10,20,30,40,50,60)

# **************for score in marks:****************
#    print(score)   

4  #append*******add kar na 
# marks = [10,20,30,40,50,60]
# marks.append(99)
# print(marks)  

5  #insert *******starting number can be add
# marks = [10,20,30,40,50,60]
# marks.insert(0,99)
# print(marks)  
6
# marks length find in list 

# marks = [10,20,30,40,50,60]
#  marks.insert(0,40)
# print(len(marks))



7  # now foe while loop***********
# marks = [10,20,30,40,50,60]
# i=0
# while i<len(marks ):
#   print(marks[i])
#   i=i+1
  
# marks.clear()
# print(marks)

8
# break and continue    key word
1
# students = ["vikas", "vishal", "ram", "sam", "rock"]
# for student in students:
#     if student == "ram":
#         break
#     print(student)
2
# continue key 
# students = ["vikas", "vishal", "ram", "sam", "rock"]
# for student in students:
#      if student == "sam":
#          continue
#      print(student)
    
   
   
# tuple  in list symbol ( )

# marks=(1,2,3,4,5,6,7,8,9) 
# marks[0]=99
# 'tuple' object does not support item assignment

  #********** in tuple ther are 2 type operation 
    
    # ------------- it count the number 

# marks= (95,55,44,99,77,77,99,77)
# print(marks.count(77))
# now for index----------------
# print(marks.index(99))

1 
  
  #  ()tuple in to the {}-->set

# marks= {95,55,44,99,77,77,99,77}

# person = "ram" "vikas" "vikas" "rock" "right"
# print(marks.index(99))






























# **********************************function**********************
1 #in built function   ---int ,bool , chr ,str

2 #Module function   --------store in one function

3 #user-defined function


# -----------module function ----------
# import math
# print(dir(math))
1
# from math import sqrt
# print(sqrt(5))
2
# from math import floor
# print (floor(16.6))

 
# ------- Syntax for  functions-----------------------
 
# def function_name (parameters):
  #  do something
  
  
  # question in function 
  
# def print_sum (first, second):
#   print(first*second)
# print_sum(5,6)






















