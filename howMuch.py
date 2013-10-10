import sys
import csv
import datetime
import dateutil
from dateutil import tz
from databaseQuery import findNickname


coffeeLiter = 0. #Clears variables.  Honestly, probably not important

try:    #makes sure that coffeeLiterTotal and coffeeOuncesTotal are initialized
    coffeeLiterTotal
except NameError:
    coffeeLiterTotal= 0.
try:
    coffeeOuncesTotal
except NameError:
    coffeeOuncesTotal = 0.

def makingCoffee(ounce, user, time_stamp): #Pass variable 'ounce' in from JabberBot
    global coffeeLiter #Global variables
    global coffeeLiterTotal
    #Loads current value of coffeeLiterTotal

    nickName = findNickname(user)
    print nickName

    #print 'I have gotten to the date split'
    timestr = str(time_stamp)
    date, time = timestr.split(" ",1) #date is the part of the split string before the space, time is the part after the space
    timeMade, utcCorrection = time.split(".", 1) #timeMade is the part of the time string before the period
    print date
    year, month, day = (int(x) for x in date.split('-'))
    print str(day)
    print str(month)
    print str(year)
    weekDay= datetime.date(year,month,day)
    print str(weekDay)
    dayOfWeek = weekDay.strftime("%A")
    print dayOfWeek
    
    #print str(date)
    #print str(timeMade)
    
    with open('/Code/JabberBot/useageData/coffeeMade.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            list(row)
            coffeeLiterTotal = float(row[2])

    coffeeLiter = coffeeLiter + ounce/33.8 #Calculate liters from ounces and add to current coffeeLiter
    coffeeLiterTotal = coffeeLiterTotal + ounce/33.8 #Calculate liters from ounces and add to current coffeeLiterTotal
    #print str(coffeeLiter)
    #print str(coffeeLiterTotal)
    
    #Writes current value of coffeeLiterTotal
    with open('/Code/JabberBot/useageData/coffeeMade.csv','ab') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow([str(nickName), str(ounce), str(coffeeLiterTotal), dayOfWeek, str(day), str(month), str(year), str(timeMade)])
'''        
    with open('makingCoffee.csv','w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow([str(nickName), str(ounce)])

'''
'''
def finished():
    with open('makingCoffee.csv','w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(['null', 'null'])
'''
def coffeeMade():
    global cofeeLiter #Global variable
    return coffeeLiter

def coffeeMadeTotal():
    global coffeeLiterTotal #global coffeeLiterTotal #Global variable
    #Loads current value of coffeeLiterTotal
    with open('/Code/JabberBot/useageData/coffeeMade.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            list(row)
            coffeeLiterTotal = float(row[2])
    
    return coffeeLiterTotal
