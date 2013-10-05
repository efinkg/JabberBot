import csv
import sys

def approve(username):
    with open('/Code/JabberBot/users.csv') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                list(row)
                userName = ['null','null','null']
                userName[0] = row[1]
                userName[1] = row[2]
                userName[2] = row[3]
                print userName[0]
                print str(username)
                print userName[2]
                if str(username) == userName[0]:
                    if userName[2] == 'Full':
                        print 'FullApproval'
                        return 'full_approval'
                    print 'approved by me'
                    return 'approved'

def saidPlease(order):
    orderList = order.split(" ")
    listLength = len(orderList)
    print orderList[(listLength-1)]
    if orderList[1] == 'stop':
            return 'yes'
    if orderList[(listLength-1)] == 'please' or orderList[(listLength-1)] == 'Please':
        print 'yes'
        return 'yes'
    return 'no'
