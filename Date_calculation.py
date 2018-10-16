#Author: Meir Zeevi
#Date: 12 Sept 2018
#Purpose: Excersise

import time
import datetime
import calendar

from datetime import date

today = date.today()
print ("Today is:", today)

print ("-------- Life Expectancy V1 --------")


NAME = input("What is your name? ")
BIRTH_DATE = input("what is your birth date? i.e YYYY-MM-D   \n ")

def days_between(today, BIRTH_DATE ):
    today = date.today()
    BIRTH_DATE = datetime.strptime(BIRTH_DATE, "%Y-%m-%d")
    AGE = datetime.timedelta(today, BIRTH_DATE )
    print (AGE)


days_between(today, BIRTH_DATE )










#END
