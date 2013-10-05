#! /usr/bin/env python
from jabberbot import JabberBot, botcmd
from approved import approve, saidPlease
from barista_bot_control import barista_makeCoffee
from config import timeZone, jabberUsername, jabberPassword
from currentlyMaking import isOn
from howMuch import coffeeMade, coffeeMadeTotal
import datetime
import dateutil
from dateutil import tz
import sys
import os

class SystemInfoJabberBot(JabberBot):
    @botcmd
    def serverinfo( self, mess, args):
        """Displays information about the server"""
        version = open('/proc/version').read().strip()
        loadavg = open('/proc/loadavg').read().strip()

        return '%s\n\n%s' % ( version, loadavg, )
    
    @botcmd
    def time( self, mess, args):
        """Displays current server time"""
        time = datetime.datetime.now(dateutil.tz.gettz(timeZone()))
        return str(time)

    @botcmd
    def whoami(self, mess, args):
        """Tells you your username"""
        return mess.getFrom().getStripped()

    @botcmd
    def got(self, mess, args):
        """This is for Glass to stop Stupid Looping"""
        message = str(mess.getBody())
        listMessage = message.split(" ")
        if listMessage[1] == 'TEXT':
            print 'Aint Nobody got Time for That'
        else:
            return 'Got milk?'

    @botcmd
    def alfred(self, mess, args):
        '''Makes Coffee, messages take the form "Alfred make (me) a cup/thermos/pot (of coffee)" where words in parentheses are not required'''
        user = mess.getFrom().getStripped()
        time = datetime.datetime.now(dateutil.tz.gettz(timeZone()))
        order = mess.getBody()
        approval = approve(user)
        if approval == 'approved' or saidPlease(order) == 'yes':
            barista_makeCoffee(order, user, time)
            #return str(mess)
            return 'I have forwarded your order to the barista.'
        return 'Say Please.'
    

    @botcmd
    def howmuch(self, mess, args):
        '''How much coffee has been made since last reboot of the system'''
        print 'I am reading your coffee usage'
        volMade = coffeeMade()
        print volMade
        return 'I have made %d liters of coffee since last reboot' %volMade

    @botcmd
    def howmuchtotal(self, mess, args):
        '''How much coffee has been made ever'''
        user = mess.getFrom().getStripped()
        if user == approvedUser() or approvedUser2():
            volMadeTotal = coffeeMadeTotal()
            print volMadeTotal
            return 'I have made %d liters of coffee since I started counting' %volMadeTotal
        return 'I am sorry, sir, that is strictly need-to-know'
    
    '''
    @botcmd
    def nextalarm(self, mess, args):
        return alarm_clock.next_alarm()                
'''        

debug = 'false'
bot = SystemInfoJabberBot(jabberUsername(),jabberPassword())
bot.serve_forever()
