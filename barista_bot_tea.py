#!/usr/bin/python
 
import sys
import os
import threading
from teatimethreading import CoffeeMaker
from CoffeeEmail import SendTeaStartEmail

coffee_maker = CoffeeMaker()

def barista_makeTea(order, user, time):
    orderList = order.split(" ")
    print orderList

    if len(orderList) > 1:   # and orderList[0] == 'barista' or orderList[0] == 'Barista':
                            # I am removing this word to make changing the name of the Press easier
                            #Change this to the location/name of the desired first word of the jabber message
        #'barista make/start a small/large coffee"
        if orderList[0].lower() == 'tea': #natural systax
                
            if len(orderList) > 3 and orderList[1].lower() == 'earl': #natural systax

                if len(orderList) > 3 and orderList[2].lower() == 'grey' or orderList[2].lower() == 'gray': #natural systax
                    
                    #do_command('coffeelarge')
                    size = 12
                    print 'Starting small tea'
                    coffee_maker.makeCoffee(size, user, time)
                    print 'makeCoffee sent'
                    SendTeaStartEmail(user)

            #if len(orderList) == 4 and orderList[4] == 'coffee'
            #    do_command('coffee')
            #    print '/echo /push Starting Coffee'
     
        if orderList[1] == 'stop':
            coffee_maker.force_stop()
            print str(user)
            SendCoffeeCancelledEmail(user)
            print 'Stopping Coffee'
        
#if len(orderList) == 1 and orderList[1] == 'stop':
#    do_command('killall')
#    print '/echo /push Stopping Coffee'
