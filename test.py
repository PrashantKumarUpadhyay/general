#Getting Date :tdate
from datetime import date
tdate=date.today()
#converting date to mmddyyyy format :fdate
fdate=tdate.strftime("%m/%d/%y")
print("date:",fdate)
#reading a file dir 
