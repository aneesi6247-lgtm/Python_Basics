                #### OPPS : OBJECT ORIENTED PROGRAMMING. ####
# to map with the read world problems/scenarious, we started using objects in cods

# class is a blue print for creating objects
class student:
    name = "anees"
    unterricht = "automotive"

# creating objects/instances

s1 = student()
print(s1.unterricht)

# __int__Function
# CONSTRUCTOR
# All clases have a function called __int__(), which is always executed wehen the object is being initiated. 

class names:
    name = "anees"
    def __init__(self):
        print("Im executed because anywehere creat an object")

muhammad = names() ### here self and muhammad are basically the same things

class new:
    def __init__(self, name, marks):    # This is called a paramatrized constructor the constuctor with only "self" attribute is called dafult constructor.
        self.name = name                
        self.marks = marks
        print("adding a new student in the database")

s2= new("anees","45")
print(s2.name, s2.marks)

#   1. what we have same for example "college name" for all the students. we only store at once and we need to write it before the consturctor
#   so that it cannot used space every time when a new object is created. 
#   2. when we have same class and object attribute, then the object attribute will alwas excute because of its higher periority

class new1:
    college_name = "wings"          # these are called class attributes
    name = "ananomous"
    def __init__(self, name, marks):    #
        self.marks = marks                  ## these are called object attributes
        self.name = name
        print("adding a new student in the database")

s3= new1("anees","45")
print(s3.name, s2.marks)

##### Methods #####
###   Methods are the functions that belongs to the objects  #####

class student:
    college_name1 = "wings"

    def __init__(self, name, marks):
        self.name = name
        self.marks= marks
    def rol(self, intk):   # these functions that belongs to the objects are called methods
        self.intk = intk
        return intk
    
s4 = student ("anees", 97)
s5 =s4.rol(342423)
print (s5)

## practice question ##
# create a student class that takes names and marks of 3 subjects as an argument in the constructor, then create a method to print the average.

class student_subjects:

    def __init__(self, sub1, sub2, sub3, mark1, mark2, mark3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    def average (self):
        avg = (self.mark1 + self.mark2 + self.mark3)/3
        return avg
    
stu = student_subjects ("math", "chem", "phy", 12, 14, 15)
avge = stu.average ()
print(avge)

## second way 
class student_new:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def average (self):
        sum = 0
        for val in self.marks:
            sum += val
            avgre = sum /3
        return avgre

gu = student_new("hassan", [13, 15, 123])
avgre = gu.average ()
print (avgre)

## Static methods ##
# Methods that don't use the self parameter (works at the class level)

class new:
    @staticmethod               ## decorator 
    def college ():
        print("hello")

b1 = new
b1.college()

## IMPORTANT THINGS ##

                                        ## Abstraction ##
# Hiding the implementation details of a class and only showing the essential features to the user. 
# for examples in the above examples a lot of things are happing in the class but when we make an object and get the output we get only necessary output.
# so basically we hide all the unnecessary details from the user

                                        ## Encapsulation ##
# wraping data and functions into a single unit (object) is called encapsulation.
# what we do above in all classes is basically called Encapsulation.



## practice Question
#1. write a programe in which create an account class with 2 attributes - balance and acc. number
# also creats the methods to debit, credit and print the balance.

class account_number:
    def __init__(self, balc, accnum):
        self.balc = balc
        self.accnum = accnum
    def debit(self, amount):
        self.balc -= amount
        print("the amount of ", amount, " is debited")
        print (" the remaining balance is ", self.balc)
    def credit(self, amount):
        self.balc += amount
        print("the amount of ", amount, " is creadited")
        print (" the remaining balance is", self.balc)

acc = account_number(5000, 123456)
acc.debit(400)
acc.credit(700)