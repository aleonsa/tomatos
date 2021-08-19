import ntptime
import time
from machine import RTC

def correct_datetime():
    #defining the time with the ntp server (is +5hrs)
    ntptime.host = "1.north-america.pool.ntp.org"
    try:
      ntptime.settime()
      #print("Local time after synchronization：%s" %str(time.localtime()))
    except:
      print("Error syncing time")
    
    datetime_elements = [0,0,0,0,0,0,0,0] # (year, month, mday, hour, minute, second, wday, yday)
    datetime_elements[0] = time.localtime()[0]
    datetime_elements[1] = time.localtime()[1]
    datetime_elements[2] = time.localtime()[2]
    datetime_elements[3] = time.localtime()[3] - 5
    datetime_elements[4] = time.localtime()[4]
    datetime_elements[5] = time.localtime()[5]
    datetime_elements[6] = time.localtime()[6]
    datetime_elements[7] = time.localtime()[7]
    
    if(datetime_elements[3] < 0):
        datetime_elements[3] = 24 + (time.localtime()[3] - 5)
        datetime_elements[2] = time.localtime()[2] - 1
        datetime_elements[6] = time.localtime()[6] - 1
        if(datetime_elements[6]==-1):
            datetime_elements[6] = 6
        datetime_elements[7] = time.localtime()[7] - 1
        if(datetime_elements[2] == 0):
            datetime_elements[1] =  time.localtime()[1] - 1
            #checking the year
            if(datetime_elements[1] == 0):
                datetime_elements[0] = time.localtime()[0] - 1
                datetime_elements[1] = 12
                if is_leap(datetime_elements[0]) == True:
                    datetime_elements[7] = 366
                else:
                    datetime_elements[7] = 365
            else:
                datetime_elements[0] = time.localtime()[0]
                datetime_elements[1] = time.localtime()[1]
            #checking the month    
            if(datetime_elements[1] == 1 or datetime_elements[1] == 3 or datetime_elements[1] == 5 or datetime_elements[1] == 7 or datetime_elements[1] == 8 or datetime_elements[1] == 10 or datetime_elements[1] == 12):
                datetime_elements[2] = 31
            elif(datetime_elements[1] == 4 or datetime_elements[1] == 6 or datetime_elements[1] == 9 or datetime_elements[1] == 11):
                datetime_elements[2] = 30
            elif(datetime_elements[1] == 2): #leap-year
                if is_leap(datetime_elements[0]) == True:
                    datetime_elements[2] = 29
                else:
                    datetime_elements[2] = 28
    rtc = RTC() #
    correct = (datetime_elements[0], datetime_elements[1], datetime_elements[2], datetime_elements[6], datetime_elements[3], datetime_elements[4], datetime_elements[5], 0)
    print(correct)
    rtc.datetime(correct)
    return rtc.datetime()
    
def is_leap(year):
    if year % 4 != 0: #no divisible entre 4
        return False
    elif year % 4 == 0 and year % 100 != 0: 
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: 
        return False
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: 
        return True
