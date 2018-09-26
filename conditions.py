#conditions
import string;
import sys; #The sys module allows you to use stdin and stdout, as well as stderr, but, most interestingly, we can utilize sys.argv(). To many, this is a confusing concept, but it is pretty simple and very useful once you learn it. The idea of sys.argv is to allow you to pass arguments through to Python from the command line.
#print len(sys.argv)
number_of_args = len(sys.argv) 
used_args = len(sys.argv) -1
script_threshold_args = 3

###### Simple if statment ################
print ("#################### simple if statment examples ######################################### \n \n \n ")
min = 89
max = 9

if min < max:
     print (min , "Is less then", max)
else:
     print (min, "Is greater than", max )

################# elif statment #############################
#testing the number of arguments passing to the script
#Note that sys module count the script name as the first argument.
print ("#################### else if examples ######################################### \n \n \n ")

if len(sys.argv) < script_threshold_args:
    print ("The script", sys.argv[0], "requires at leset", script_threshold_args ,"arguments" )
    print ("You have used: ", used_args  , "arguments" )
elif used_args > script_threshold_args:
    print ("To much arguments used, script is expecting ", script_threshold_args - 1 ,"arguments")
elif  used_args > script_threshold_args + 10:
    print ("Now you realy used to much ...")


    for i in sys.argv:
        print ("Argument: ", i )

else: 
    print ("other options are :......")


########### For loops ####################
####   for loop it an itrerator ##########
##########################################
print ("#################### For loop examples ######################################### \n \n \n ")
string1 = "Hellow!!!"

for i in string1:
    print (i)


print ("#################### For loop throuh range ######################################### \n \n \n ")

for i in range(20):
    print (i)


print ("#################### more complex For loop example ######################################### \n \n \n ")
#lets say we have a file with three lines and we want to extract its data to a different log file
#the lines are treated as items in a list and we want to extract the data maybe manipulate each line and create a different list from it

logfile1 = ["date 20040925 IP 192.168.1.2 port 8000" , "date 20040926 IP 192.168.3.3 port 2000" , "date 20040927 IP 192.168.1.7 port 5000"]
logfile2 = []
for i in logfile1:
    logfile2.extend(i.split() )
    print (logfile2)



###########################################################
#######    While Loop   ###################################
###########################################################
print ("#################### simple while loop example ######################################### \n \n \n ")

count = 0

while count <= 10:
    print (count)
    count = count+1


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
