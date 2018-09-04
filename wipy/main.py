# main.py -- put your code here!

from mqtt import MQTTClient
from machine import Pin
from machine import Timer
# from network import WLAN
import utime
import ussl as ssl

# wlan = WLAN(mode=WLAN.STA)
#
# if not wlan.isconnected():
#     wlan.connect('slow2', auth=(WLAN.WPA2, '7dVV5twSLx4E'), timeout=5000)
#     while not wlan.isconnected():
#         machine.idle()
#         print('WLAN conection status: ' + str(wlan.isconnected()))

led = Pin('G16', mode=Pin.OUT, value=1)

def sub_cb(topic, msg):
    if topic.decode('utf-8') == 'garden/water' and msg.decode('utf-8') == 'toggle':
        led.toggle()
    if topic.decode('utf-8') == 'garden/water' and msg.decode('utf-8') == 'start':
        led.value(1)
        led_timer = Timer.Alarm(lambda t: led.value(0), 5, periodic=False)
        # led_timer = Timer(1)
        # led_timer.init(mode=Timer.ONE_SHOT)
        # timer_a = led_timer.channel(Timer.A, freq=1000, period=5000)
        # timer_a.irq(handler=lambda t: led.value(0), trigger=Timer.TIMEOUT)
    if topic.decode('utf-8') == 'garden/water' and msg.decode('utf-8') == 'stop':
        led.value(0)



    print(str(topic), str(msg))


TLS_CERT_PATH = '/ssl/m2mqtt_ca.crt'
TLS_PORT = 8883
SSL_PARAMS = {'cert_reqs':ssl.CERT_NONE, 'ca_certs':'TLS_CERT_PATH'}
client = MQTTClient('WiPy', server='172.16.1.91', port=TLS_PORT, ssl=True,
                    ssl_params=SSL_PARAMS)

client.set_callback(sub_cb)
# client.tls_set(ca_certs=TLS_CERT_PATH, certfile=None,
#                 keyfile=None, cert_reqs=ssl.CERT_NONE,
#                 tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

client.connect()
client.subscribe(topic='garden/water')

while True:
    if True:
        client.wait_msg()
    else:
        client.check_msg()
        time.sleep(1)
client.disconnect()
