import mysql.connector
import random

def makeCode(count,length):
    str = "abcdefghijklmnopqrstuvwxyz0123456789"
    result = []
    for x in range(count):
        randomStr = ''
        for y in range(length):
            randomStr = randomStr + random.choice(str)
        result.append(randomStr)

    return result
conn = mysql.connector.connect(user='root', password='tuzhenyu', database='test')
cursor = conn.cursor()
cursor.execute('create table if not exists codes(code char(64))')
for str in makeCode(200,10):
    cursor.execute('insert into codes values (%s)', [str])
conn.commit()
