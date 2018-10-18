#Excersise2 - Taken from https://www.practicepython.org/

try:
    GET_NUM = int(input("Please specify an integer number: "))
    if type(GET_NUM) == int:
        print(GET_NUM, "is an integer")
except:
    print("\nThe number you gave is not an integer.\n")
if GET_NUM % 4 == 0:
    print(GET_NUM, "number is a multiple of 4.")
elif GET_NUM % 2 == 0:
    print("The number is even.")
elif GET_NUM % 2 != 0:
    print(GET_NUM, "number is odd.")


    
NUM2 = int(input("Please give number to check: "))
NUM_CHK = int(input("please give a number to check with: "))
RESUALT = NUM2 % NUM_CHK

if RESUALT == 0:
    print("The number you gave are devided fully.")
else:
    print("The numbers are not divisible ")









