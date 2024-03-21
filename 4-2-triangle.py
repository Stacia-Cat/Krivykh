import RPi.GPIO as GPIO
import time

def dec2bin(value):
    l = [0]*8
    for i in range(8):
        l[7-i] = value % 2
        value = value // 2
    return l

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

k = 1
x = 0

try:
    T = float(input("Enter a period: "))
    while True:
        GPIO.output(dac, dec2bin(x))

        if x == 0:
            k = 1
        elif x == 255:
            k = 0
        
        if k == 1:
            x = x + 1
        else:
            x = x - 1
        
        time.sleep(T/10)
except ValueError:
    GPIO.output(dac, 0)
    print("Wrong period")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()