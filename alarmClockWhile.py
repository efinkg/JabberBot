import csv
from config import timeZone
import datetime
import dateutil
from dateutil import tz
import time

with open('/Code/JabberBot/alarmClockSchedule.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        list(row)
        Schedule = ['null','null','null','null']
        Schedule[0] = row[0] #Day of the Week
        timeSchedule = row[1]
        hours,minutes,seconds = (str(x) for x in timeSchedule.split(':'))        
        Schedule[1] = hours #Hours
        Schedule[2] = minutes #Minutes
        Schedule[3] = seconds #Seconds
        print Schedule
        if Schedule[0] == 'MON':
            #Alarm for Monday
            hourScheduled = hours
            minuteScheduled = minutes
            print hourScheduled
            print minuteScheduled
            notTime = 1
            while(notTime):
                timeNow = datetime.datetime.now(dateutil.tz.gettz(timeZone()))
                hour = str(timeNow[3])
                print hour
                minute = str(timeNow[4])
                print minute
                if hourScheduled == hour and minuteScheduled == minute:
                    print 'Alfred, awaken!'
                    notTime = 0
            
            
        
            '''
            #Alarm for Monday
            hour=str(Schedule[1])
            minute=str(Schedule[2])
            timeScheduled = hour + ':' + minute
            timestr = str(datetime.datetime.now(dateutil.tz.gettz(timeZone())))
            
            date, time = timestr.split(" ",1) #date is the part of the split string before the space, time is the part after the space
            timeNow, utcCorrection = time.split(".", 1) #timeMade is the part of the time string before the period
            hourNow,minuteNow,secondNow = timeNow.split(':')
            print hourNow
            print minuteNow
            print secondNow
            
            notTime = 1
            while (notTime):
                if timeSplit == timeScheduled():
                    notTime = 0
                    '''
        '''
        if Schedule[0] == 'TUE':
            Tue = cron.new(command='/usr/bin/echo',comment='Alarm for Tuesday')
            Tue.hour.on(Schedule[1])
            Tue.minute.on(Schedule[2])
            Tue.day.on(Schedule[0])

        if Schedule[0] == 'WED':
            Wed = cron.new(command='/usr/bin/echo',comment='Alarm for Wednesday')
            Wed.hour.on(Schedule[1])
            Wed.minute.on(Schedule[2])
            Wed.day.on(Schedule[0])

        if Schedule[0] == 'THU':
            Thur = cron.new(command='/usr/bin/echo',comment='Alarm for Thursday')
            Thur.hour.on(Schedule[1])
            Thur.minute.on(Schedule[2])
            Thur.day.on(Schedule[0])

        if Schedule[0] == 'FRI':
            Fri  = cron.new(command='/usr/bin/echo',comment='Alarm for Monday')
            Fri.hour.on(Schedule[1])
            Fri.minute.on(Schedule[2])
            Fri.day.on(Schedule[0])

def enableAll():
    Mon.enable()
    Tue.enable()
    Wed.enable()
    Thur.enable()
    Fri.enable()

def disableAll():
    Mon.enable(False)
    Tue.enable(False)
    Wed.enable(False)
    Thur.enable(False)
    Fri.enable(False)
    '''
