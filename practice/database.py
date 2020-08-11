import random
import datetime
import time
import pymysql

try:
    conn = pymysql.connect(host='192.168.0.173', user='root', password='mysql_p@ssw0rd', \
                         db='testdb', charset='utf8') # input to MySQL in PKNU host
    while True:
        try:
            wtime = datetime.datetime.now() # Time Now
            
            curs = conn.cursor() # cursor
            query = "INSERT INTO testtbl (number, time) \
                 VALUES (%s, %s)"
            data = (random.randint(1,100), wtime.strftime("%Y-%m-%d %H:%M:%S")) # 1~100 random number + Time
            curs.execute(query, data)
            conn.commit()
            time.sleep(1) # play 1 sec

            print('playing') # Check play
        except Exception as e:
            print('play error', e)

except Exception as e:
    print('DB', e) # Print Error
finally:
    curs.close()
    conn.close()