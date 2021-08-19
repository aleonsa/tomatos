import sys
import datetime

def wlan_connect(ssid='MEGACABLE-079F', password='566J3RdD'):
    import network
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active() or not wlan.isconnected():
        wlan.active(True)
        print('connecting to:', ssid)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

wlan_connect()
datetime.correct_datetime()