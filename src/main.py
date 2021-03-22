import gc
import time
import ujson
import ubinascii
import network
import esp
import machine
from neopixel import NeoPixel
from umqttsimple import MQTTClient

esp.osdebug(None)
gc.collect()

n = 12
p = 5

np = NeoPixel(machine.Pin(p), n)

def clear():
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()

def set_color(r, g, b):
    for i in range(n):
        np[i] = (r, g, b)
    np.write()

def connect_network(network_ssid: str, network_password: str) -> None:
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(network_ssid, network_password)

    while station.isconnected() == False:
        pass

    print('Connection Network successful')

def connect_mqtt(mqtt_server_addr: str, mqtt_login: str, mqtt_password: str) -> MQTTClient:

    # import usocket
    # ip = usocket.getaddrinfo('blackpearl.local', 9000)[0][-1][0]
    #ip = usocket.getaddrinfo('www.micropython.org', 80)[0][-1][0] 

    client_id = ubinascii.hexlify(machine.unique_id())
    print('MQTTBROKER: %s' %mqtt_server_addr)
    client = MQTTClient(client_id, mqtt_server_addr, port=1883, user=mqtt_login, password=mqtt_password)
    client.connect()
    print('Connected to %s MQTT broker' % (mqtt_server_addr))
    return client

def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(2)
    machine.reset()

# Read secret
try:
    with open('secrets.json') as fp:
        secrets = ujson.loads(fp.read())
except OSError as e:
    print("secrets.json file is missing")
    restart_and_reconnect()

# Connect network
# try:
#     connect_network(secrets["wifi"]["ssid"], secrets["wifi"]["password"])
#     mqtt_client = connect_mqtt(secrets["mqtt"]["url"], secrets["mqtt"]["login"], secrets["mqtt"]["password"])
# except OSError as e:
#     print("Network connection is not possible")
#     restart_and_reconnect()


clear()
while True:
    set_color(255, 0, 0)
    