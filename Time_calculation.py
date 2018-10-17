#Time Calaculations using timedelta class

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

print (timedelta(days=365, hours=24, minutes=0)) # timedelta calculates the delta it can use days/weeks/hours/min/sec all are optional arguments
print( "\nOne year from now it will be " , datetime.now() + timedelta(days=365))
print("\nTwo weeks from now it will be: ", datetime.now() + timedelta(weeks=2) )

#calculating what was the date one week a go
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print ("\nOne week ago it was ", s )


#calculating how many days untill specific day on the current year - on this example I used April first 
# date arguments are year,month,day

today = date.today() # gets todays date
Destination_date = date(today.year, 4, 1) 

if Destination_date < today:
    print ("The requested day already went by", (today - Destination_date).days, "days ago" )
    #Destination_date = Destination_date.replace(year=today.year + 1) # This works to for incremanting the year + 1
    Destination_date = Destination_date + timedelta(days=365)
    print ("The next specific day will arrive in: ", abs(Destination_date - today).days , "days")
else:
    print ("The requested date will arrive in: ", (Destination_date - today).days ,"days" )