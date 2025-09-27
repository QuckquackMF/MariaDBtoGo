import mysql.connector
import time

print("Waiting a few seconds for MariaDB to be ready...")
time.sleep(3)

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="vscode",
        password="",
        database="mydatabase"
    )
    cursor = conn.cursor()
    conn.commit()
    print("Database 'mydatabase' is ready and table 'test_table' created.")
except mysql.connector.Error as err:
    print(f"Error connecting to MariaDB: {err}")
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
