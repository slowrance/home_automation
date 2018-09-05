import paho.mqtt.client as mqtt
import ssl

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def send_msg(client, topic, msg):
    client.publish(topic, msg)


TLS_CERT_PATH = '/home/pi/home_automation/ssl/m2mqtt_ca.crt'
TLS_PORT = 8883

def send_message():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.tls_set(ca_certs=TLS_CERT_PATH, certfile=None, 
               keyfile=None, cert_reqs=ssl.CERT_NONE, 
               tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
    client.tls_insecure_set(True)



    client.connect("localhost", TLS_PORT, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
    client.loop_start()


    topic = 'garden/water'
    msg = 'stop'
    send_msg(client, topic, msg)

    client.loop_stop()
    client.disconnect()

if __name__ == '__main__':
    send_message()

