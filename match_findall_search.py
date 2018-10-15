import re

#Difference between match,search and findall

#first we compile a pattern of digits that contains only digits
reg1 = re.compile('\d+')

#Checking if it returns the object as match:

reg2 = reg1.findall('mei1rz2ee3')  # findall searches all the string for digits and should return them all
reg3 = reg1.match('mei1rz2ee3')  # match is looking for match on the first char and will not find it so it will return None unless we will place a digit on the first location i.e: 1meirz
reg4 = reg1.search('mei1rz2ee3')  # search will look for a digit until it founds one, once it will find it will exit and stop searching it will not search the entire string


print ("findall return: ", reg2)
print ("match return: ", reg3)
print ("search returns: ", reg4.group())
