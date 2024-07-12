import time
timeNow = time.strftime('%H:%M:%S')
print(timeNow)
if(timeNow > '06:00:00' and timeNow < '12.00.00'):
    print("Good Morning sir")
if(timeNow > '12.00.00' and timeNow < "13.00.00"):
    print("Good Noon sir")
if(timeNow > '13.00.00' and timeNow < '17.00.00'):
    print("Good Afternoon sir")
if(timeNow > '17.00.00' and timeNow < '19.00.00'):
    print("Good Evening sir")
if(timeNow > '19.00.00' and timeNow < '06.00.00'):
    print("Good Night sir")