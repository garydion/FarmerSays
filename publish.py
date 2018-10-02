import sys
import time
import telnetlib
import paho.mqtt.client as mqtt

HOST = "io.adafruit.com"
PORT = "1883"
USERNAME = "topher_cantrell"
PASSWORD = "<ADAFRUIT.IO KEY>"
TOPIC = "topher_cantrell/feeds/quantum-farmer-chris"

client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.connect(HOST, PORT)
time.sleep(1)
client.publish(TOPIC, sys.argv[1])
