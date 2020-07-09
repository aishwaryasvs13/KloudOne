#alarm clock
import datetime


#set the time
hours = int(input("What hour do you want to wake up ?  "))
minutes = int(input("What minute do you want to wake up ? "))
amPm =  str(input("am or pm ? "))

if(amPm == "pm"):
    hours = hours + 12

while(True):
    if(hours == datetime.datetime.now().hour and minutes == datetime.datetime.now().minute):
        print("Wake up! You Lazy Lad!!")
        break

print("exited")

