                            ## LOOPS ##
# loops are used to repeat the instructions untill the condition is true

    
                        ## while loop ##

num = 1     # this variable is called iterator and the repeation process called iterations
while num<=8:
    print("while condtion is active")
    num +=1
print(num)

# practice questions
#1. print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i +=1
print("End of program")
#2.print numbers from 100 to 0
b = 100
while b>=1:
    print(b)
    b -= 1
print("edn of program")

#3. print a multiplication of number n
t = 1
val = int(input("enter the value: "))
while t<=10:
    print(t*val)
    t +=1
print (" the table of your number", val, "is creaeted")

# 4. print the index of the following list using the loop 

list = [2,4,9,16,25,36,49,64,81,100]
k = 0
while k <= len(list)-1:
    print(list[k])
    k += 1
print(" end of qeustion 4")

# search for a number x in a tuple with the help of loop
tuple = (2,4,9,16,25,36,49,64,81,100)
inp = int(input("enter to number to match"))
j=0
while j < len(tuple):
    if (inp == tuple[j]):
        print( " your number is matched")
        
    j += 1

# Contines and Break commands in Loops
a = 1
while a <= 10:
    if (a==3):
        break # ends the loop wher the condition met
    print(a)
    a += 1
while a <= 10:
    if (a==3):
        a += 1
        continue # skip the programe onwards in the while loop when the conditon met and go for next iteration
    print(a)
    a += 1
    
    #print all odd and even numbers form 1 to 10
    c = 0
    while c<= 10:
        if (c%2==0):  #print even number, if we type not equall then it result in odd number (c%2!==0)
           print(c)
        c += 1

                             ##FOR LOOP  ##
                             ###############
#for loops are used for the sequential traversal. For traversin list, stirng, tuples etc. 
abc = (12, 34, 34, 53, 53)
for val in abc:    # for loop is mostly used for when we have a sequential data and we want to traverse on each entry
    print(val)

# practice questions
#1. print all even numbers from 1 to 100 using for loop
cba = [0,2,4,16,25,36,49,64,81,100] 
for el in cba:
    print(el)
#2. figure out a specific number in the listing using for loop
x = 100
l = 0
for el in cba:
    if el == x:
        print("number found" ,l)
        break
    l += 1
    # Here in the practice questions we proform the linear search to get the values 


            ## Range() function
            ###################
#Range funtions retruns the sequence of numbers starting from 0 by default and increament by 1 (by default) and 
#stops befor the specified number. you can also add the step. range (start, stop, step)
for i in range(10): # stop number is not included in the output. stop is compulosry in the range but start and step are optional
    print(i)

for i in range (5,15):
    print(i)

for i in range (5,19,3): #with step
    print(i)

#practice questions 
#1. print nubmers from the 1 to 100 with range fuction
for a in range(100):
    print(a)
#2.now print from 1oo to 1 
for a in range(100, 0, -1):
    print(a)
#3. print the multiplication of any number
t = 3
for a in range(11):
    print(t*a)

### pass statemen ###
#pass is a null statement that does nothing. It is used as a placholder for future code. 
for y in range(5):
    pass        # this loop do nothing just skip it

# practice Question
#1. find the sum of the natural numbers using while
i = 1
sum = 0
while i<= 10:
    sum = sum +i
    i +=1
print (sum)

#2. write a program to find the factorial of any user defined natural number
num = int(input("enter the number for factorial: "))
factorial = 1
for i in range(num,0,-1):
    factorial = factorial*i
print("factorial is =", factorial)


