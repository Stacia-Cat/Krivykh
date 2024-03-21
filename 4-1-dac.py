import RPi.GPIO as GPIO

def decimal2binary(value):
    l = [0]*8
    for i in range(8):
        l[7-i] = value % 2
        value = value // 2
    return l

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        num = input("Enter a number from 0 to 255: ")
        try:
            num = int(num)
            if (0 <= num) and (num <= 255):
                GPIO.output(dac, decimal2binary(num))
                voltage = float(num) / 256.0 * 3.3
                print("Output voltage is about","{:.4f}".format(voltage))
            elif (num < 0) or (num > 255):
                GPIO.output(dac, 0) 
                print("Number should not be out of range [0;255]. Try again")
        except Exception:
            if (num == "q"):
                print("Stopped")
                break
            GPIO.output(dac, 0)
            print("You should write a number. Try again")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()