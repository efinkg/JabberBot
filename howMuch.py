import sys

coffeeLiter = 0.
coffeeOunces = 0.
try:
    coffeeLiterTotal
except NameError:
    coffeeLiterTotal= 0.
try:
    coffeeOuncesTotal
except NameError:
    coffeeOuncesTotal = 0.

def makingCoffee(ounce):
    global coffeeOunces
    global coffeeLiter
    global coffeeOuncesTotal
    global coffeeLiterTotal
    coffeeOunces = coffeeOunces + ounce
    coffeeOuncesTotal = coffeeOuncesTotal + ounce
    coffeeLiter = coffeeOunces/33.8
    coffeeLiterTotal = coffeeOuncesTotal/33.8

def coffeeMade():
    global cofeeLiter
    return coffeeLiter

def coffeeMadeTotal():
    global coffeeLiterTotal
    return coffeeLiterTotal

def initialize():
    global coffeeOunces
    print 'hi'
    coffeeOunces = 0
