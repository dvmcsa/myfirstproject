import socket
flukelist = ['34.225.25.86', '34.206.132.62', '54.86.189.185', '54.84.181.170']
#create an empty list for nslookup results#
nslookupresults = []
#loop lookup 20 times#
for i in range(0,20):
    nslookup = socket.gethostbyname("lms.lausd.net")
    nslookupresults.append(nslookup)

lmsips = list(set(nslookupresults))


faillist = []
for each in lmsips:
    if each not in flukelist:
        faillist.append(each + " FAIL")
    else:
        faillist.append(each + " PASS")

body = str(faillist)
print(body)

import smtplib

sender = 'no-reply@lausd.net'
receivers = ['jesus.delval@lausd.net']

message = """From: From Person <no-reply@lasud.net>
To: To Person <jesus.delval@lausd.net>
Subject: FLUKE LMS NSLOOKUP

Current NSLOOKP for lms.lausd.net: \n.
"""

try:
   smtpObj = smtplib.SMTP('mailout.lausd.net', 25)
   smtpObj.sendmail(sender, receivers, message + body)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")


