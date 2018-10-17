#Author: Meir Zeevi
#Date: 12 Sept 2018
#Purpose: Excersise

from datetime import date
from datetime import time
from datetime import datetime



def main():
    # Get the current date
    TODAY = date.today()
    print ("Today is: ", TODAY )
    print ("The Date componeents are: ", TODAY.day, TODAY.month, TODAY.year)

    #Gets today's date and current time
    TODAY = datetime.now()
    print("The Current date and time is: ", TODAY)

    #Get only time without the date
    T = datetime.time(datetime.now())
    print ("Time is: ", T)



if __name__ == "__main__":
    main()
