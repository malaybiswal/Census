import datetime
from re import sub
from decimal import Decimal
import pymysql
import ssl
import sys
import traceback
name='Costco'
addr='999 Lake Drive'
city='Issaquah'
country='USA'
zipcode='98027'
state='Washington'
username='shopper@costco.com'
password='costco'
phone='+1-425-313-8100'

sql="""INSERT INTO Customer(name,Address,city,state,country,zip,phone,username,password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
conn = pymysql.connect(host='censuscountersdev.czywg4t7fvct.us-east-1.rds.amazonaws.com', unix_socket='/tmp/mysql.sock', user='Census', passwd='CensusCountersDEV123=6', db='CensusCountersDEV',use_unicode=True, charset="utf8")
cur = conn.cursor()
try:
    cur.execute(sql,(name,addr,city,state,country,zipcode,phone,username,password))
except:
    print("DB ERROR while inserting into icertdata table!!!!!!!!!!!!!!!!!!")
    #print('ERROR: %sn' %str(err))
    tb = traceback.format_exc()
    print(tb)
conn.commit()
cur.close()
conn.close()
