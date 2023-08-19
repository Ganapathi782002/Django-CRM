import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'ganapathi@782002'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_and_co")

print("All Done!")