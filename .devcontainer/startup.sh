#!/bin/bash

# Start the MariaDB server in the background
/usr/bin/mysqld_safe --datadir=/var/lib/mysql &

# Wait for MariaDB to be ready
echo "Waiting for MariaDB to start..."
until mariadb -u root -e 'SELECT 1' 2>/dev/null; do
    sleep 1
done

echo "MariaDB is up. Running application command..."

# Keep the container running indefinitely
sleep infinity
