from machine import Pin
from neopixel import NeoPixel

n = 12
p = 5

np = NeoPixel(Pin(p), n)

def clear():
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()

def set_color(r, g, b):
    for i in range(n):
        np[i] = (r, g, b)
    np.write()

clear()
while True:
    set_color(255, 0, 0)
    