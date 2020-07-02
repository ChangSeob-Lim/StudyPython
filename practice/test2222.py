import serial
import smbus2
import bme280
import datetime
import time
import urllib.request
import pymysql

# 아두이노 연결
read_port = '/dev/ttyACM0'
write_port = '/dev/ttyUSB0'
brate = 9600
cmd = 'temp'

read_ser = serial.Serial(read_port, baudrate=brate, timeout=None)
write_ser = serial.Serial(write_port, baudrate=brate, timeout=None)
print(read_ser.name)
print(write_ser.name)

control = False

# 온습도 센서 Grove 연결
port = 1; address = 0x76
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus, address)

try:
    print('play')
    while True:
        try:
            if read_ser.in_waiting != 0:
                content = read_ser.readline()
                # print(content[:-2].decode())
                vals = content.decode('utf-8').replace('\r\n', '')
                print(vals)

                if vals == '1':
                    control = ~control
            
                if control:
                    write_ser.write(b'1')
                else:
                    write_ser.write(b'0')

                # time.sleep(0.5)

            wtime = datetime.datetime.now()
            data = bme280.sample(bus, address)
            t = data.temperature
            h = data.humidity
            p = data.pressure
            print('Temp = {0:0.1f}C Humid = {1:0.1f}% Pressure = {2:0.1f}'.format(t, h, p))
            time.sleep(1)
        except Exception as e:
            print(e)

except Exception as e:
    print('DB', e)