import bs4
import requests
import pyodbc
import json
import mysql.connector as mysql
# mydb = mysql.connect( host='localhost', user='newuser',passwd= 'passwOrd', port=8888)
import sqlite3
for driver in pyodbc.drivers():
    print (driver)
db = pyodbc.connect('Driver={SQL Server};Server=LAPTOP-L06OLGV8;Database=Luftschadstoffbelastung_Daten;Uid=myUsername;Pwd=myPassword;')
source =  pyodbc.SQLDataSources(pyodbc.SQL_FETCH_FIRST)
while source:
    print(source)
    source = pyodbc.SQLDataSources(pyodbc.SQL_FETCH_NEXT)

credentials = None
with open('/var/run/secrets/user_credentials/mysql_credentials') as f:
    credentials = json.load(f)

# Ensure your credentials were setup
if credentials:
    # Connect to the DB
    connection = mysql.connect(
        user=credentials.get('username'),
        password=credentials.get('password'),
        database='employees',
        host='support-mysql.dev.anaconda.com'
    )
    cursor = connection.cursor()

    # Execute the query
    cursor.execute("SELECT first_name, last_name FROM employees LIMIT 20")

    # Loop through the results
    for first_name, last_name in cursor:
        print(f'First name: {first_name}, Last name: {last_name}')



def read(conn):

    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from Luftschadstoffbelastung")
    for row in cursor:
        print(f'row={row}')
        print()

# conn_str = (
#     r'DRIVER = {MySQL ODBC 8.0 Unicode Driver};'
#     r'SERVER=LAPTOP-L06OLGV8;'
#     r'DATABASE=Luftschadstoffbelastung_Daten;'
#     r'Trusted_Connection=yes;'
# )
#
# conn= pyodbc.connect(
#     conn_str
# )
# connection = pymysql.connect(host='localhost', user='root', passwd= 'passwOrd', db= 'Luftschadstoffbelastung')
# cursor = connection.cursor()
# sql = ('select  * from Luftschadstoffbelastung_Daten')
#
# read(conn)
#
# conn.close


# url = 'https://www.umweltbundesamt.de/daten/luft/luftdaten/stationen/eJzrXpScv9BwUXEykEhJXGVkYGSoa2Cma2i5qCRzkaHRorzUBYuKSxYsSUl0K0LIGgH5IfnIqpMTJyzKrWJblJvctDgnseS0g-eqea8a5Y4vzslLP-2gcs7F4ZPFbAANaivJ'
# sourcecode =requests.get(url)
# html=sourcecode.content
#
# soup = bs4.BeautifulSoup(html, "lxml")
# html = sourcecode.content
#
# tables = soup.findAll("table")
# tableMatrix = []
# for table in tables:
#     #Here you can do whatever you want with the data! You can findAll table row headers, etc...
#     list_of_rows = []
#     list_of_cells = []
#     for row in table.findAll('en')[1:]:
#         for cell in row.findAll('en'):
#             text = cell.text.replace('&nbsp;', '')
#             list_of_cells.append(text)
#         list_of_rows.append(list_of_cells)
#     tableMatrix.append((list_of_rows, list_of_cells))
# print(tableMatrix)