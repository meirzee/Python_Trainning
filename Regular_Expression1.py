#Regular Expressions
# In order to use Regular Expressions we need to import the "re" module

import re

# Searching for a match string:
reg1 = re.compile('meirz') # this will return a compiled string pattern object (abcdefg) and keep it in variable name reg1 and it is loaded to the memory
reg2 = reg1.match('meirz') # on this line we actually asked the system to check if there is such an object on the system memory it returns a match output (it is case sensetive)

print (reg2.group() ) # will print meir
print (reg2.match('meirz').group )



# trying a different string object wich does not exists will return "None"
print (reg1.match('kkdd'))


