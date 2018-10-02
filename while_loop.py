###########################################################
#######    While Loop   ###################################
###########################################################

import sys

print ("#################### simple while loop example ######################################### \n \n \n ")

count = 0

while count <= 10:
    print (count)
    count = count+1


##############################################################


## While loop without exiting:

# while 1:
#    do some actions
#    ..
#    ..


#if we want to exit it on some cases then we need to add the break:

count = 0
while 1:
    x = input("please enter password: ")
    count = count + 1
    if count == 3:
        answer = input("You have typed wrong password for 3 times. Would you like to continue? y/n:  ")
        if answer == "n":
            #sys.exit() # this will exit the script
            break # this will exit the while loop and continue with the script.
        else:
            count = 0

print ("Got up to here...")