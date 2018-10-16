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
match2 = reg2.search(searchstring)
# Note that search scans all the chars too and if it founds a match it shows it and go to next char until it encounter a none match then it exits
# for example if I give it 111asc222 it will return 111 but when it will get to char "a" it will exit and will return 111 only
#if you want it to continue use findall or finditer
#match2 = reg2.findall(searchstring)

if match2:
    print ("Found a match for: ", match2.group())
else:
    print ("No match..")
