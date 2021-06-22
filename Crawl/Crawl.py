import bs4
import requests
import pyodbc
import sqlalchemy
import urllib3
import mysql.connector as mysql
import sqlite3
from sqlalchemy import create_engine
import xlrd
import pandas as pd
import openpyxl
import json
### establish and manipulate sql with python

#######################################
# Connect to mysql database
# mydb = mysql.connect(
#     # always : localhost
#     host="localhost",
#     # always : root
#     user="root",
#     # password for sql db
#     passwd="",
#     # points toward targeted database: relevant only after creating the database
#     database="Luftschadstoffbelastung"
# )
# sqlite3 connection
conn=sqlite3.connect('Luftschadstoffbelastung')
# prove that connection is established
# print (mydb)

########################################

#### Manipulate

# initialize command/storing structure
mycursor = mydb.cursor()

# execute sql commands
#

# create database
# mycursor.execute("Create Database testdb")


# collect all databases: proof of existence
# mycursor.execute("show Databases")
# print result
# for db in mycursor:
#    print (db)

# create table
# mycursor.execute("create table pyschadstoff (Stationscode integer(10), Stationsname Varchar(30), Verschmutzung Integer(10))")

# collect all table data: proof of existence
# mycursor.execute("show tables")
# for tb in mycursor:
#     print(tb)

#######################################################################################################################
#######################################################################################################################

### fetch from excel



# manual scraping
#### writo to excel file
###chose date range in june 2021
# for i in range(15, 21):
#     r = requests.get('https://www.umweltbundesamt.de/api/air_data/v2/measures/csv?date_from=2021-06-'+ str(i) + '&time_from=12&date_to=2021-06-20&time_to=12&data%5B0%5D%5Bco%5D=3&data%5B0%5D%5Bsc%5D=3&lang=de')
#
# # # gets commands/items on webpage
# # # print(help(r))
# #
# # write as csv file and store on in project folder
#     with open('Luftverschmutzung'+ str(i) + '.csv', 'wb' ) as f:
#          f.write(r.content)

#print text in unicode(html)
#print(r.text)


##########################################################

###### use newly created excel files to fill sql table
# pd.set_option('display.max_columns', None)   #or 1000
# pd.set_option('display.max_rows', None)   #or 1000
# pd.set_option('display.max_colwidth', -1)   #or 199

# read the excel files



##read all excel and store in sql
# for i in range(15, 21):
#     df = pd.read_csv('Luftverschmutzung'+str(i)+'.csv', delimiter=';',  error_bad_lines=False)
# #print(df)
# #print(df.head())
#     engine = sqlalchemy.create_engine('mysql+pymysql://root:Admiral01!@localhost:3306/Luftschadstoffbelastung')
#
#     df.to_sql('test1', con=engine, if_exists='append')
#

# df= pd.DataFrame({"a":[1,2,3]})
# print(df)
#df.to_sql('test1', con=conn, if_exists='replace')

     #get sheet names(we only have one)
# sheet_names = xls.sheet_names
#      #get info for one sheet
# df = pd.read_excel(xls, "Events")
# df.tail()








# API Scraping

# api_key= None;

##

# https://www.umweltbundesamt.de/api/air_data/v2/airquality/json?date_from=2019-08-01&date_to=2019-08-01&time_from=11&time_to=17&station=857



url= f'https://www.umweltbundesamt.de/api/air_data/v2/measures/json?date_from=2018-05-05&date_to=2018-05-10&time_from=1&time_to=24&station=1778&component=1&scope=1'
### param =dict(...)
data = requests.get(url=url).json()
#formatieren: json in string
print(json.dumps(data, indent =4))

print(data['request'])