#clock
import time
import datetime

#implement graphics to design a clock
from turtle import *
setup()
t1 =  Turtle() #t1 will write the time


#set the time
hours = datetime.datetime.now().hour
minutes = datetime.datetime.now().minute
seconds = datetime.datetime.now().second


while(True):
    t1.clear()
    t1.write(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2), font = ("helvetica", 25, "normal" ))
    seconds =  seconds + 1
    time.sleep(1)
    if(seconds == 60):
        seconds = 0
        minutes = minutes + 1
    if(minutes == 60):
        minutes = 0
        hours =  hours + 1
