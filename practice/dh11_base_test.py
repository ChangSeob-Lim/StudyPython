import Adafruit_DHT as dht
import time
sensor = dht.DHT11
pin = 4
try:
    while True:
        h, t = dht.read_retry(sensor, pin)
        if h is not None and t is not None:
            print('Temp = {0:0.1f}C Humi = {1:0.1f}%'.format(t, h))
        else:
            print('Read error')
        time.sleep(1)
except KeyboardInterrupt:
    print("Terminated by Keyborad")
finally:
    print("End of program")