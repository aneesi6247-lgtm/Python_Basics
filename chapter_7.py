            ########  Files input and outputs  #######
            ##########################################
# python can be used to perform the operations on a file (read and write data)
# types of all files:
#1. Text files: .text, .docx, .log, etc.    # these files stores data in the form of charcters
#2. Binary files: .mp4, .mov, .png, .jpeg etc.

f = open("/Users/muhammad/Documents/Python/Folder_for_chapter_7/demo.txt", "r")  # first of all we have to open a file
#data = f.read()  # Then we will read the file 
#print(data)
#f.close()       # and its a good practice to close the file

line1 = f.readline()            # if we read the whole file first then the line command didn't work because the reading cursor 
                                # is at the end of the file already and it will output nothing thats why I comment out the upper program
line2 = f.readline()

print (line1)
print(line2)        

data=f.read()       
print(data)
f.close()

# now writing to a file
f = open("/Users/muhammad/Documents/Python/Folder_for_chapter_7/demo.txt", "w")  # open the file in the write mode
f.write(" I want to add this data into the file")  # this will erase all the previous data and add this one
f.close()

# appending in a file
f = open("/Users/muhammad/Documents/Python/Folder_for_chapter_7/demo.txt", "a") 
f.write("\nthis is the second line for append")  
f.close()   # this will add the data at the end of the existing file data

# if you dont have existing file and use the command w or a for writing or appending, it will automatically create a file
# f = open("new.txt", "w")   # you can try it by uncommenting it
# f.close()

f = open("/Users/muhammad/Documents/Python/Folder_for_chapter_7/demo.txt", "r+")
f.write("abc") # r+ command allows write and read in a file but not delete all the data once instead it overwrite the data one by one
f.close     # in this mode the pointer placed at the start of the file

f = open("/Users/muhammad/Documents/Python/Folder_for_chapter_7/demo.txt", "w+")
f.write("abc") # w+ command allows write and read in a file but delete all the data first from the file
f.close()

# in the r+ mode we also read and append the data but here the pointer state at the end fo file (no truncation)

##### with syntax #######


with open("/Users/muhammad/Documents/Python/Folder_for_chapter_7/demo.txt", "r") as f:
    data = f.read()
    print (data)    # no need to close the file in the with syntax because it automatically close the file at the end

## Deleting a file ###
# using the OS module   # module (is like a code library) is a file written by another programmer that generally has a functions we can use


# import os 
# os.remove("/Users/muhammad/Documents/Python/Folder_for_chapter_7/sample.txt")




##### practice questions ######

#1. make a python file and write the following data in it

f = open ("paractice_file.txt", "w")
f.write("Hi everyone. \n we are learning Fiel (I/O). \n using java \n in like programming in java")
f.close()
#2. now read all the data form the file and replace java with python

with open("paractice_file.txt", "r") as f:
    data = f.read()
    new_data = data.replace("java", "python")
    print (new_data)
with open("paractice_file.txt", "w") as f:
    f.write(new_data)

#3. now we have to figure out weather "learning" exist in our file or not

with open("paractice_file.txt", "r") as f:
    data = f.read()
    if data.find("learning"):
        print("found")
    else:
        print("not found")

##  other way
word = "alearning"
with open("paractice_file.txt", "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("found")
    else:
        print("not found")

#4. write a prgrame to find in which line of the file does the word "learning" occur first. print -1 if not found

def check_for_line():
    word = "python"
    line_numer = 1
    data = True
    f = open("paractice_file.txt","r")
    while data:
        data = f.readline()
        if (word in data):
            print(line_numer)
            return
        line_numer +=1

    return -1

print(check_for_line())

#5. from a file containing the numbers separated by the comma, find out the even numbers in it 

count = 0

with open("/Users/muhammad/Documents/Python/Folder_for_chapter_7/demo2.txt", "r") as f:
    data = f.read()
    print(data)
    nums = data.split(",")
    print(nums) 
    for val in nums:
        if (int(val) % 2 == 0):
            count +=1

print(count)
