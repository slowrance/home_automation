# boot.py -- run on boot-up
import os
import machine
from network import WLAN
uart = machine.UART(0, 115200)
os.dupterm(uart)


wlan = WLAN(mode=WLAN.STA)

if not wlan.isconnected():
    wlan.connect(ssid='SLOW2', auth=(WLAN.WPA2, '7dVV5twSLx4E'), timeout=5000)
    while not wlan.isconnected():
        machine.idle()
        print('WLAN conection status: ' + str(wlan.isconnected()))
