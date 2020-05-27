import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT) # green
GPIO.setup(21, GPIO.OUT) # red

try:
    while True: # loop
        GPIO.output(20, True) # green on
        GPIO.output(21, False) # red off
        time.sleep(1)
        GPIO.output(20, False) # green off
        GPIO.output(21, True) # red on
        time.sleep(1)
except Exception as e:
    print(e)
finally:
    GPIO.cleanup()
    