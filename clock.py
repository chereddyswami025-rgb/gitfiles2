import datetime
import time 
import os

while True:
    a_t=input("enter alarm")
    now=datetime.datetime.now().strftime("%H:%M:%S")
    print(now)
    if now==a_t:
        print("time to wake")
    try:
        os.system("echo")
    except:
        pass 

    break

