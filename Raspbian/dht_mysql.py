import Adafruit_DHT as dht
import datetime
import time
import urllib.request
import pymysql

sensor = dht.DHT11
pin = 4
print('Reading Temperature&Humidity')
# DB저장

try:
    conn = pymysql.connect(host='210.119.12.52', user='test_usr', password='mysql_p@ssw0rd', \
                         db='shopdb', charset='utf8')

    while True:
        wtime = datetime.datetime.now()
        humid, temp = dht.read_retry(sensor, pin)

        if humid is not None and temp is not None:
            print(wtime, 'Temp={0:0.1f}C Humidity={1:0.1f}%'.format(temp, humid))

            curs = conn.cursor()
            query = "INSERT INTO shopdb.iotmachine (currents_time, machine_id, temperature, humidity) \
                 VALUES (%s, %s, %s, %s)"
            data = (wtime.strftime("%Y-%m-%d %H:%M:%S"), 'LCS', temp, humid)
            curs.execute(query, data)
            conn.commit()

            time.sleep(10)
        else:
            print('Failed to get reading. Try again')
except Exception as e:
    print("{}".format(e))
finally:
    curs.close()
    conn.close()