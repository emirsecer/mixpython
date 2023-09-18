import sqlite3
import random
import time
import datetime

con=sqlite3.connect("dersler.db")

cursor=con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS tablo1 (zaman REAL, tarih TEXT, anahtarkelime TEXT, deger REAL )")

def rastgeledegerekle():
    zaman=time.time()
    tarih=str(datetime.datetime.fromtimestamp(zaman).strftime(" %Y %m %d"))
    anahtarkelime="python sqlite 3"
    deger=random.randrange(10,100)
    cursor.execute("INSERT INTO tablo1 (zaman,tarih,anahtarkelime,deger) VALUES(?,?,?,?)",(zaman,tarih,anahtarkelime,deger))
    con.commit()




def degerlerial():
    cursor.execute("SELECT * FROM tablo1 WHERE deger=1.0 " )
    data=cursor.fetchall()
    for i in data :
        print(i)

        con.commit()



def guncelle():
    cursor.execute("SELECT * FROM tablo1 ")
    data = cursor.fetchall()
    print("-------------ilk değerler---------------------")
    for i in data:
        print(i)
        cursor.execute("UPDATE tablo1 SET deger=99 WHERE deger =2 ")
        cursor.execute("SELECT * FROM tablo1 ")
        data = cursor.fetchall()
        print("-------------güncellenmiş değerler---------------------")
        for i in data:
            print(i)

        cursor.execute("DELETE FROM tablo1 WHERE deger=99 ")
        cursor.execute("SELECT * FROM tablo1 ")
        data = cursor.fetchall()
        print("-------------son  değerler---------------------")
        for i in data:
            print(i)

tabloolustur()
degerlerial()
guncelle()








i=0
while (i<10):
    rastgeledegerekle()
    time.sleep(5)
    i+=1
con.commit()
con.close()