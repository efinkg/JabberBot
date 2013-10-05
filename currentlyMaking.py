import csv

def isOn():
    with open('makingCoffee.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            list(row)
            currentPot = ['null','null']
            currentPot[0] = row[0] #Nickname
            currentPot[1] = row[1] #Amount Making

    if currentPot[0] == 'null':
        print 'availible'
        return 'availible'

    else:
        return currentPot
