import gc
import time
import ujson
import ubinascii
import network
import esp
import machine, time
from neopixel import NeoPixel
from umqttsimple import MQTTClient
from machine import Pin
from time import sleep

# Bleu G5
# Violet GND
# Vert 5V

n = 12
p = 5 # PIN G5

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
#try:
#    with open('secrets.json') as fp:
#        secrets = ujson.loads(fp.read())
#except OSError as e:
#    print("secrets.json file is missing")
#    restart_and_reconnect()

# Connect network
# try:
#     connect_network(secrets["wifi"]["ssid"], secrets["wifi"]["password"])
#     mqtt_client = connect_mqtt(secrets["mqtt"]["url"], secrets["mqtt"]["login"], secrets["mqtt"]["password"])
# except OSError as e:
#     print("Network connection is not possible")
#     restart_and_reconnect()
print("soil")


addr_i2c = 0x20

#from machine import I2C
#import machine
#i2c = I2C(scl=Pin(22), sda=Pin(21), mode=I2C.SLAVE)

from pyb import I2C
SLAVE_ADDRESS = 0x42
BAUDRATE = 100000

i2c_slave = I2C(1, I2C.SLAVE, addr=SLAVE_ADDRESS, baudrate=BAUDRATE)
i2c_slave.write(0x20, 6)


# addr = i2c.scan()
# print("size: "+ str(len(addr)))
# for i in addr:
#     print("addr : " + str(i))

print("start")
clear()
#while True:
   # print('val : '+ soil_sensor.read())
    #sleep(0.1)
#    set_color(255, 0, 0)
    