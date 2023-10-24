# Connection to PythonAnywhere MySQL. Uses SSH tunnel.
# Reference for details: https://help.pythonanywhere.com/pages/AccessingMySQLFromOutsidePythonAnywhere/
import MySQLdb
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='marku123', ssh_password='20&Burger&19',
    remote_bind_address=('marku123.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    connection = MySQLdb.connect(
        user='marku123',
        passwd='w6NTxY3Xi',
        host='127.0.0.1', port=tunnel.local_bind_port,
        db='marku123$default',
    )

    mycursor = connection.cursor()
    # Executing Query
    mycursor.execute("SELECT CURDATE();")
    m = mycursor.fetchone()
    print("Today's Date Is ", m[0])

    mycursor.execute("SELECT * FROM Persons;")
    symbolsFromDB = mycursor.fetchall()
    for x in symbolsFromDB:
        print(x[2])

connection.close()



# Connection to DailyRazor MySQL. May need to add requesting server to the server hostname file on dailyrazor.
import mysql.connector

mydb = mysql.connector.connect(host='gldz3.dailyrazor.com', user="ukramcom_1", passwd="%%bac0n2013")

mycursor = mydb.cursor()
mycursor.execute("SELECT CURDATE();")
m = mycursor.fetchone()
print("Today's Date Is ", m[0])

mycursor.execute("Select * From ukramcom_unhcr_legaltool.authentication")
symbolsFromDB = mycursor.fetchall()
for x in symbolsFromDB:
    print(x[2])

mydb.cursor()



# Connection to Localhost MySQL.
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user="ukram123", passwd="%%bac0n2013")

mycursor = mydb.cursor()
mycursor.execute("Select distinct stocksymbol From ukram123_stocks.tsxdata")

symbolsFromDB = mycursor.fetchall()

allStockSymbols = []
for x in symbolsFromDB:
    allStockSymbols.append(x[0])
    print(x[0])
    for y in allStockSymbols:
        print(y)

mydb.cursor()
