#Regular_Expresion5.py 
# password setter

import re


passwordstring = input("Please set your password:")
reg1 = re.compile('\d+' )   # include spaces
reg2 = re.compile('[a-z]' )
reg3 = re.compile('[A-Z]' )

match1 = reg1.findall(passwordstring)
match2 = reg2.findall(passwordstring)
match3 = reg3.findall(passwordstring)

if match1 and match2 and match3 and len(passwordstring) >= 8:
    newpassword = 'passwordstring'
    print ("password set successfully." )
else:
    print ("Please use at lease 8 charecters and include one or more digits and one or more UPPERCASE letter.")

#print (match1 )
#print (match2 )
#print (match3 )