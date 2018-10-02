#File I/O
import string;

print ("Following lines will copy file one to file 2 using user input instructions :")

print ("Welcom !! \n please specify source file: ")
f1 = input()

print ("Please specify target file: ") 
f2 = input()

open(f2 , 'w').write(open(f1 , 'r').read())

# this syntax will work too:  open(f2,'w').write(open(f1).read())

# if we want to append to the file we need to change the command to append mode "a"
#open(f2, 'a').write('\n')
open(f2 , 'a').write(open(f1 , 'r').read())
#open(f2, 'a').write('\n')
open(f2 , 'a').write(open(f1 , 'r').read())


#in order to open a filw to read and write:
#open(file_name, 'r+')
