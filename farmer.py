import network
from umqtt.simple import MQTTClient
import os
import gc
import sys
import time
import board
import bitbangio
import adafruit_mcp230xx

i2c = bitbangio.I2C(board.SCL, board.SDA)
mcp = adafruit_mcp230xx.MCP23017(i2c)

# WiFi connection information
WIFI_SSID = '<SSID>'
WIFI_PASSWORD = '<wifipassword>'

# turn off the WiFi Access Point
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

# connect the device to the WiFi network
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

# wait until the device is connected to the WiFi network
MAX_ATTEMPTS = 20
attempt_count = 0
while not wifi.isconnected() and attempt_count < MAX_ATTEMPTS:
    attempt_count += 1
    time.sleep(1)

if attempt_count == MAX_ATTEMPTS:
    print('could not connect to the WiFi network')
    sys.exit()

# create a random MQTT clientID
random_num = int.from_bytes(os.urandom(3), 'little')
mqtt_client_id = bytes('client_'+str(random_num), 'utf-8')

# connect to Adafruit IO MQTT broker using unsecure TCP (port 1883)
ADAFRUIT_IO_URL = b'io.adafruit.com'
CHRIS_USERNAME = b'<CHRIS"S_USERNAME>'
ADAFRUIT_USERNAME = b'<MY_USERNAME>'
ADAFRUIT_IO_KEY = b'<MY_IO_KEY>'
ADAFRUIT_IO_QFG_FEEDNAME = b'Quantum_Farmer_Gary'
ADAFRUIT_IO_QFC_FEEDNAME = b'quantum-farmer-chris'

client = MQTTClient(client_id=mqtt_client_id,
                    server=ADAFRUIT_IO_URL,
                    user=ADAFRUIT_USERNAME,
                    password=ADAFRUIT_IO_KEY,
                    ssl=False)

try:
    client.connect()
except Exception as e:
    print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
    sys.exit()

# the following function is the callback which is
# called when subscribed data is received
def cb(topic, msg):
#    print('Received Data: Topic = {}, Msg = {}\n'.format(topic, msg))
    try:
        index = animals2.index("".join(map(chr, msg)))
#        print(index)
        reset.value = False
        animals1[index].switch_to_output(value=True)
        mot.value = True
        time.sleep(0.2)
        animals1[index].switch_to_input()
        time.sleep(5)
        reset.value = True
        mot.value = False
    except:
#        print('Error')
        pass

# format of feed name: "ADAFRUIT_USERNAME/feeds/ADAFRUIT_IO_FEEDNAME"
mqtt_outgoing_feedname = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, ADAFRUIT_IO_QFG_FEEDNAME), 'utf-8')
mqtt_incoming_feedname = bytes('{:s}/feeds/{:s}'.format(CHRIS_USERNAME, ADAFRUIT_IO_QFC_FEEDNAME), 'utf-8')
client.set_callback(cb)
client.subscribe(mqtt_incoming_feedname)

Sheep = mcp.get_pin(8)     # Sheep
Turkey = mcp.get_pin(9)     # Turkey
Cat = mcp.get_pin(10)    # Cat
Bird = mcp.get_pin(11)    # Bird
Cow = mcp.get_pin(12)    # Cow
Pig = mcp.get_pin(13)    # Pig
Rooster = mcp.get_pin(14)    # Rooster
Coyote = mcp.get_pin(15)    # Coyote
Horse = mcp.get_pin(0)     # Horse
Frog = mcp.get_pin(1)    # Frog
Duck = mcp.get_pin(2)    # Duck
Dog = mcp.get_pin(3)    # Dog
reset = mcp.get_pin(4)  # Reset
mot = mcp.get_pin(5)    # Motor

animals1 = [Sheep, Turkey, Cat, Bird, Cow, Pig,
            Rooster, Coyote, Horse, Frog, Duck, Dog]
animals2 = ["Sheep", "Turkey", "Cat", "Bird", "Cow", "Pig",
            "Rooster", "Coyote", "Horse", "Frog", "Duck", "Dog"]

reset.switch_to_output(value=True)
mot.switch_to_output(value=False)

Check_subscription_period_in_seconds = 2
Loop_time = 0.1
accum_time = 0

# if True:
while True:
    for x in range (0, 12):
        if animals1[x].value == True:
            while animals1[x].value == True:
                pass
#            print('Button: {0}'.format(animals1[x].value))
            client.publish(mqtt_outgoing_feedname, bytes(str(animals2[x]), 'utf-8'), qos=0)
            reset.value = False
            animals1[x].switch_to_output(value=True)
            mot.value = True
            time.sleep(0.2)
            animals1[x].switch_to_input()
            time.sleep(5)
            reset.value = True
            mot.value = False

    time.sleep (Loop_time)
    accum_time += Loop_time
    if (accum_time >= Check_subscription_period_in_seconds):
        print('Going to check now')
        # Subscribe.  Non-blocking check for a new message.
        try:
            client.check_msg()
        except:
            pass
        accum_time = 0
        print('Done checking')

sys.exit()
