import firebase
from machine import RTC, Pin
import time

URL = 'tomatos-w-default-rtdb'
p2 = Pin(2, Pin.OUT)
p2.off()

#print(data['time'])
#print(data['days'])
#print(data['hour'])

rtc = RTC()
#print(rtc.datetime())
data = firebase.get(URL)['config']
db_time = rtc.datetime()[4]
curr_min = rtc.datetime()[5]

def water(timeWater):
    p2.on()
    time.sleep(timeWater*60)
    p2.off()

while(True):
        
    if (db_time != rtc.datetime()[4]):
        data = firebase.get(URL)['config']
        db_time = rtc.datetime()[4]
    
    if (rtc.datetime()[5] != curr_min):
        curr_min = rtc.datetime()[5]
        hour = int(data['hour'][0:2])
        minute = int(data['hour'][3:])
        if(data['days'][rtc.datetime()[3]] == True and (hour == rtc.datetime()[4] and minute == rtc.datetime()[5])):
            water(int(data['time']))
            

            
            
    
  
  
#db psswd: QWROalwZ9ULXJ6smEbVY0XaXQ0ZWbscD6rE2tJWU
#db url: https://tomatos-w-default-rtdb.firebaseio.com