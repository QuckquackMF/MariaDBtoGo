#!/bin/bash
set -e

# Start MariaDB
sudo service mariadb start

# Wait until MariaDB is ready
echo "⏳ Waiting for MariaDB to be ready..."
for i in {1..30}; do
    if sudo mariadb -e "SELECT 1;" &> /dev/null; then
        break
    fi
    echo "Waiting for database... retrying in 2 seconds"
    sleep 2
done

# Run Python script to create database
python3 /workspace/create_db.py

# Keep the container running
exec "$@"
