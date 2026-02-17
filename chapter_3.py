#lists in Python
cus = ["anees", 10, 20, "hassan"]
print(cus[2])
print(cus)
cus[0]= "ali" # the strings are mutable in the lists
print(cus)


#LIST SLICING 
marks = [5,65,65,63,34,345,643,34]
print(marks[2:5])
print(marks[:3])
print(marks[3:])
print(marks[-1:-3])


#LISTS METHODS/Commands
marks.append(25)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
marks.insert(4, 7)
print(marks)
marks.remove(7)
print (marks)
marks.pop(5)
print(marks)

# TUPLES IN PYTHON

tup = (34,23,34,54,85,34,34,23) #tuples are immutable
print (tup[2:4])

#Methods in tuples
print(tup.index(34))
print(tup.count(34))

#PRACICE QUESTIONS
#1. write a programe to ask the user to enter names of four favourite movies and store them in a list
movie1= input("Enter the name of your first favourite movie:")
movie2= input("Enter the name of your second favourite movie")
movie3= input("Enter the name of your second favourite movie")
cus_input = [movie1, movie2, movie3]
print(cus_input)
print (cus_input[2])

#other technique
movies=[]
movies.append(input("enter your first movie"))
movies.append(input("enter your second movie"))
movies.append(input("enter your third movies"))
print(movies)

#2. write a programe to check if a list contain a palindrome of elements. (hint, use copy() method)
# paleindromic values or words means that they will be same when we read it form forward or backward
list1 = [1,2,3,2,1]
list2 = [1,2,4]
first_list=list1.copy()
second_list=list2.copy()
first_list.reverse()
second_list.reverse()
if (list1 == first_list):
    print("the values are palidrome")
else:
    print(" the values are not palindrome")
if (list2 == second_list):
    print("the values are palidrome")
else:
    print(" the values are not palindrome")

#write a programe to find the number of students with the grade "A" in the following tupple.
tup = ("C","D", "D", "E", "A", "G", "S", "A", "D", "A")
print(tup.count("A"))

# create a list and sort it in the decending order

list = ["C","D", "D", "E", "A", "G", "S", "A", "D", "A"]
list.sort()
print(list)
