# print("Hello")
# print(("hello" + "\n") *10)

# VARIABLES IS CONTAINER TO STORE DATA.Python is dynamically typed → no need to declare type.
# Variable names must start with a letter or underscore, followed by letters, numbers, or underscores.
# Variable names are case-sensitive and cannot be Python reserved keywords.

      #TAKING USER INPUT 
#INPUT FUNCTION ALWAYS RETURNS A STRING
# name= input("Enter your name:")
# print("Hello" , name)

# Expression : COMBINATION OF OPERATORS AND OPERANDS
# Statement : COMPLETE LINE OF CODE THAT PERFORMS A SPECIFIC TASK

#INDENTATION : PYTHON USES INDENTATION TO DEFINE BLOCKS OF CODE.

                        #DATA TYPES:int,float,str,bool,list,tuple,set,dict
# x=10
# print(type(x))


                        #PROGRAM TO TAKE DIAMETER AS INPUT AND CALUCLATE AREA OF CIRCLE
# diameter=input("Enter diameter of circle:")
# radius= float(diameter)/2
# area=3.14*(radius**2)   #** IS EXPONENTIATION OPERATOR
# print("Area of circle is:" ,area)

#KEYWORDS : RESERVED WORDS IN PYTHON THAT HAVE SPECIAL MEANING
#EXAMPLES: if, else, elif, while, for, def, return, import, as, from, class, try, except, finally, with, lambda, pass, break, continue, global, nonlocal, assert, yield, raise, in, is, and, or, not

#COMMENTS : SINGLE LINE COMMENTS START WITH # , MULTI LINE COMMENTS USE TRIPLE QUOTES (''' ''')

                              #TYPE CONVERSION :IMPLICIT AND EXPLICIT
                         #IMPLICIT TYPE CONVERSION : AUTOMATICALLY DONE BY PYTHON
# x=10      #int
# y=2.5     #float
# z=x+y    #int + float = float
# print(z)
# print(type(z))

                        #EXPLICIT TYPE CONVERSION : MANUALLY DONE BY PROGRAMMER
# a="100"
# b=int(a)   #str to int
# print(b)
# print(type(b))

# c= float(a)  #str to float
# print(c)

#operators : arithmetic, comparison, logical, assignment, bitwise, membership, identity
#ARITHMETIC OPERATORS : +, -, *, /, %, **, //
#COMPARISON OPERATORS : ==, !=, >, <, >=, <=
#LOGICAL OPERATORS : and, or, not
#ASSIGNMENT OPERATORS : =, +=, -=, *=, /=, %=, **=, //=
#BITWISE OPERATORS : &, |, ^, ~, <<, >>, >>
#MEMBERSHIP OPERATORS : in, not in
#IDENTITY OPERATORS : is, is not


                              #STRING
# str1="Hello world"
# str2='Hello'
# str3='''hello '''
# print(str1)
# print(str2)
# print(str3)

# s1=input("Enter your name:")
# print(s1[0])
# print(s1[-1])
# print(len(s1))

                            #STRING SLICING

# sr="Choudhary"
# print(sr[0:5])
# print(sr[::-1])
# print(sr[::2])
# print(sr[2:])


# print(sr.upper())
# print(sr.lower())
# print(sr.replace("Chou","Shri"))
# print(sr.split("u"))
# print(sr.find("d"))
# print(sr.startswith("C"))
# print(sr.endswith("y"))

                        #   CONDITIONAL STATEMNETS
# age=int(input("Enter your age:"))
# if age<18:
#     print("You can't vote")
# else:
#     print("You can vote")


# age = 18
# if age >= 18:
#     print("Adult")
# elif age == 17:
#     print("Almost there")
# else:
#     print("Minor")


                      #LISTS : ORDERED, MUTABLE, ALLOW DUPLICATES
# marks=[85,90,78,92,51,23,16,18]
# print(marks)
# print(len(marks))
# print(marks[0])
# print(marks[4])
# print(marks[1:4])
# print(marks[:3])
# print(marks[3:])
# marks[2]=100
# print(marks)
# marks.append(75)  #ADDING ELEMENT AT END
# print(marks)
# marks.sort()
# print(marks)
# marks.pop(3)
# print(marks)
# marks.remove(51)
# print(marks)

                                    #TUPLES : ORDERED, IMMUTABLE, ALLOW DUPLICATES
