import datetime
from re import sub
from decimal import Decimal
import pymysql
import ssl
import sys
import traceback
import xlrd

CustomerID=2
BusinessName='Shopper Stop'
BusinessType='retail'
address=''
city=''
state=''
country=''
zipcode=''
lattitude=50.5
longitude=45.5
phone='+1-425-313-8100'

sql="""INSERT INTO Location(CustomerID,BusinessName,businessType,Address,City,State,Country,ZipCode,PhoneNumber,Latitude,Longitude) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
conn = pymysql.connect(host='host', unix_socket='/tmp/mysql.sock', user='user', passwd='pwd', db='db',use_unicode=True, charset="utf8")
cur = conn.cursor()



workbook = xlrd.open_workbook('/Users/mala0858/Downloads/ShoppersStopLocations-1.xlsx')

worksheet = workbook.sheet_by_name('Sheet1')
j=0
for i in range(1,38):
    try:
        BusinessName=worksheet.cell(i, j).value
        address=worksheet.cell(i, j+1).value
        city=worksheet.cell(i, j+2).value
        state=worksheet.cell(i, j+3).value
        zipcode=worksheet.cell(i, j+4).value
        country=worksheet.cell(i, j+5).value
        j=0
        cur.execute(sql,(CustomerID,BusinessName,BusinessType,address,city,state,country,zipcode,phone,lattitude,longitude))
    except:
        print("DB ERROR while inserting into icertdata table!!!!!!!!!!!!!!!!!!")
        #print('ERROR: %sn' %str(err))
        tb = traceback.format_exc()
        print(tb)
#r=worksheet.cell(1, 4).value
#print(r)
conn.commit()
cur.close()
conn.close()
#with open("/Users/mala0858/Downloads/ShoppersStopLocations.csv","r") as f:
#    for line in f:
#        print(line)
