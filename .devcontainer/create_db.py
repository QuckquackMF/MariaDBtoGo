import subprocess

# Start MariaDB safely
subprocess.run("sudo service mariadb start", shell=True, check=True)

# Create 'vscode' user with all privileges, no password
subprocess.run("""
sudo mariadb -e "CREATE DATABASE IF NOT EXISTS mydatabase;
CREATE USER IF NOT EXISTS 'vscode'@'%' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON mydatabase.* TO 'vscode'@'%';
FLUSH PRIVILEGES;"
""", shell=True, check=True)
