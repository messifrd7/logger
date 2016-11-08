"""
monitor.py

Monitoring Application for Application's log file.
Log file is written to in append-only fashion.

"""

from argparse import ArgumentParser

def main():
	p=ArgumentParser()
	p.addArgument("log_file",help="file to write application logs to")
	args = p.parse_args()

	""" Consume the input log file
	Invoke parseLine() for each new line of log	"""
	while True:
		
		try:
			#for line in open(filename).xreadlines():
			#	parts = line.split(" ")
		
		except Exception e:
			print(str(e))



""" Parses a give line of the log
Calls send_email(msg) with all stats info when ERROR line has occurred """
def parseLine():
	pass

if __name__ == "__main__":
	main()