import sys
import traceback
#import time
import datetime
from re import sub
from decimal import Decimal
import pymysql
from random import *
import time

start = time.time()
z=0
#file = open("/Users/mala0858/malay/python/Census/Counts.txt", "w")
selectsql= """select d.imei,l.Latitude,l.Longitude from Location l, Device d where l.CustomerID=d.customerID and l.BusinessID=d.businessID"""
conn = pymysql.connect(host='censuscountersdev.czywg4t7fvct.us-east-1.rds.amazonaws.com', unix_socket='/tmp/mysql.sock', user='Census', passwd='CensusCountersDEV123=6', db='CensusCountersDEV',use_unicode=True, charset="utf8")
cur = conn.cursor(pymysql.cursors.DictCursor)
imei=[];lat=[];lng=[]
try:
    cur.execute(selectsql)
    for row in cur:
        imei.append(row['imei'])
        lat.append(row['Latitude'])
        lng.append(row['Longitude'])
except:
    print("DB ERROR while inserting into icertdata table!!!!!!!!!!!!!!!!!!")

    tb = traceback.format_exc()
    print(tb)
countTime=""
sql="""insert into Counts(countTime,imei,button1Count,button2Count,button3Count,button4Count,latitude,longitude) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""

dt=datetime.datetime(2017,5,1,10,00,00)
loc=0
for i in range(1,32):
    dt=datetime.datetime(2017,5,i,10,00,00)
    for loc in range(0,len(lat)):
        dt=datetime.datetime(2017,5,i,10,00,00)
        for j in range(60,43320,60):
            print("****",dt.date(),dt.time())
            countTime=str(dt.date())+" "+str(dt.time())
            print("---",countTime)
            button1Count = randint(1, 20)
            button2Count = randint(1, 20)
            button3Count = randint(1, 20)
            button4Count = randint(1, 20)
            try:
                cur.execute(sql,(countTime,imei[loc],button1Count,button2Count,button3Count,button4Count,lat[loc],lng[loc]))
                #data=str(countTime)+','+str(imei[loc])+','+str(button1Count)+','+str(button2Count)+','+str(button3Count)+','+str(button4Count)+','+str(lat[loc])+','+str(lng[loc])+'\n'
                #file.write(data)
                dt=dt+datetime.timedelta(0,60)
            except:
                print("DB ERROR while inserting into icertdata table!!!!!!!!!!!!!!!!!!")

                tb = traceback.format_exc()
                print(tb)
        conn.commit()
        z+=1
        print('committed ',z,' times')
#file.close()
conn.commit()
cur.close()
conn.close()
end = time.time()
print("TOTAL TIME TAKEN:",end - start)
