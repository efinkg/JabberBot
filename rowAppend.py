from config import timeZone
import csv
import datetime
import dateutil
from dateutil import tz


time_finished = datetime.datetime.now(dateutil.tz.gettz(timeZone()))
timestr = str(time_finished)
date, time = timestr.split(" ",1) #date is the part of the split string before the space, time is the part after the space
timeDone, utcCorrection = time.split(".", 1) #timeMade is the part of the time string before the period
print timeDone

with open('coffeeMade.csv', 'rb') as csvfile:
    

with open('coffeeMade.csv','wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([str(timeDone)])
    
