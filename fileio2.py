import string;


#FileIO2.py - read from a file

''' open file excepts two arguments file name and the mode following are the possible modes: 
read = r 
read binary files = rb 
write = w
write to a binary file = wb
append = a

'''



#The readline function reads the first line and stops when it encounter the new line \n it stors it or displays it as a string
print (" ##############################   Executing readlines ########################################## \n ")
readMe = open('datafile1.py' ,"r").readlines()
print(type(readMe)) # show details about type of the readMe variable
print(readMe) 

#The readlines function reads all the lines of a file one by one as list elements (output will contain the \n charecter).
#print (" ##############################   Executing readline ########################################## \n ")
#print (readMe.readlines() ) 

#The read function read the complete file and store it as a string into variable name readMe
print (" ##############################   Executing read ########################################## \n ")
readMe = open('datafile1.py' ,"r").read()
print(readMe)
print (type(readMe))



print ("########################### OPenning file for writing ###############################")

mytext = "This is sample file for testing some python commands"
savefile = open('examplefile.txt', 'w').write(mytext)

readMe2 = open('examplefile.txt' ,'r').read()
print ("Following is the content of readM2 file: ")
print(readMe2)


print ("########################### OPenning file for writing and copy one file content to a nother ###############################")

mytext2 = open('file_to_copy.txt' , 'r').read()
savefile2 = open('copied_file.txt', 'w').write(mytext2)

print ("Following is the content of readM3 file: ")
print (open('copied_file.txt' ,'r').read())

print ("########################### Openning file for writing and copy one file content to a nother with less code lines ###############################")

print ("Following is the content of copied_file2 file: ")
open('copied_file2.txt', 'w').write(open('file_to_copy.txt' , 'r').read())  #reads file file_to_copy.txt and copy it to copied_file2.txt file overwrite mode if it doesnt exist python will creat the file.
print (open('copied_file.txt' ,'r').read())


print ("########################### Openning file for writing using append mode ###############################")
appendMe = "\nThis is the line to be apended to copied_file2 file "
appendFile = open('copied_file2.txt', 'a')
appendFile.write(appendMe)
appendFile.write("\nYou can append text manually too")
print ("The copied_file2.txt file is under C:/Users/\meirzee/\Desktop/\GitHub/\Python_Trainning" )

#Appendind directly to a file without openning the content to a variable first.
open('copied_file.txt', 'a').write("\nApending directlly to a file...")