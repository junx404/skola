# Exempelprogram för labb IoT datainsamling, GPP100
# Thomas L, dec 2020, use freely!
#
# Referenslänkar:
#   https://pypi.org/project/paho-mqtt/
#   https://thingsboard.io/docs/reference/mqtt-api/#telemetry-upload-api

import paho.mqtt.client as mqtt
import time, json, datetime
from sense_hat import SenseHat
from time import sleep
import math

ACCESS_TOKEN = "AccessTokenFromThingsboard"
MQTTURL = "thingsboard.port0.org"
MQTTPORT = 1883

# The callback for when the client receives a CONNACK response from the server.
# Just print the response from the server.
def on_connect(client, userdata, rc, *extra_params):
   print('Connected with result code '+str(rc))

client = mqtt.Client()
client.on_connect = on_connect

# ThingsBoard requires the device access token as the user name
client.username_pw_set(ACCESS_TOKEN)

# Connect with 60 seconds keepalive ping
client.connect(MQTTURL, MQTTPORT, 60)

# Start mqtt loop as separate thread to handle messaging
# in the background
client.loop_start()

sense = SenseHat()

while True:
    skakning = []
    for i in range(0,10):
        sleep(0.5)
        raw = sense.get_accelerometer_raw()
        x = raw['x']
        y = raw['y']
        z = raw['z']
        s = math.sqrt(x*x + y*y + z*z)
        skakning.append(s)

    skak = max(skakning) - min(skakning)
    skak *= 20
    timestamp_ms = int(time.time() * 1000)
    temp = sense.get_temperature()
    payload = {'ts':timestamp_ms, 'values':{'temperatur':temp, 'skakningar':skak}}
    client.publish('v1/devices/me/telemetry',json.dumps(payload), 1)

# Pseudokod:
#    läs accelerometer varje 0.5 sek
#    efter 5 sek:
#        beräkna max - min skakningar
#        läs temperatur
#        läs klockslag, beräkna timestamp
#        skicka till server:

# Data till servern bör ha följande utseende.
# timestamp_ms är vanlig unix-timestamp fast omskalat till
# millisekunder och omvandlad till ett heltal
#   payload = {'ts':timestamp_ms, 'values':{'temperatur':temp, 'skakningar':skak}}

# Skicka telemetridata json-formaterad till servern
# (sista argument 1 = QoS, means at least once failure semantics)
#   client.publish('v1/devices/me/telemetry',json.dumps(payload), 1)

# Sedan är det dags att börja om i loopen för nya 5 sekunder
