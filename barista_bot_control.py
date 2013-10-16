#!/usr/bin/python
 
import sys
import os
import threading
from coffeetimethreading import CoffeeMaker
from CoffeeEmail import SendSmallStartEmail, SendLargeStartEmail, SendThermosStartEmail, SendCoffeeCancelledEmail, SendTwoCupStartEmail

coffee_maker = CoffeeMaker()

def barista_makeCoffee(order, user, time):
    orderList = order.split(" ")
    print orderList

    if len(orderList) > 1:   # and orderList[0] == 'barista' or orderList[0] == 'Barista':
                            # I am removing this word to make changing the name of the Press easier
                            #Change this to the location/name of the desired first word of the jabber message
        #'barista make/start a small/large coffee"
        if orderList[1] == 'start' or orderList[1] == 'make': #natural systax
            if orderList[2] == 'me': #Allows use of 'Make a Coffee' or 'Make me a coffee" by dropping 'me' if it appears
                del orderList[2]
                
            if len(orderList) > 3 and orderList[3] == 'large' or orderList[3] == 'pot': #natural systax
                #do_command('coffeelarge')
                size = 29
                print 'Starting Large Coffee'
                coffee_maker.makeCoffee(size, user, time)
                SendLargeStartEmail(user)
                
            if len(orderList) > 3 and orderList[3] == 'small' or orderList[3] == 'cup': #natural systax
                #do_command('coffeesmall')
                size = 12
                print 'Starting Small Coffee'
                coffee_maker.makeCoffee(size, user, time)
                SendSmallStartEmail(user)

            if len(orderList) > 3 and orderList[3] == 'thermos':
                print len(orderList)
                size = 20
                print 'Starting a thermos of coffee'
                coffee_maker.makeCoffee(size, user, time)
                SendThermosStartEmail(user)

            if len(orderList) > 4 and orderList[2] == 'two' and orderList[3] =='cups':
                print len(orderList)
                size = 26
                print 'Starting two cups of coffee'
                coffee_maker.makeCoffee(size, user, time)
                SendTwoCupStartEmail(user)

            if len(orderList) > 3 and orderList[3] == 'ounce':
                print len(orderList)
                size = 1
                print 'Starting an ounce of coffee'
                coffee_maker.makeCoffee(size, user, time)
                SendThermosStartEmail(user)


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
