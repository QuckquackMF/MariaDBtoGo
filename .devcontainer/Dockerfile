# Start from a Node.js image that also includes Python
FROM node:18-bullseye-slim

# Install a specific version of npm
# Note: npm version 11.6 is very old and not officially supported. 
# This command is for illustration purposes.
RUN npm install -g npm@11.6.0

# Install MariaDB server and client
# The Node.js image is based on Debian, so we can use apt-get
RUN apt-get update && apt-get -y install mariadb-server mariadb-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Run MariaDB on container start
CMD ["sudo", "service", "mariadb", "start"]
