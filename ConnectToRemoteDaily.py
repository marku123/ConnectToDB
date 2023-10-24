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