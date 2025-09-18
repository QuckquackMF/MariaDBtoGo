#!/bin/bash
set -e

# Start MariaDB in the background
sudo service mariadb start

# Wait a few seconds to make sure MariaDB is ready
sleep 5

# Run Python script to create database
python3 /workspace/create_db.py

# Drop into bash for interactive use
exec /bin/bash
