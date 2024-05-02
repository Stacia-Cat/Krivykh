import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time

def dec2bin(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

def adc(bits, comp):
    lvl = 0
    for i in range(bits-1, -1, -1):
        lvl = lvl + 2**i
        GPIO.output(dac, dec2bin(lvl))
        time.sleep(0.001)
        comp_val = GPIO.input(comp)
        if (comp_val == 1):
            lvl = lvl - 2**i
    return lvl

def num2_dac_leds(value):
    s = dec2bin(value)
    GPIO.output(dac, s)
    return s

dac = [8, 11, 7, 1, 0, 5, 12, 6]
bits = len(dac)
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

levels = 2**bits
maxV = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

volts = []
times = []

try:
    GPIO.output(troyka, 1)
    start_time = time.time()
    val = 0
    while (val < 200):
        val = adc(bits, comp)
        print(" Volts = {:3}".format(val/levels * maxV))
        num2_dac_leds(val)
        volts.append(val)
        times.append(time.time()-start_time)
    GPIO.output(troyka, 0)

    while (val > 192):
        val = adc(bits, comp)
        print(" Volts = {:3}".format(val/levels * maxV))
        num2_dac_leds(val)
        volts.append(val)
        times.append(time.time()-start_time)
    end_time = time.time()

    with open("settings7.txt", "w") as f:
        f.write(str((end_time - start_time)/len(volts)))
        f.write("\n")
        f.write(str(maxV/256))
    print(end_time-start_time, " secs\n", len(volts)/(end_time - start_time), "\n", maxV / 256)

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()

times_str = [str(i) for i in times]
volts_str = [str(i) for i in volts]

with open("data.txt", "w") as f:
    f.write("\n".join(volts_str))

plt.plot(times, volts)
plt.show()