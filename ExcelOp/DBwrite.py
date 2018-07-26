import xlwt
import pymysql

conn = pymysql.connect(user='root', password='989044', host='localhost', port=3306, db='Excel')
cur = conn.cursor()

cur.execute('create table empinfo8(name VARCHAR(15),add VARCHAR(15),state VARCHAR(20)')
cur.execute('insert into empinfo8 values(\'Ashish\',\'Pune\',\'Maharashtra\')')
cur.execute('insert into empinfo8 values(\'Ashish\',\'Pune\',\'Maharashtra\')')
cur.execute('insert into empinfo8 values(\'Ashish\',\'Pune\',\'Maharashtra\')')
cur.execute('insert into empinfo8 values(\'Ashish\',\'Pune\',\'Maharashtra\')')
cur.execute('select * from empinfo8')

print(cur.fetchmany(3))

cur.commit()

cur.close()
conn.close()

