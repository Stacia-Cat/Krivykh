import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

p = GPIO.PWM(21, 1000)
p.start(0)

try:
    while True:
        f = int(input("Enter: "))
        p.ChangeDutyCycle(f)
        print(f*3.3/100)

finally:
    p.stop()
    GPIO.output(21, 0)
    GPIO.cleanup()