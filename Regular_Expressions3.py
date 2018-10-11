#Regular_Expressions3.py
import re

#Searching for chars across multiple lines
# lets say we have a string that is a cross few lines and we know that regular expresions "." and "*" can not search the new line
# so we can use the DOTALL function i.e:

Search_String="This is a test \nThis is a test 2 \nThis is a test 2"
#print (Search_String)

reg1 = re.compile('.*')

match1 = reg1.match(Search_String)
print (match1.group())

print ("\nNow if we use DOTALL function when we compile the object the reg expression will be able to move on and search on the new line ")

reg1 = re.compile('.*', re.DOTALL )

match1 = reg1.match(Search_String)
print (match1.group())


reg2 = re.compile('^T')
match2 = reg2.match(Search_String)
print ("\nThe full string is:\n" , Search_String )

print ("\nFollowing is the matchin T upon one line: ", match2.group())


#This part is not working since it returns only one T - Need to understand why
reg3 = re.compile('T', re.IGNORECASE )
match3 = reg3.findall(Search_String)
print ("\nFollowing is the matchin T upon all lines: ", match3)

