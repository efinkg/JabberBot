import sys

coffeeLiter = 0.
coffeeOunces = 0.
coffeeOuncesTotal = 0.
coffeeLiterTotal = 0.


def makingCoffee(ounce):
    global coffeeOunces
    global coffeeLiter
    coffeeOunces = coffeeOunces + ounce
    coffeeLiter = coffeeOunces/33.8
    coffeeLiterTotal = coffeeOuncesTotal/33.8

def coffeeMade():
    global cofeeLiter
    return coffeeLiter

def coffeeMadeTotal():
    global coffeeLiterTotal
    return coffeeLiterTotal

def clearCoffeeMade():
    global coffeeOunces
    print 'hi'
    coffeeOunces == 0
