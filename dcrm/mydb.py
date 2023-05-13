import mysql.connector
import config

dataBase = mysql.connector.connect(
    host=config.HOST,
    user=config.USER,
    password=config.PASSWORD,
)

cursorObject = dataBase.cursor()

# create database
cursorObject.execute("CREATE DATABASE djangocrm")

print("All done!")
