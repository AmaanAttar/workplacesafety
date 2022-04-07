import pyfirmata
import time
import cv2
from detect2 import run
from detect2 import parse_opt

port = 'com3'
board=pyfirmata.Arduino(port)

led_1=board.get_pin('d:13:o')
led_2=board.get_pin('d:12:o')

def light1(det):
    if len(det) == 2:
        led_1.write(1)
    else:
        led_1.write(0)

def light2(det):
    if len(det) == 0:
        led_2.write(1)
    else:
        led_2.write(0)