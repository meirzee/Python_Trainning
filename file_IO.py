#File I/O
import string;

print ("Following lines will copy file one to file 2 using user input instructions :")

print ("Welcom !! \n please specify source file: ")
f1 = input()

print ("Please specify target file: ") 
f2 = input()

open(f2 , 'w').write(open(f1 , 'r').read())

# this syntax will work too:  open(f2,'w').write(open(f1).read())
