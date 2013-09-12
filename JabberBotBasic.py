#! /usr/bin/env python
from jabberbot import JabberBot, botcmd
from barista_bot_control import barista_makeCoffee
from config import jabberUsername, jabberPassword
from howMuch import coffeeMade, clearCoffeeMade, coffeeMadeTotal
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
        '''euid = os.geteuid()
        if euid != 0:
            #print "Script not started as root. Running sudo.."
            args = ['sudo', sys.executable] + sys.argv + [os.environ]
            # the next line replaces the currently-running process with the sudo
            os.execlpe('sudo', *args)'''
        order = mess.getBody()
        barista_makeCoffee(order)
        #return str(mess)
        return 'I have forwarded your order to the barista.'

    @botcmd
    def howmuch(self, mess, args):
        print 'I am reading your coffee usage'
        volMade = coffeeMade()
        print volMade
        return 'I have made %d liters of coffee since last reboot' %volMade

    @botcmd
    def howmuchtotal(self, mess, args):
        volMadeTotal = coffeeMadeTotal()
        print volMadeTotal
        return 'I have made %d liters of coffee since I started counting' %volMadeTotal
    
    '''
    @botcmd
    def nextalarm(self, mess, args):
        return alarm_clock.next_alarm()                
'''        

debug = 'false'
bot = SystemInfoJabberBot(jabberUsername(),jabberPassword())
bot.serve_forever()
