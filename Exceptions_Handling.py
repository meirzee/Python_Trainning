#Exceptions_Handling

#when using try we allow the script to handle the exceptions of the script by performing some action without exiting 

f1 = input("Please specify file name: ")

try:
    handleFile = open(f1, 'r')
except:
    print ("[]: Problem openning file :" , f1 , "\n")
else:
    print ("File name was found.")
finally:
    print ("This code will always be executed ...")



print ("Continuing with script execution")