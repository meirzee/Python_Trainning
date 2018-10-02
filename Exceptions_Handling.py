#Exceptions_Handling

#when using try we allow the script to handle the exceptions of the script by performing some action without exiting 

f1 = input("Please specify file name: ")

try:
    handleFile = open(f1, 'r')
except:
    print ("problem openning file :" , f1 , "\n")


print ("Continuing with script execution")