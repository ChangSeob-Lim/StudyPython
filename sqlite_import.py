# 바로 실행하지 말고 콘솔 창에서 폴더 위치 맞추고 ( > python sqlite_import.py student.csv )로 실행
from sys import argv
import csv
import sqlite3

conn = sqlite3.connect('sample.db')
c = conn.cursor()

if len(argv) < 2: # 아규먼트 에러
    print("Error!!")
    exit(1)
else: # 정상적인 실행
    csvfile = argv[1]
    print(csvfile)
    c.execute('CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY AUTOINCREMENT, \
             name TEXT, birth DATE, gender CHAR )')
    student = csv.reader(open(csvfile, 'r'), delimiter=',', quotechar='"')
    
    for row in student:
        print('%s' % (row)) #print('{}'.format(row))
        c.execute('INSERT INTO student (name, birth, gender) VALUES (?, ?, ?)', (row[0], row[1], row[2]))

    conn.commit()
    conn.close()
    exit(0)