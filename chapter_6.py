                        #### Functions and Recursions  #####
                        ####################################
# Block of statements that perform a specific task.
# def func_name(parmeter1, parameter2).    This is called function defination 
# func_name(avg1, avg2).    this is called function calling with arguments
#1. write a function who can calculate the average of three numbers 
def func_average(a, b, c):
    avg = a+b+c
    return avg
out = func_average (10, 13, 14)
print(out)
                                # identation means proper spacing in the coding

# Build in functions i.g print(), len(), type(), range()
# user defined functions are the one which defined by the users

# Default parameters
# Assigning a default value to parameter, which is used when no argument is passed. 
def func_multi(a=2, b= 7):
    mul = a*b
    return mul
mulplication = func_multi (14, 10)
print(mulplication)

# practice questions 
#1. write a programe to find the length of the list
num = [12, 12,434, 4324,23445, 234214,353,24214,124,214]
names= ["MUHAMMAD","hassan","awais"]
def cal_len(list):
    print(len(list))

cal_len(num)
cal_len(names)

#2. write a programe to print the numbers of elements of a list in a single line 

def ele_pri(list):
    for items in list:
        print (items, end =" ")
ele_pri(num)
    
#3.write a progeme to find the factorial of any number
def fac_num():
    factorial = 1
    numer = int(input("enter the number: "))
    for n in range (numer, 1, -1):
        factorial = factorial * n
    return factorial
print(fac_num())
        
#3. write a function to convert euro to pkr
def eur_pak(a):
    pak = a * 330
    print( "pakstni amount ist = ", pak)

eur_pak(100)

#4. write to program to find out weather the number is odd or even

def odd_even(b):
    if b%2==0:
        print("the number is even")
    else:
        print("the number is odd")

odd_even(15)

            #### Recursions ###
# when a function calls itself repeatedly
# recursive function 
def show(i):
    if (i==0):   # Base case
        return
    print(i)
    show(i-1)       # recrusion 
show(10)


def show(i):
    if (i==0):   
        return
    print(i)
    show(i-1) 
    print("end")        # if we add a any other statement here it will also run as many times as many times the function calls due to the fact of call stack in which
                        # first layers all build for each funcition calling and then delete it accordingly     
show(10)

#1. to find out the factorial of any number
def fac(q):
    if (q == 0 or q== 1):
        return 1
    else:
        return (fac(q-1)*q)
print(fac(5))

## Exercise Questions ##
#1. write a recursion function to calcluate the sum of the first natural numbers
def add(n):
    if (n==0):
        return 0
    return add(n-1) + n # each time calculate the sum of previous number and then add it to to the n as followed by the call stack, check on handbook for more clarity
print(add(8))

#2. write a recursive function to print all the entries of a list
def list_name(list,indx):
    if (indx == len(list)):
        return
    print (list[indx])
    list_name (list, indx +1)
    
list = [1, 2 ,3 ,2, 432, 523]
list_name(list,0)