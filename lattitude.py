"""This Program reads Location data from excel spreadsheet(Assume data in Sheet1). Parse them get lattitude,
longitude and write excel data along with lattitude,longitude to another file. A error file also creates in same directory where lattitude and longitude data are unavailable.
Parse this new file inserts rows into Locations table
"""
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
file = open("/Users/mala0858/malay/python/Census/locationError.txt", "w")
CustomerID=3
BusinessType='Retail'
phone='+1-425-313-8100'
sql="""INSERT INTO Location(CustomerID,BusinessName,businessType,Address,City,State,Country,ZipCode,PhoneNumber,Latitude,Longitude) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
conn = pymysql.connect(host='censuscountersdev.czywg4t7fvct.us-east-1.rds.amazonaws.com', unix_socket='/tmp/mysql.sock', user='Census', passwd='CensusCountersDEV123=6', db='CensusCountersDEV',use_unicode=True, charset="utf8")
cur = conn.cursor()
#add='1600+Amphitheatre+Parkway,+Mountain+View,+CA'
def massage(str):
    str=str.strip()
    s=str.split()
    if(len(s)>=2):
        string=''
        for i in s:
            string=string+'+'+i
    #print(str,'----',string)
        return string[1:]
    else:
        return str

#add='Alpha+One+Mall,+Amritsar+Punjab+143010+India'
url='https://maps.googleapis.com/maps/api/geocode/json?address='

workbook = xlrd.open_workbook('/Users/mala0858/Downloads/CostcoLocations.xlsx')
worksheet = workbook.sheet_by_name('Locations')
j=1
with open('/Users/mala0858/malay/python/Census/location.txt','w') as f:
    for i in range(1,399):
        j=1
        data=''
        try:
            add1=worksheet.cell(i, j).value
            data=data+str(worksheet.cell(i, 0).value)+'-----'+add1
            adds=add1.split(',')
            if(len(adds)>1):
                #add=massage(adds[0])
                add=massage(adds[0])+"-----"+massage(adds[1])
            else:
                add=massage(add1)
            city=worksheet.cell(i, j+1).value
            data=data+'-----'+city
            city=city.strip()
            city=massage(city)
            state=worksheet.cell(i, j+2).value
            data=data+'-----'+state
            state=massage(state)
            zipcode=int(worksheet.cell(i, j+4).value)
            zipcode=str(zipcode)
            data=data+'-----'+zipcode
            zipcode=zipcode.strip()
            country=worksheet.cell(i, j+3).value
            data=data+'-----'+country
            country=country.strip()
            phone=worksheet.cell(i, j+6).value
            phone=str(phone)
            if(len(phone)<=1):
                phone=n/a

            data=data+'-----'+phone
            add=add+"+"+city+"+"+state+"+"+zipcode+"+"+country
            print(add)
            url='https://maps.googleapis.com/maps/api/geocode/json?address='
            url=url+add
            response = requests.get(url)

            resp_json_payload = response.json()
            lat=resp_json_payload['results'][0]['geometry']['location']['lat']
            lng=resp_json_payload['results'][0]['geometry']['location']['lng']
            data=data+'-----'+str(lat)+'-----'+str(lng)+'\n'
            print(lat,lng)
            #print(resp_json_payload['results'][0]['geometry']['location'])
            #data=str(worksheet.cell(i, 0).value)+","+str(add1)+","+str(worksheet.cell(i, 2).value)+","+str(worksheet.cell(i, 3).value)+","+str(worksheet.cell(i, 4).value)+","+str(worksheet.cell(i, 5).value)+","+lat+","+lng
            print(data)
            f.write(data)
            #time.sleep(1)
        except:
            print('ERROR')
            lat='n/a'
            lng='n/a'
            data=data+'-----'+lat+'-----'+lng+'\n'
            f.write(data)

            file.write(data)

            #time.sleep(1)
            tb = traceback.format_exc()
            print(tb)
file.close()

with open('/Users/mala0858/malay/python/Census/location.txt','r') as f:
    text=f.readlines()
    i=0
    for t in text:
        texts=t.strip().split('-----')
        BusinessName=texts[0]
        address=texts[1]
        city=texts[2]
        state=texts[3]
        zipcode=texts[4]
        country=texts[5]
        phone=texts[6]
        lat=texts[7]
        lng=texts[8]
        try:
            cur.execute(sql,(CustomerID,BusinessName,BusinessType,address,city,state,country,zipcode,phone,lat,lng))
        except:
            print("DB ERROR while inserting into icertdata table!!!!!!!!!!!!!!!!!!")
            #print('ERROR: %sn' %str(err))
            tb = traceback.format_exc()
            print(tb)
conn.commit()
cur.close()
conn.close()
#response = requests.get(url)

#resp_json_payload = response.json()

#print(resp_json_payload['results'][0]['geometry']['location'])
