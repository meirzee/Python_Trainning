#Regular_Expresion5.py 
# password setter

import re
import sys

passwordstring = input("Please set your password:")
#reg1 = re.compile('\d+' )   # include spaces
#reg2 = re.compile('[a-z]' )
#reg3 = re.compile('[A-Z]' )

reg1 = re.compile('^(?=.*[A-Z].*)(?=.*[0-9].*)(?=.*[a-z].*).{8}$') # this is replacing the 3 reg's I did at first . The ?=. makes the order of the chars not rellevant

match1 = reg1.findall(passwordstring)
#match2 = reg2.findall(passwordstring)
#match3 = reg3.findall(passwordstring)

count = 0
#while not (match1 and match2 and match3 and len(passwordstring) >= 8):
while not (match1):
    print ("Please use at lease 8 charecters and include one or more digits and one or more UPPERCASE letter.")
    passwordstring = input("Please set your password:")
    match1 = reg1.findall(passwordstring)
    #match2 = reg2.findall(passwordstring)
    #match3 = reg3.findall(passwordstring)
    count = count + 1
    print ("count is:", count )
    if count > 2:
        print ("Too many tries. Exiting ." ) 
        sys.exit() 

newpassword = 'passwordstring'
print ("password set successfully." )
    