# tuple1=(10,20,30,40,50)
# print(tuple1)
# print(tuple1[0])
# print(tuple1[2:4])
# # tuple1[1]=25  #ERROR: TUPLES ARE IMMUTABLE
# print(len(tuple1))

# singleTuple=(100,)  #SINGLE ELEMENT TUPLE
# print(type(singleTuple)) # <class 'tuple'>
# notTuple=(200)   #NOT A TUPLE
# print(type(notTuple))  #<class 'int'>

                                  #DICTIONARY : UNORDERED, MUTABLE, KEY-VALUE PAIRS
                              #KEYS ARE ALWAYS UNIQUE
# student={
#     "name":"John",
#     "age":20,
#     "courses":["Math,Science,English"],
#     "name":"Doe"  #DUPLICATE KEY, LAST ONE WILL OVERRIDE
# }
# print(student)
# print(student["name"])
# print(student.get("age"))
# student["age"]=21
# print(student)
# student["grade"]="A"
# print(student)
# print(student)
# print(student.keys())
# print(student.values())
# print(student.items()) #KEY-VALUE PAIRS AS TUPLES IN A LIST
# print(len(student))
# print(student.get("name"))


                                    #SET : UNORDERED, MUTABLE, UNIQUE ELEMENTS
# mySet={10,20,30,40,50,10,20}  #DUPLICATES WILL BE REMOVED
# print(mySet)
# mySet.add(60)  #ADDING ELEMENT
# print(mySet)
# mySet.remove(30)  #REMOVING ELEMENT
# print(mySet)


# empty_set=set()  #TO CREATE AN EMPTY SET
# print(type(empty_set))  #<class 'set'>

#  #HOW TO CONVERT LIST INTO SET
# myList=[1,2,2,3,4,4,5]
# mySetFromList=set(myList)
# print(mySetFromList)  #OUTPUT: {1, 2, 3, 4, 5}


                                      #LOOPS : FOR AND WHILE
# num=1
# while num<=5:
#     print("Himani Choudhary")
#     num+=1

# j=10
# while j>=1:
#       print(j)
#       j-=1

# n=1
# while n<=10:
#     if n%2==0:
#         print(n)
#     n+=1
    

                    #SUM OF FIRST N NATURAL NUMBERS
# n=5
# sum=0
# while n>0:
#     sum+=n
#     n-=1
# print("Sum is:",sum)

                 #PROGRAM TO PRINT STAR PATTERN
# n=1
# while n<=5:
#     print("*" * n)
#     n+=1
                    
                        #PROGRAM TO PRINT TABLE OF A NUMBER
# num=int(input("Enter a number:"))
# i=1
# while i<=10:
#     print( num, "*" , i , "=" ,num * i)
#     i+=1

                            #FOR LOOP
# list1=[10,20,30,40,50]
# for item in list1:
#     print(item)

# for i in range(1,10,2):
#     print(i)

# for i in range(2,21,2):
#     print(i)

                  #PROGRAM TO PRINT SQUARE OF A NUMBER
# for i in range(1,11):
#     print(i**2)

                        #BREAK CONTINUE AND PASS
# for i in range(1,11):
#     if i==5:
#          break
#     print(i)

# for j in range(1,11):
#      if j==5:
#          continue
#      print(j)
          
                              #START DEFAULT VALUE IS 0 , END DEFAULT VALUE IS 1,END VALUE IS EXCLUSIVE
# for k in range(5):
#     print(k)

# import time
# count=int(input("Enter a number:"))
# for i in range(count,0,-1):
#     print(i)
#     time.sleep(1)

# print("Boom")

                        #PASS STATEMENT : USED AS A PLACEHOLDER, DOES NOTHING,WHEN WE NEED A STATEMENT SYNTAX BUT NO OPERATION IS REQUIRED


                               #FUNCTIONS: BLOCK OF CODE THAT PERFORMS A SPECIFIC TASK
# def sum():
#     a=4
#     b=5
#     sum=a+b
#     print(sum)
# sum()
# sum()
# sum()

def greet(name,age):
    print(f"{name} is {age} years old")
greet("Himani",21)


