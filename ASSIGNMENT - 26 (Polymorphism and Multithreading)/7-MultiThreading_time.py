# Write a python script to create a clock where 1st thread will print the current time every second and 2nd will print “1 Minute Completed” after every 1 minute.

from datetime import datetime
from threading import *
from time import sleep
class CurrentTime(Thread):
    def run(self):
        while(True):
            date_data = datetime.now()
            current_time = date_data.strftime("%H:%M:%S")
            print(current_time)
            sleep(1)

class Minute(Thread):
    def run(self):
        while(True):
            sleep(60)
            print("Minute Completed")

time = CurrentTime()
minute = Minute()
time.start()
minute.start()