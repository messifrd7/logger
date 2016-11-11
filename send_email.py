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
	receivers = 'tprasad@hawk.iit.edu' #Make as list if multiple
	host = 'smtp.gmail.com'
	port = 587
	user = 'shreyasmoudgalya064'
	password = 'ShrMoud123'

	server = smtplib.SMTP(host,port)
	server.ehlo()
	server.starttls() 
	

	try:
		if user and password: 
			server.login(user, password) 
	except Exception as e:
		print("Unable to Login")


	try:
		server.sendmail(sender,receivers,msg)
		print ("Successfully sent email")
	except Exception as smtpE:
		print ("Error: unable to send email")

	server.close()

