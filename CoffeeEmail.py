import sys
import csv
from config import emailSenderUsername, emailSenderPassword
username = 'null'

def SendSmallStartEmail(user):
   global username
   username = user
   import subprocess
   import smtplib
   import socket
   from email.mime.text import MIMEText
   import datetime
   # Change to your own account information
   with open('/Code/JabberBot/users.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            list(row)
            userName = ['null','null']
            userName[0] = row[1]
            userName[1] = row[2]
            #print userName[0]
            #print username
            if username == str(userName[0]):
                to = userName[1]
                break
   gmail_user = emailSenderUsername()
   gmail_password = emailSenderPassword()
   smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
   smtpserver.ehlo()
   smtpserver.starttls()
   smtpserver.ehlo
   smtpserver.login(gmail_user, gmail_password)
   today = datetime.date.today()
   # Very Linux Specific
   arg='ip route list'
   p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
   data = p.communicate()
   split_data = data[0].split()
   ipaddr = split_data[split_data.index('src')+1]
   my_ip = 'I am Making you a Cup of Coffee, Sir'
   msg = MIMEText(my_ip)
   msg['Subject'] = 'Coffee Time'
   msg['From'] = gmail_user
   msg['To'] = to
   smtpserver.sendmail(gmail_user, [to], msg.as_string())
   smtpserver.quit()

def SendTwoCupStartEmail(user):
   global username
   username = user
   import subprocess
   import smtplib
   import socket
   from email.mime.text import MIMEText
   import datetime
   # Change to your own account information
   with open('/Code/JabberBot/users.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            list(row)
            userName = ['null','null']
            userName[0] = row[1]
            userName[1] = row[2]
            #print userName[0]
            #print username
            if username == str(userName[0]):
                to = userName[1]
                break
   gmail_user = emailSenderUsername()
   gmail_password = emailSenderPassword()
   smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
   smtpserver.ehlo()
   smtpserver.starttls()
   smtpserver.ehlo
   smtpserver.login(gmail_user, gmail_password)
   today = datetime.date.today()
   # Very Linux Specific
   arg='ip route list'
   p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
   data = p.communicate()
   split_data = data[0].split()
   ipaddr = split_data[split_data.index('src')+1]
   my_ip = 'I am Making you Two Cups of Coffee, Sir'
   msg = MIMEText(my_ip)
   msg['Subject'] = 'Coffee Time'
   msg['From'] = gmail_user
   msg['To'] = to
   smtpserver.sendmail(gmail_user, [to], msg.as_string())
   smtpserver.quit()

def SendLargeStartEmail(user):
   global username
   username = user
   import subprocess
   import smtplib
   import socket
   from email.mime.text import MIMEText
   import datetime
   # Change to your own account information
   with open('/Code/JabberBot/users.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            list(row)
            userName = ['null','null']
            userName[0] = row[1]
            userName[1] = row[2]
            #print userName[0]
            #print username
            if username == str(userName[0]):
                to = userName[1]
                break
   gmail_user = emailSenderUsername()
   gmail_password = emailSenderPassword()
   smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
   smtpserver.ehlo()
   smtpserver.starttls()
   smtpserver.ehlo
   smtpserver.login(gmail_user, gmail_password)
   today = datetime.date.today()
   # Very Linux Specific
   arg='ip route list'
   p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
   data = p.communicate()
   split_data = data[0].split()
   ipaddr = split_data[split_data.index('src')+1]
   my_ip = 'I am Making you a Pot of Coffee, Sir'
   msg = MIMEText(my_ip)
   msg['Subject'] = 'Coffee Time'
   msg['From'] = gmail_user
   msg['To'] = to
   smtpserver.sendmail(gmail_user, [to], msg.as_string())
   smtpserver.quit()

def SendThermosStartEmail(user):
   global username
   username = user
   import subprocess
   import smtplib
   import socket
   from email.mime.text import MIMEText
   import datetime
   # Change to your own account information
   with open('/Code/JabberBot/users.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            list(row)
            userName = ['null','null']
            userName[0] = row[1]
            userName[1] = row[2]
            #print userName[0]
            #print username
            if username == str(userName[0]):
                to = userName[1]
                break
   gmail_user = emailSenderUsername()
   gmail_password = emailSenderPassword()
   smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
   smtpserver.ehlo()
   smtpserver.starttls()
   smtpserver.ehlo
   smtpserver.login(gmail_user, gmail_password)
   today = datetime.date.today()
   # Very Linux Specific
   arg='ip route list'
   p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
   data = p.communicate()
   split_data = data[0].split()
   ipaddr = split_data[split_data.index('src')+1]
   my_ip = 'I am Making you a Thermos of Coffee, Sir'
   msg = MIMEText(my_ip)
   msg['Subject'] = 'Coffee Time'
   msg['From'] = gmail_user
   msg['To'] = to
   smtpserver.sendmail(gmail_user, [to], msg.as_string())
   smtpserver.quit()

def SendCoffeeDoneEmail():
   global username
   print username
   import subprocess
   import smtplib
   import socket
   from email.mime.text import MIMEText
   import datetime
   # Change to your own account information
   with open('/Code/JabberBot/users.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            list(row)
            userName = ['null','null']
            userName[0] = row[1]
            userName[1] = row[2]
            #print userName[0]
            #print username
            if username == str(userName[0]):
                to = userName[1]
                break
   gmail_user = emailSenderUsername()
   gmail_password = emailSenderPassword()
   smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
   smtpserver.ehlo()
   smtpserver.starttls()
   smtpserver.ehlo
   smtpserver.login(gmail_user, gmail_password)
   today = datetime.date.today()
   # Very Linux Specific
   arg='ip route list'
   p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
   data = p.communicate()
   split_data = data[0].split()
   ipaddr = split_data[split_data.index('src')+1]
   my_ip = 'Your Coffee Is Ready, Sir'
   msg = MIMEText(my_ip)
   msg['Subject'] = 'Coffee Time'
   msg['From'] = gmail_user
   msg['To'] = to
   smtpserver.sendmail(gmail_user, [to], msg.as_string())
   smtpserver.quit()

def SendCoffeeCancelledEmail(user):
   print str(user)
   username = user
   import subprocess
   import smtplib
   import socket
   from email.mime.text import MIMEText
   import datetime
   # Change to your own account information
   with open('/Code/JabberBot/users.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            list(row)
            userName = ['null','null']
            userName[0] = row[1]
            userName[1] = row[2]
            #print userName[0]
            #print username
            if username == str(userName[0]):
                to = userName[1]
                break
   gmail_user = emailSenderUsername()
   gmail_password = emailSenderPassword()
   smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
   smtpserver.ehlo()
   smtpserver.starttls()
   smtpserver.ehlo
   smtpserver.login(gmail_user, gmail_password)
   today = datetime.date.today()
   # Very Linux Specific
   arg='ip route list'
   p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
   data = p.communicate()
   split_data = data[0].split()
   ipaddr = split_data[split_data.index('src')+1]
   my_ip = 'Your Coffee Is Canceled, Sir'
   msg = MIMEText(my_ip)
   msg['Subject'] = 'Coffee Time'
   msg['From'] = gmail_user
   msg['To'] = to
   smtpserver.sendmail(gmail_user, [to], msg.as_string())
   smtpserver.quit()

