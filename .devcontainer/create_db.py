import mysql.connector

conn = mysql.connector.connect(
    user="root",
    unix_socket="/run/mysqld/mysqld.sock"
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
print("✅ Database 'mydatabase' created or already exists.")

cursor.close()
conn.close()
