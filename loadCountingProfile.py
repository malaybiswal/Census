import requests
import xlrd
import sys
import traceback
import time
import datetime
from re import sub
from decimal import Decimal
import pymysql
import ssl

CustomerID = 3
BusinessID=1
CountingProfileName='Retail Foot Traffic'
CountingMeasure='Total'
Button1='Men'
Button2='Women'
Button3='Senior'
Button4='Kids'
sql="""INSERT INTO CountingProfile(CustomerID,BusinessID,countingProfileName,countingMeasure,button1,button2,button3,button4) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
conn = pymysql.connect(host='censuscountersdev.czywg4t7fvct.us-east-1.rds.amazonaws.com', unix_socket='/tmp/mysql.sock', user='Census', passwd='CensusCountersDEV123=6', db='CensusCountersDEV',use_unicode=True, charset="utf8")
cur = conn.cursor()

#for i in range(1,38):
for i in range(510,908):
    try:
        cur.execute(sql,(CustomerID,i,CountingProfileName,CountingMeasure,Button1,Button2,Button3,Button4))
    except:
        print("DB ERROR while inserting into icertdata table!!!!!!!!!!!!!!!!!!")

        tb = traceback.format_exc()
        print(tb)
conn.commit()
cur.close()
conn.close()
