#Formating dates

from datetime import date
from datetime import time
from datetime import datetime

def main():
    now = datetime.now()
    print ("Default format: ", now)

    # Formating :%y/%Y year , %a/%A weekday, %b/%B month %d day of month 
    # the small letter is for short format and the uper case is for long format
    # The strftime function stands for String Format time
    
    print ("Long year format: ", now.strftime("%Y"))
    print ("Short year format: ", now.strftime("%y"))
    print ("Long weekday format: ", now.strftime("%A, %d"))
    print ("Long weekday format: ", now.strftime("%a, %d"))
    print ("Long month format: ", now.strftime("%B, %d"))
    print ("Short month format: ", now.strftime("%b, %d \n"))

    print ("Use %c for locales date and time will return the date and time as it is used in the local machine. some countries use the dd/mm/yy and some use mm/dd/yy etc: ")
    print (now.strftime("%c"))

    print ("\nUse %x for locale date: " )
    print (now.strftime("%x"))

    print ("\nUse %X for locales time")
    print (now.strftime("%X"))

    #Time formatting %I or %H for hours display 12 or 24 hours
    # %M for minutes %s for seconds %p for local AM/PM
    print ("Different time formating:")
    print (now.strftime("%I:%M:%S %p"))
    print (now.strftime("%H:%M:%S"))








if __name__ == "__main__":
    main()