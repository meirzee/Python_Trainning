#Birthday
import sys
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


NAME = input("What is your name? ")
AGE = int(input("How Old are you? "))
DELTA = (100 - AGE)

TODAY = date.today()


DESTINATION_DATE= TODAY.replace(year = TODAY.year + DELTA)
print ("Hello ", NAME ,"you are now " , AGE ,"years old and you have got " , DELTA , "years left to live up to 100 years old." )
print ("You will be 100 years old on:", DESTINATION_DATE )



