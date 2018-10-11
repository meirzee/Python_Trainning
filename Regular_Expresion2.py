#Regular_Expresion2.py
#
# Using Metacharecters:
#  ^  carote this specify that we are looking for a string that starts with specific char 
#  $  dollar sign for catching the end of a string
#  .  will match any char except new line once meanning it will return the first char it match from the start of the string
#  *  will match any char except new line and will continue to search the string from start to end
#  +  will return a match of the next char
#  [a-z] specifying range
#  [A-Z] specifying range of capital letters
#  \s  searches for space - can not be used in the [] sign
#  \S  searches for non spaces strings
#  \d searches for digits
#  w\ searches for a-zA-z0-9 _
#  W\ ignore a-zA-z0-9 _ 
#  ignore specific chars, for example ignor chars a up to g: [^a-g]
# Lets say we are looking for 
#

import re

#Regular expresion is case sensetive but we can ask it to ignore case function IGNORCASE
reg1 = re.compile('meirzee', re.IGNORECASE)

print ("\n 1. Checking if it returns the object as match:")
reg2 = reg1.match('MeirzeE')
print (reg2.group())


#creating a generic pattern object that starts with T
reg1 = re.compile('^T')
searchstring = 'This is a test'

print ("\n 2. Checking if searchstring value is matching reg1 value (which is any string that starts with T) the resualts of this check will be inserted to reg2 variable:")
reg2 = reg1.match(searchstring)
print (reg2)

print ("\n 3. We can do the same check directly on reg1 var without using the reg2 variable:")
print (reg1.match(searchstring))

print ("\n 4. Print the match: ")
print (reg1.match(searchstring).group())
# or 
print (reg2.group() )

# The $ sign is for searching chars at the end of the strings note that we have to use the search method
# match checks the beginning of the string while search method looks for all.
print ("\n 5. Checking if the search string ends with charecter t: ")
reg3 = re.compile('t$')
reg4 = reg3.search(searchstring)
print (reg4.group())

print ("\n 6. Checking if a file extension is pdf: ")

r1 = re.compile("\.pdf$")  # regular expression corrected
if r1.search("spam.pdf"):  # re.match() replaced with re.search()
    print ("yes")
else:
    print ("no")