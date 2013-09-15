import sys
import pickle

coffeeLiter = 0. #Clears variables.  Honestly, probably not important

try:    #makes sure that coffeeLiterTotal and coffeeOuncesTotal are initialized
    coffeeLiterTotal
except NameError:
    coffeeLiterTotal= 0.
try:
    coffeeOuncesTotal
except NameError:
    coffeeOuncesTotal = 0.

def makingCoffee(ounce): #Pass variable 'ounce' in from JabberBot
    global coffeeLiter #Global variables
    global coffeeLiterTotal
    
    print str(ounce)
    #Loads current value of coffeeLiterTotal
    pkl_file = open('totalCoffee.pkl', 'rb') #Open pickle file 'totalCoffee'
    coffeeLiterTotal = pickle.load(pkl_file) #write current value of 'totalCoffee' to coffeeLiterTotal
    pkl_file.close() #Close pickle file 'totalCoffee'

    coffeeLiter = coffeeLiter + ounce/33.8 #Calculate liters from ounces and add to current coffeeLiter
    coffeeLiterTotal = coffeeLiterTotal + ounce/33.8 #Calculate liters from ounces and add to current coffeeLiterTotal
    print str(coffeeLiter)
    print str(coffeeLiterTotal)
    #Writes current value of coffeeLiterTotal
    output = open('totalCoffee.pkl', 'wb') #Open pickle file 'totalCoffee'
    pickle.dump(coffeeLiterTotal, output) #write current value of coffeeLiterTotal 'totalCoffee'
    output.close() #Close pickle file 'totalCoffee'

def coffeeMade():
    global cofeeLiter #Global variable
    return coffeeLiter

def coffeeMadeTotal():
    #global coffeeLiterTotal #Global variable
    
    #Loads current value of coffeeLiterTotal
    pkl_file = open('totalCoffee.pkl', 'rb') #Open pickle file 'totalCoffee'
    coffeeLiterTotal = pickle.load(pkl_file) #write current value of 'totalCoffee' to coffeeLiterTotal
    pkl_file.close() #Close pickle file 'totalCoffee'
    
    return coffeeLiterTotal
