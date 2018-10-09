#conditions
import string;
import sys; #The sys module allows you to use stdin and stdout, as well as stderr, but, most interestingly, we can utilize sys.argv(). To many, this is a confusing concept, but it is pretty simple and very useful once you learn it. The idea of sys.argv is to allow you to pass arguments through to Python from the command line.
#print len(sys.argv)
number_of_args = len(sys.argv) 
used_args = len(sys.argv) -1
script_threshold_args = 3

############### Simple loop example #################################
string1 = "LinuxCBT Scripting Edition 2004 Python Perl BASH PHP"
count = 0
while count < 10:
    print (string1)
    count = count + 1
########################################################################


############### Simple if statment ##########################################################################
print ("#################### simple if statment examples ######################################### \n \n \n ")
min = 89
max = 9

if min < max:
     print (min , "Is less then", max)
else:
     print (min, "Is greater than", max )

################# elif statment ###################################################################
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



        


