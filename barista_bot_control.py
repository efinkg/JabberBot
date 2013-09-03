#!/usr/bin/python
 
import sys
import os
import threading
from coffeetimethreading import CoffeeMaker
from CoffeeEmail import SendSmallStartEmail
from CoffeeEmail import SendLargeStartEmail
from CoffeeEmail import SendCoffeeCancelledEmail

coffee_maker = CoffeeMaker()

def barista_makeCoffee(order):
    
    orderList = order.split(" ")
    
    if len(orderList) >1 and orderList[0] == 'barista':#'/etc/jabberd/cmds/barista':
        #Change this to the location/name of the desired first word of the jabber message
        #'barista make/start a small/large coffee"
        if orderList[1] == 'start' or orderList[1] == 'make': #natural systax
            if len(orderList) > 4 and orderList[3] == 'large' or orderList[3] == 'pot': #natural systax
                #do_command('coffeelarge')
                size = 34
                coffee_maker.makeCoffee(size)
                SendLargeStartEmail()
                print 'Starting Large Coffee'
                
            if len(orderList) > 4 and orderList[3] == 'small' or orderList[3] == 'cup': #natural systax
                #do_command('coffeesmall')
                size = 14
                coffee_maker.makeCoffee(size)
                SendSmallStartEmail()
                print 'Starting Small Coffee'

            if len(orderList) > 4 and orderList[3] == 'thermos':
                size = 20
                coffee_maker.makeCoffee(size)
                SendThermosStartEmail()
                print 'Starting Small Coffee'

            #if len(orderList) == 4 and orderList[4] == 'coffee'
            #    do_command('coffee')
            #    print '/echo /push Starting Coffee'
     
        if orderList[1] == 'stop':
            coffee_maker.force_stop()
            SendCoffeeCancelledEmail()
            print 'Stopping Coffee'
            
    #if len(orderList) == 1 and orderList[1] == 'stop':
    #    do_command('killall')
    #    print '/echo /push Stopping Coffee'
