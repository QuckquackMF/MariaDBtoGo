import mysql.connector
import time

print("⏳ Waiting for MariaDB to be ready...")

while True:
    try:
        conn = mysql.connector.connect(
            host="mariadb",  # Docker service name
            user="root",
            port=3306
        )
        break
    except mysql.connector.Error:
        print("Waiting for database... retrying in 5 seconds")
        time.sleep(5)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
print("✅ Database 'mydatabase' created or already exists.")

cursor.close()
conn.close()
