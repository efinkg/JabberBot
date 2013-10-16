from crontab import CronTab
import csv
global chron

global chron
system_cron = CronTab()
user_cron = CronTab('root')
file_cron = CronTab(tabfile='filename.tab')
mem_cron = CronTab(tab="""
* * * * * command
""")
job  = cron.new(command='/usr/bin/echo')
job.minute.during(5,50).every(5)
job.hour.every(4)
job.day.on(4, 5, 6)

job.dow.on('SUN')
job.month.during('APR', 'NOV')

'''
with open('/Code/JabberBot/alarmClockSchedule.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        list(row)
        Schedule = ['null','null','null','null']
        Schedule[0] = row[0] #Day of the Week
        time = row[1]
        hours,minutes,seconds = (int(x) for x in time.split(':'))
        Schedule[1] = hours #Hours
        Schedule[2] = minutes #Minutes
        Schedule[3] = seconds #Seconds
        if Schedule[0] == 'MON':
            Mon  = cron.new(command='/usr/bin',comment='Alarm for Monday')
            Mon.hour.on(Schedule[1])
            Mon.minute.on(Schedule[2])
            Mon.day.on(Schedule[0])
        
        elif Schedule[0] == 'TUE':
            Tue = cron.new(command='/usr/bin/echo',comment='Alarm for Tuesday')
            Tue.hour.on(Schedule[1])
            Tue.minute.on(Schedule[2])
            Tue.day.on(Schedule[0])

        elif Schedule[0] == 'WED':
            Wed = cron.new(command='/usr/bin/echo',comment='Alarm for Wednesday')
            Wed.hour.on(Schedule[1])
            Wed.minute.on(Schedule[2])
            Wed.day.on(Schedule[0])

        elif Schedule[0] == 'THU':
            Thur = cron.new(command='/usr/bin/echo',comment='Alarm for Thursday')
            Thur.hour.on(Schedule[1])
            Thur.minute.on(Schedule[2])
            Thur.day.on(Schedule[0])

        elif Schedule[0] == 'FRI':
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
