import mysql.connector
import time

DB_NAME = "mydatabase"
SOCKET_PATH = "/run/mysqld/mysqld.sock"
TIMEOUT = 60  # seconds
INTERVAL = 5  # seconds between retries

print(f"⏳ Waiting for MariaDB to be ready at {SOCKET_PATH} (timeout {TIMEOUT}s)...")

start_time = time.time()

while True:
    try:
        conn = mysql.connector.connect(
            user="root",
            unix_socket=SOCKET_PATH
        )
        break
    except mysql.connector.Error:
        elapsed = time.time() - start_time
        if elapsed > TIMEOUT:
            print(f"❌ Timeout: MariaDB not ready after {TIMEOUT} seconds.")
            exit(1)
        print(f"Waiting for database... retrying in {INTERVAL} seconds")
        time.sleep(INTERVAL)

cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
print(f"✅ Database '{DB_NAME}' created or already exists.")

cursor.close()
conn.close()
