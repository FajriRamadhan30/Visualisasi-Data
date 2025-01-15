import mysql.connector
import pandas as pd

# Koneksi ke database MySQL
db_connection = mysql.connector.connect(
    host="localhost",          # Sesuaikan dengan host database Anda
    user="root",      # Ganti dengan username MySQL Anda
    password="",  # Ganti dengan password MySQL Anda
    database="sakila"          # Nama database
)

# Buat cursor untuk menjalankan query
cursor = db_connection.cursor()

# Query untuk mengambil data dari tabel (misalnya, tabel 'actor')
query = "SELECT * FROM address"
cursor.execute(query)

# Ambil hasil query dan tampilkan dalam bentuk DataFrame
result = cursor.fetchall()
columns = [column[0] for column in cursor.description]

# Tampilkan DataFrame
print(data_frame)

# Tutup koneksi
cursor.close()
db_connection.close()
