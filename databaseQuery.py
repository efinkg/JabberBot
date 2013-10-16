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

def findPermissions(jabberAddress):
    with open('/Code/JabberBot/users.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            list(row)
            userName = ['null','null','null','null']
            userName[0] = row[0] #Nickname
            userName[1] = row[1] #Jabber Username
            userName[2] = row[2] #Email Account
            userName[3] = row[3] #Permissions
            #print userName[0]
            #print username
            if str(jabberAddress) == userName[1]:
                    if userName[3] == 'Full':
                        print 'FullApproval'
                        return 'full_approval'
                    print 'approved by me'
                    return 'approved'
