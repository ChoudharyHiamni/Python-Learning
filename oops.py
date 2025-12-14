#OOPS:MAES CODE REUSABLE,ORGANIZED,MODULAR,SCALABLE

#CLASSS AND OBJECT
#CLASS:BLUEPRINT OR TEMPLATE OF AN OBJECT
#OBJECT:INSTANCE OF A CLASS


# class student:
#     name="John"      #  "attributes"

# s1=student()     #CREATING OBJECT
# print(s1.name)    #ACCESSING ATTRIBUTE OF CLASS USING OBJECT


#INSTANCE AND CLASS ATTRIBUTE
#CLASS ATTRITBUTE:ATTRIBUTE WHICH IS SHARED AMONG ALL THE OBJECTS OF A CLASS
#INSTANCE ATTRIBUTE:ATTRIBUTE WHICH IS UNIQUE TO EACH OBJECT

# class student:
#     school="abc"

#     def __init__(self):   #CONSTRUCTOR:IT IS A SPECIAL METHOD WHICH IS AUTOMATICALLY CALLED WHENEVER AN OBJECT IS CREATED
#         print(self)

# s1=student()

#SELF PARAMETER:IT IS A REFERENCE TO THE CURRENT INSTANCE OF THE CLASS.IT IS USED TO ACCESS VARIABLES THAT BELONG TO THE CLASS
#SELF JO OBJECT CALL KARTA HAI WO OBJECT KA REFERENCE PASS KARTA HAI
#SELF REFER TO CURRENT OBJECT AND IS USED TO ACCESS VARIABLES AND METHODS ASSOCIATED WITH THE CURRENT OBJECT



# class student:
#     school="abc"

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age


# s1=student("John",20)
# print(s1.name)
# print(s1.age)
# s2=student("Alice",22)
# print(s2.name)
# print(s2.age)


class student:
    school="abc"
      
    def hello(self):
        print("Hello students")

s1=student()
s1.hello()