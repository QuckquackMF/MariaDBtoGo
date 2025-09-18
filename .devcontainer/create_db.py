import subprocess

# Start MariaDB
subprocess.run("sudo service mariadb start", shell=True, check=True)

# Create 'mydatabase' and 'vscode' user with full privileges
subprocess.run("""
sudo mariadb -e "CREATE DATABASE IF NOT EXISTS mydatabase;
CREATE USER IF NOT EXISTS 'vscode'@'%' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON mydatabase.* TO 'vscode'@'%';
FLUSH PRIVILEGES;"
""", shell=True, check=True)

print("✅ MariaDB is running, database 'mydatabase' created, user 'vscode' ready to connect!")
