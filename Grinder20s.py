#import RPi.GPIO as GPIO
import time
import os
import sys

KETTLE = 18
SOLENOID = 17
GRINDER = 27
PUMP = 22

'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(KETTLE, GPIO.OUT)
GPIO.setup(SOLENOID, GPIO.OUT)
GPIO.setup(GRINDER, GPIO.OUT)
GPIO.setup(PUMP, GPIO.OUT)
'''
print sys.argv[1]

#GPIO.output(GRINDER, GPIO.HIGH)
timeGrind = float((13./6.)*float(sys.argv[1]))
print timeGrind
time.sleep(timeGrind)
print 'I ground beans for %d oz of Coffee' %timeGrind
#GPIO.output(GRINDER, GPIO.LOW)

