import csv

def findEmail(jabberAddress):
    with open('/Code/JabberBot/users.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            list(row)
            userName = ['null','null','null']
            userName[0] = row[0] #Nickname
            userName[1] = row[1] #Jabber Username
            userName[2] = row[2] #Email Account
            #print userName[0]
            #print username
            if jabberAddress == str(userName[1]):
                return userName[2]

def findNickname(jabberAddress):
    with open('/Code/JabberBot/users.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            list(row)
            userName = ['null','null','null']
            userName[0] = row[0] #Nickname
            userName[1] = row[1] #Jabber Username
            userName[2] = row[2] #Email Account
            #print userName[0]
            #print username
            if jabberAddress == str(userName[1]):
                return userName[0]
