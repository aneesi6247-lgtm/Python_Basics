                    ##########################################
                    ## OBJECT ORIENTED PROGRAMMING (PART 2) ##

# delete keyword 
# used to delete the object properties or object itself. 

class student:
    def __init__(self, name):
        self.name = name
        print (self.name)

s1 = student ("anees")
print(s1)
del s1 # now i cann't print the s1 anymore

    
## Private attributes and methods
# Conceptual implementation in python, private attribues and methods are meant to be used within the class 
# and are not accessible from outside the class. we used double underscore it the begining to make it private

class person:
    def __init__(self, name):
        self.name = name
        pass
    #def __hello(self):    # this function cannot be called out from outside the class because it has two 
       # print("hello")     # undersocre the begining but it can be called within the class
s2 = person ("anees")
#s2.__hello()                # this will give an error


### Inheritance ###
# when one class (child/derived) derives the peroperties and methods of another class (parent/base).

class car:
    color = "blue"
    def start (self):
        print("car is started")
    def stop (self):
        print("car is stopped")

class mercedes_car (car):
    def __init__(self):
        print ("object is created")
        
s2 = mercedes_car()
print (s2.color) 
s2.start()

# TYPES OF inheritances#
# 1. single inheritance = there is one parent class and one child class 
#2. muli_level Inheritance = where properties of one class inhereite to the multiple classes  for example

class benz(mercedes_car):
    def __init__(self, cartype):
        self.cartype = cartype
        print("this is multi level inheritance")

b1 = benz("diesel")
print (b1.cartype)
print (b1.color)

#3. Multiple Inheritance = when we inherit the properties of multiple classes into one for example

class hybrid(benz, mercedes_car):
    def __init__(self):
        print( " this is the example of multiple inheritances")

h1 = hybrid()
h1.stop()

## Super method
# super method is used to access the methods of the parent class

class car1:
    color = "blue"
    def __init__(self, type):
        self.type = type
        print(type)
        pass
    def start (self):
        print("car is started")
    def stop (self):
        print("car is stopped")

class mercedes_car (car1):
    def __init__(self):
        print ("object is created")
        super().__init__(type)
        
c3 = mercedes_car()
c3.type

### CLASS METHODS ###
# static method can't acess or modify class state or attribute and generally for utility. 
# A class method is bound to the class and receives the class as an implicit first argument

class newcar:
    carcolor = "blue"
    def __init__(self):
        print ("for methods")
    @classmethod
    def chnagecolor(cls, color):
        cls.carcolor = color        # this will change the attribute of the class
toyota = newcar()
toyota.chnagecolor("red")
print(toyota.carcolor)
print(toyota.carcolor)

                                            ## Property ##
# we used the @property decorator on any method in the class to use the method as a property. 
# In simple words when one instance change in the class then it will automatically change the value in property.
# if it does't define in the property then the percentage remain unchanged as shown in the below example

class student:
    def marks(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = (self.phy + self.chem + self.math)/3 

st = student()
st.marks(34, 35, 23)
print(st.percentage)
st.chem = 43        # this will change the value in chem but not in the percentage value will be same
print(st.chem)
print (st.percentage) # this is the same so we need to make the percentage as property to change it as welll.

## again

class student1:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
    @property
    def prc(self):
        return str ((self.phy + self.chem + self.math) / 3)

stu = student1 (12,43,56)
print(stu.prc)
stu.math = 45
print(stu.prc)          # now when prc is an property it will directly change the prcentage when you change the instance of the function


########  Polymorphism: Operator Overloading    #######
# When the same operator is allowed to have different mearning according to the context. 

print(2+3)                              # here plus opertor is simply used to add the numbers
print("muhamamd" + "Anees")             # here plus opertor is used for concatenating
print([23, 353, 324] + [23, 234,234])   # here Plus operator is used for merging two lists

            #### Operators and Dunder Functions   ###

class complex():
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def shownumber(self):
        print(self.real, "i", + self.img, "j")
    def add (self, n2):
        realpart = self.real + n2.real
        imgpart = self.img + n2.img
        return complex (realpart, imgpart)
        #print(realpart,"i",+ imgpart, "j" )
    

n1 = complex(4, 5)
n1.shownumber()
n2 = complex (6,3)
n2.shownumber()
n3 = n1.add(n2)
n3.shownumber()

# but if we simply try to add two number it will show an error because we didn't define the plus or minus role in our class

# num3 = n1 + n2

# to tackle these issues we used Dunders functions 

class complex1():
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def shownumber(self):
        print(self.real, "i", + self.img, "j")
    def __add__(self, n2):
        realpart = self.real + n2.real
        imgpart = self.img + n2.img
        return complex (realpart, imgpart)
        #print(realpart,"i",+ imgpart, "j" )
    def __sub__(self, n2):
        realpart = self.real - n2.real
        imgpart = self.img + n2.img
        return complex (realpart, imgpart)
    

n1 = complex1(4, 5)
n1.shownumber()
n2 = complex1(6,3)
n2.shownumber()
num3 = n1 + n2
num3.shownumber()
num4 = n1 - num3
num4.shownumber()

# so here we used the dunder functions for the addition and substration thats why there is no error and we simply add two complex numbers
# in python there are a lot of dunder functions which are used to perform differnt kinds of operations in the certain class

####### Practice Questions #######

# 1.1 define a circle class to create a circle wiht radius r using the constructor
# 1.1 define the an area method of the class which calculates the area of the circle
# 1.2 define a perimeter() method of the class which allows you to calculate the perimeter of the class

class circle():
    def __init__(self, radius):
        self.radius = radius
    def areaofcircle(self):
        area= 3.14 * self.radius * self.radius
        return area
    def perimeterofcircle(self):
        perimeter= 2*3.14*self.radius
        return perimeter
    
c1 = circle(15)
Cicrle = c1.areaofcircle()
print(Cicrle)
print(c1.perimeterofcircle())

#2.     Define a employee class with the attribute role, department, and salary. This class should contain a showdetails method
#2.1    Define a engineer class that inherit property from Employee 

class Employee():
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    def showdetails(self):
        print("The role of the peroson is ",self.role)
        print("The person belongs to the ", self.department, "department")
        print("The salary of the person is ",self.salary)

emp1 = Employee("developer", "Programming", 150000)
emp1.showdetails()

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def additionaldetails(self):
        emp1.showdetails()                  # or we can use super command here to call the constructor and add the details in __int__ constructor
                                                #super().__init__("engineer", "IT", 340000)
        print ("The name of the person is ", self.name)
        print("The age of the person is ", self.age)

eng = Engineer ("anees", 27)
eng.additionaldetails()

# 3. creat a class called order which stores items and its price. use dunder function __gt__() to convey that order1 > order2 if price of order1 > Price of order2

class order():
    def __init__(self, item, price):
        self.item = item
        self.price = price 
    def __gt__(self,ord2):
        return self.price > ord2.price
ord1 = order("chips", 20)
ord2 = order("candy", 4)
print(ord1>ord2)