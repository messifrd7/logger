# Python Monitoring Application 
Logger and Email Sender

## How to run
### Initially run the Producer Sample Code 
python3 log_generator.py logfile.txt
####Note: Kindly use the file name as "logfile.txt" 
### Next, run the Consumer Code
python3 monitor.py

An email is sent every time the Producer logs ERROR Code.