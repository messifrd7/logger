"""
send_email implementation
Sends an email with the provided msg
"""

from datetime import datetime
import smtplib
from email.mime.text import MIMEText

def send_email(msg):
	
	sender = 'from@fromdomain.com'
	receivers = ['to@todomain.com']

	try:
		smtpObject = smtplib.SMTP('localhost')
		#smtpObject = smtplib.SMTP('mail.your-domain.com', 25)    #If you are not running an SMTP server on your local machine
		smtpObject.sendmail(sender, receivers, message)
		print "Successfully sent email"
	except SMTPException:
		print "Error: unable to send email"