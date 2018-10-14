#Regular_Expression4.py

import re

searchstring = input("Please give a serch string:")
reg1 = re.compile('Hello' , re.IGNORECASE)
match1 = reg1.search(searchstring)

if match1:
    print ("Found a match for: ", match1.group())
else:
    print ("No match..")


# compile a digits object pattern
# Note that if I will input string that ends with numbers it will return No match but if the string will contain a digit on the first char then it will match 
# this is since the match function is looking for the first char of the list and if it finds it retuns true and stops  but it doesnt go through all the string if it doesnt find on the first char it exits
# if we want it to search for all the charecters of the string we need to use the search function instead the match but note that the search function will stop once it will find a match and will not continue scanning all the string

searchstring = input("Please give a serch string with digits:")
reg2 = re.compile('\d+' , re.IGNORECASE) 
#match2 = reg2.search(searchstring)
match2 = reg2.findall(searchstring)

if match2:
    print ("Found a match for: ", match2 )
else:
    print ("No match..")
