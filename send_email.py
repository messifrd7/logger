"""
send_email implementation
Sends an email with the provided msg
@author: Shreyas Moudgalya{shreyas@hawk.iit.edu}
"""

from datetime import datetime
import smtplib
from email.mime.text import MIMEText

def send_email(msg):
	
	sender = 'smoudgal@hawk.iit.edu'
	receivers = ['shreyas@hawk.iit.edu']
	host = 'smtp.gmail.com'
	port = 587
	user = None
	password = None

	smtpObject = smtplib.SMTP(host,port)
	server.starttls() 
    #Check if user and password defined 
    if user and password: 
		server.login(user, password) 
	
	try:
		#smtpObject = smtplib.SMTP('localhost') #If there is a localhost SMTP Server
		smtpObject.sendmail(sender, receivers, message)
		print "Successfully sent email"
	except SMTPException:
		print "Error: unable to send email"