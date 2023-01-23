import mysql.connector

# Koneksi ke database
cnx = mysql.connector.connect(
    host="hostname",
    user="username",
    password="password",
    database="database_name"
)

cursor = cnx.cursor()

# Membuat tabel
create_table = """
CREATE TABLE laptop (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    no_hp VARCHAR(255)
)
"""
cursor.execute(create_table)

# Menambahkan data
add_user = "INSERT INTO laptop (name, no_hp) VALUES (%s, %s)"
user_data = ("dila", "085785005761")
cursor.execute(add_user, user_data)
cnx.commit()

# Mengambil data
query = "SELECT * FROM laptop"
cursor.execute(query)

for (id, name, email) in cursor:
    print("ID: {}, Name: {}, no_hp: {}".format(id, name, no_hp))

# Menutup koneksi
cursor.close()
cnx.close()