import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def send_msg(topic, msg):
    client.publish(topic, msg)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()

while True:
    topic = input("Enter your topic (garden/water): ")
    msg = input("Enter your message: ")
    if not topic:
        topic = 'garden/water'
    if not msg:
        print('You must enter a message!')
        break
    send_msg(topic, msg)
