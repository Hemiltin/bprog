import mysql.connector

mysql = mysql.connector.connect(
    host = "192.168.120.99",
    user = "root",
    password = "",
    database = "",
)
if mysql.is_connected():
    print("Anda Berhasil Connect Ke Database")