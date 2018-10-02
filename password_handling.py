#password

#print ("Following while loop is for checking that password is in the correct standards")
#password = input("Please create password: ")
#while not (len(password) >= 6 and any(x.isupper() for x in password) and any(x.isdigit() for x in password) and any(x.islower() for x in password)):
#    print ("Password must contain at least 7 charecters and contains at least one upper case charecther and one lower case")
#    password = input("Please insert new password: ")
    

print ("Following is a different way for checking that password is in the correct standards")
password = input("Please create password: ")

CONTAIN_DIGIT = any(x.isdigit() for x in password)
CONTAIN_UPPERCASE = any(x.isupper() for x in password) 
CONTAIN_LOWERCASE = any(x.islower() for x in password)
CONTAIN_SEVEN_CHARS = len(password) >= 7

while (CONTAIN_DIGIT == False or CONTAIN_UPPERCASE == False or CONTAIN_LOWERCASE == False or CONTAIN_SEVEN_CHARS == False):
    print ("Password must contain at least 7 charecters and contains at least one upper case charecther and one lower case")
    password = input("Please insert new password: ")
    CONTAIN_DIGIT = any(x.isdigit() for x in password)
    CONTAIN_UPPERCASE = any(x.isupper() for x in password) 
    CONTAIN_LOWERCASE = any(x.islower() for x in password)
    CONTAIN_SEVEN_CHARS = len(password) >= 7

print (CONTAIN_DIGIT)
print (CONTAIN_UPPERCASE)
print (CONTAIN_LOWERCASE)
print (CONTAIN_SEVEN_CHARS)
print ("password was set correctly.")