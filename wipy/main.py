# main.py -- put your code here!

from mqtt import MQTTClient
from machine import Pin
import time

led = Pin('G16', mode=Pin.OUT, value=1)

def sub_cb(topic, msg):
    if topic.decode('utf-8') == 'garden/water' and msg.decode('utf-8') == 'toggle':
        led.toggle()
    print(str(topic), str(msg))

client = MQTTClient('wipy', '192.168.4.2')

client.set_callback(sub_cb)
client.connect()
client.subscribe(topic='garden/water')

while True:
    if True:
        client.wait_msg()
    else:
        client.check_msg()
        time.sleep(1)
client.disconnect()
