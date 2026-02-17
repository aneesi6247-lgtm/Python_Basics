## DICTIONARIES IN PYTHON  ##
dic = {
    "name" : "anees", # here name is key and anees is a vlue
    "age" : "27",     # here age is key while 27 is a value
    "top" : (1,3),
    "list" : [56, 532],
}
print(dic)
print(dic["age"])
dic["name"] = "Muhammd" #the dictionaries can be changed or assigned new values
print(dic)
# nesting in the dictionaries
dic1 = {
    "name" : "muhammadanees",
    "marks": {
        "phy" : 15,
        "chem" : 34,
    }
}
print(dic1["marks"])
print(dic1["marks"]["chem"])

# METHODS in the Dictionaries
print(dic1.keys()) # returns all the keys of the dictionery
print(list(dic1.keys())) # make the list of the dictionery
print(len(dic1)) # prints the length of the dictionery 

print(dic1.values()) # print all the values of the dictionery 
print(list(dic1.values())) # to make a list of all the values

print(dic1.items()) #returns all the key and values in the form of tuples

print(dic1.get("name")) # here we can also used the simple print command to print out the values of name but the problem is
                        # that if I mistakely write a wrong key that gives an error, and the error means the program below that will not run
                        # instead this command simply returns the NONE vaue in the output if the key is wrong so It will not interupt the program

dic1.update({"city" : "chakwal"}) # to add any new value in the dictionery
print(dic1)

new_dic = {"Village" : "Maswal"}
dic1.update(new_dic)
print(dic1)

## SETS IN PYTHON ##
# sets are the collection of the unordered items. Each element in the set must be unique and immutable. 
# set itself is mutable but the values are not

num = {1, 2, 3}
print(type(num))

ary ={1, 2, 3, 4, 2, 1,3, "hello", "hello"}
print (ary) # set ignoes the repeated values

null_set = set() # null set syntex 
print(null_set)

# Methods in the sets
null_set.add(5) # add an element in the set
null_set.add(10)
null_set.add("hell0")
null_set.add(78)
print(null_set)

null_set.remove(10) # remove elements in the set
print(null_set)

null_set.clear() # clear the set
print(null_set)

null_set.add(5) # add an element in the set
null_set.add(10)
null_set.add("hell0")
null_set.add(78)

print(null_set.pop()) #pop up the random value from the set
print(null_set.pop())

print(ary.union(null_set)) # combiines both sets values and return new
print(ary.intersection(null_set)) # combines common values and return new


# exercise
#1. make a dictionery and store follwoing meanings 
exe_dic = {
    "table" : ["A peice of furniture","list of contents or figures"],
    "cat" : "a small element",
    
}
print(exe_dic)
exe_dic.update({"name" : "anees"})
print(exe_dic)

# find the number of class rooms required for each subject 
set= {"java", "python", "C++", "java", "C", "python", "C++","C"}
print(len(set)) # provide the unique values in the set
print(type(set))

# write a program to enter the values of three subjects from the user and enter them in the dictionery 
phy = int(input("Enter the marks of physics "))
chem = int(input("Enter the marks of chemistry "))
math = int(input("Enter the marks of maths "))
marks_dic = {
    "Physics" : phy,
    "chemistry" : chem,
    "matematics" : math,
}

print(marks_dic)
emp_dic= {}         # you can also make a embty dictionery and then update it accordingly
emp_dic.update({"chem": chem})
print(emp_dic)

# figure out a way to store 9 and 9.0 separetely
exe = { 9, "9.0"}   # the first way is to store one values in the form of string
print(exe)
exe.update({("int",9),(float, 9.0)}) # we can also store in the form of tuples
print(exe)
