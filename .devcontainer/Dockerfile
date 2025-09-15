# Start from a base image that's good for development and has apt
FROM mcr.microsoft.com/devcontainers/base:bullseye

# Set environment variables for non-interactive installs
ENV DEBIAN_FRONTEND=noninteractive

# Install MariaDB server and client
RUN apt-get update && apt-get -y install mariadb-server mariadb-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Add a script to start MariaDB when the container launches
COPY startup.sh /usr/local/bin/

# Set the entrypoint to your startup script
ENTRYPOINT ["/usr/local/bin/startup.sh"]

# Expose the MariaDB port (optional but good practice)
EXPOSE 3306

# You would add your application's setup here, e.g.,
# RUN apt-get install -y nodejs npm
# COPY . /workspace
# WORKDIR /workspace
