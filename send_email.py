"""
send_email implementation

"""

from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
with open(textfile) as fp:
    # Create a text/plain message
    msg = MIMEText(fp.read())

msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = shreyas@hawk.iit.edu
msg['To'] = shreyas@hawk.iit.edu

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()

#"""
#GLOBAL_TOTAL = 0

#def send_email(msg):
	#"""
	#email info here
	#"""
	
	#global GLOBAL_TOTAL
	#GLOBAL_TOTAL += 1
	
	#print(
	
	#"""\
	##########################################
	##			SERVER ALERT				##
	##										##
	##received: {date:%Y-%m-%d %H:%M:%S.%f} ##
	##total_alerts: {total:7d}				##
	##########################################
	#{msg}""". format(date=datetime.now(), total=GLOBAL_TOTAL,msg=msg)
			
#	)
#"""
