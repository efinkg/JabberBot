#!/usr/bin/python
 
import sys
import os
from CoffeeEmail import SendSmallStartEmail
from CoffeeEmail import SendLargeStartEmail
from CoffeeEmail import SendCoffeeCancelledEmail

def barista_makeCoffee(order):
    
    username = 'admin'
    password = 'secret'
     
    url = 'http://localhost:5000'

    def do_command(method):
        #logs into the MakeCoffee web server on the local network
        os.system('curl -k -u %s:%s %s/%s' % (username, password, url, method))

    orderList = order.split(" ")
    
    if len(orderList) >1 and orderList[0] == 'barista':#'/etc/jabberd/cmds/barista':
        #Change this to the location/name of the desired first word of the jabber message
        #'barista make/start a small/large coffee"
        if orderList[1] == 'start' or orderList[1] == 'make': #natural systax
            if len(orderList) > 4 and orderList[3] == 'large' or orderList[3] == 'pot': #natural systax
                do_command('coffeelarge')
                #SendLargeStartEmail()
                print 'Starting Large Coffee'
                
            if len(orderList) > 4 and orderList[3] == 'small' or orderList[3] == 'cup': #natural systax
                do_command('coffeesmall')
                #SendSmallStartEmail()
                print 'Starting Small Coffee'

            #if len(orderList) == 4 and orderList[4] == 'coffee'
            #    do_command('coffee')
            #    print '/echo /push Starting Coffee'
     
        if orderList[1] == 'stop':
            do_command('killall')
            #SendCoffeeCancelledEmail()
            #print '/echo /push Stopping Coffee'
            
    #if len(orderList) == 1 and orderList[1] == 'stop':
    #    do_command('killall')
    #    print '/echo /push Stopping Coffee'
