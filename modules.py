# Modules

import sys
import os

#in order to see all the functions that the module contains we can typ:
all_functions = dir(sys)
for i in all_functions:
    print (i)


print ("The sys path is: \n\n", sys.path)
print( "\n \n Version is : " , sys.version, "\n\n\n")


print ("The os module functions are: \n\n ", dir(os) )
