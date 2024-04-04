import RPi.GPIO as GPIO
import time

def dec2bin(value):
    l = [0]*8
    for i in range(8):
        l[7-i] = value % 2
        value = value // 2
    return l

def adc():
    for i in range(256):
        dac_x = dec2bin(i)
        GPIO.output(dac, dac_x)
        comp_x = GPIO.input(comp)
        time.sleep(0.05)
        if comp_x:
            return i
    return 0

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        u = adc()
        U = u * 3.3 / 256.0
        if u:
            print('Value = {0}; Voltage = {1}'.format(u, U))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()