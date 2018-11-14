#Regular Expressions
# In order to use Regular Expressions we need to import the "re" module

import re

print ("\n Following are the Regular expressions method:")
RE_METHODS = (dir(re))
for i in RE_METHODS:
    print (i)
print ("######################################################## \n")


# Searching for a match string a pattern:
reg1 = re.compile('meirz') # This will compile string pattern and turn it to object (meirz) and keep its memory location on variable name reg1
reg2 = reg1.match('meirz') # on this line we actually asked the system to check if there is such an object on the system memory it returns a match output (it is case sensetive)

print ("1.Following line will point to the memory location of meirz object if we have a match on reg2 variable: ")
print (reg2 ) 

print ("2.Following line will print the object meirz the Group method will expose it rather then just indicate if there is a match: ")
print (reg2.group() ) 

print ("\n 3. Following is a different way of checking if meirz exists on memory:")
print (reg1.match('meirz').group() )

print ("\n 4. Following line will return match since meir exists in memory:")
print (reg1.match('meirz') )

print ("\n 5. Following command will return \"None\" since this object does not exists:")
print (reg1.match('kkdd'))


