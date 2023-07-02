from datetime import datetime,date
import winsound
import time

def alarm():
    
    today = date.today()
    dateStr = today.strftime("%m/%d/%y")
        
    hour = int(input("enter hour(24 hr format): "))
    minute = int(input("enter minute: "))
    second = 0
    
    timeStr = f"{dateStr} {hour}:{minute}:{second}"
    timeObj = datetime.strptime(timeStr,'%m/%d/%y %H:%M:%S')
    
    timeInStr = str(timeObj)
    
    onlyTime = timeInStr.split(" ")
    
    while True:
        
        now = datetime.now()
        currTime = now.strftime("%H:%M:%S")
        print(currTime)
        time.sleep(1)
        
        if currTime == onlyTime[-1]:
            winsound.Beep(200,2000)
            break

#     winsound.Beep(200,2000)
alarm()