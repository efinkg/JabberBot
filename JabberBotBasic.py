#! /usr/bin/env python
from jabberbot import JabberBot, botcmd
from barista_bot_control import barista_makeCoffee, saidPlease
from config import jabberUsername, jabberPassword
from howMuch import coffeeMade, coffeeMadeTotal
import datetime
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
        return str(datetime.datetime.now())

    @botcmd
    def rot13( self, mess, args):
        """Returns passed arguments rot13'ed"""
        return args.encode('rot13')

    @botcmd
    def whoami(self, mess, args):
        """Tells you your username"""
        return mess.getFrom().getStripped()
    
    @botcmd
    def whoareyou(self, mess, args):
        """Tells you your username"""
        return mess.getTo().getStripped()
    
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
        '''Makes Coffee'''
        user = mess.getFrom().getStripped()
        order = mess.getBody()
        if user == 'efinkg@jabber.iitsp.com' or saidPlease(order) == 'yes':
            barista_makeCoffee(order)
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
        if user == 'efinkg@jabber.iitsp.com':
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
