
import sys
import traceback
import time
import datetime
from re import sub
from decimal import Decimal
import pymysql
imei=1234567890123456
DateReceived='2015-05-01'
selectsql= """select CustomerID,BusinessID,countingProfileID from CountingProfile"""
conn = pymysql.connect(host='host', unix_socket='/tmp/mysql.sock', user='user', passwd='pwd', db='db',use_unicode=True, charset="utf8")
cur = conn.cursor(pymysql.cursors.DictCursor)
CustomerIDs=[];BusinessIDs=[];countingProfileIDs=[]
try:
    cur.execute(selectsql)
    for row in cur:
        CustomerIDs.append(row['CustomerID'])
        BusinessIDs.append(row['BusinessID'])
        countingProfileIDs.append(row['countingProfileID'])
except:
    print("DB ERROR while inserting into icertdata table!!!!!!!!!!!!!!!!!!")

    tb = traceback.format_exc()
    print(tb)

#cur.close()
#conn.close()
print(len(countingProfileIDs))
sql="""insert into Device(customerID,businessID,dateReceived,imei,countingProfileID) VALUES (%s, %s, %s, %s, %s)"""
i=0
for i in range(0,len(countingProfileIDs)):
    try:
        cur.execute(sql,(CustomerIDs[i],BusinessIDs[i],DateReceived,imei,countingProfileIDs[i]))
        i+=1
        imei+=1
    except:
        print("DB ERROR while inserting into icertdata table!!!!!!!!!!!!!!!!!!")

        tb = traceback.format_exc()
        print(tb)
conn.commit()
cur.close()
conn.close()
