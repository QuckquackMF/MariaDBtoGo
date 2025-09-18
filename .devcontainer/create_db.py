import mysql.connector
import time

print("⏳ Waiting for MariaDB to be ready...")
time.sleep(3)

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root"
    )
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase;")
    cursor.execute("CREATE USER IF NOT EXISTS 'vscode'@'%' IDENTIFIED BY '';")
    cursor.execute("GRANT ALL PRIVILEGES ON mydatabase.* TO 'vscode'@'%';")
    cursor.execute("FLUSH PRIVILEGES;")
    conn.commit()

    print("Database 'mydatabase' created and user 'vscode' granted privileges.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
