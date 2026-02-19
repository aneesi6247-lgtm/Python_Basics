# Strings
str1= "i´m MUhammad. I´m 26 years old."
str2= "Im studying automotive engineeing"
str3 = str1 + str2
print(str3)
print(len(str3))
ch = str3[45: len(str3)]
print(ch)
print(str1.count("am"))
#exercise
str= input()
print(len(str))
print(str.count("m"))
#conditional statements
marks = int(input("enter your marks:"))
if (marks>=90):
    print("you got A grade")
elif(marks<90 and marks>80):
    print ("you got B grade")
elif(marks<80 and marks>70):
    print("you got C grade")
else:
    print ("you failed the exam")
#concept of nesting
age = int(input("enter your age:"))
if (age >=18):
    if (age >90):
        print( "sorry you can't drive")
    else:
        print ("you can drive")
else:
    print("sorry you can't drive")
print ("end of program")
#exercise of chapter2
# first: write a program to check if the number is even or odd
num=int(input("enter your number:"))
num1= num%2
if (num1==0):
    print("EVEN NUMBER")
else:
    print("ODD NUMBER")

# second: write a program to find the gratest of 3 numbers entered by the user
val=int(input("first number"))
val1=int(input("second number"))
val2=int(input("third number"))
val3=int(input("fourth number"))
if ( val>val1 and val1>val2):
    print("first values if greater")
elif( val1>val and val1>val2):
    print("second number is greater")
elif (val2>val and val2>val1):
    print("third value is greater")
else:
    print("end of program")

#another short way
if (val>val1 and val>val2):
    print("first values if greater")
elif (val1>val2):
    print("second number is greater")
else:
    print("third value is greater")
#For four values
if (val>val1 and val>val2 and val>val3):
    print("first value is the biggest one")
elif(val1>val2 and val1>val3):
    print("Second value is the biggest one")
elif(val2>val3):
    print("third value is biggest")
else:
    print("fourht value is the biggest")