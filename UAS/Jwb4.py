import mysql.connector as conn

mysql = conn.connect(
    host = "localhost",
    port = 23306,
    user = "root",
    password ="p455w0rd",
    database =""
)
if mysql.is_connected():
    print("Halo adillah, kamu berhasil connect ke database")
    