"""
send_email implementation
Sends an email with the provided msg
@author: Shreyas Moudgalya{shreyas@hawk.iit.edu}
"""

#from datetime import datetime
import smtplib
#from email.mime.text import MIMEText

def send_email(msg):
	
	sender = 'shreyasmoudgalya064@gmail.com'
	receivers = ['shreyasmoudgalya009@gmail.com']
	host = 'smtp.gmail.com'
	port = 587
	user = 'shreyasmoudgalya064'
	password = 'ShrMoud123'

	#server = smtplib.SMTP(host,port)
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls() 
	#Check if user and password defined 
	if user and password: 
		server.login(user, password) 
	
	try:
		#server = smtplib.SMTP('localhost') #If there is a localhost SMTP Server
		server.sendmail(sender, receivers, message)
		print ("Successfully sent email")
	except SMTPException:
		print ("Error: unable to send email")

        server.close()

