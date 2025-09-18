# Base image
FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    mariadb-server \
    python3 \
    python3-pip \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Create vscode user
RUN groupadd --gid 1000 vscode \
    && useradd -m -s /bin/bash --uid 1000 --gid 1000 vscode \
    && echo "vscode ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/vscode \
    && chmod 0440 /etc/sudoers.d/vscode

# Prepare MariaDB socket
RUN mkdir -p /run/mysqld && chown -R mysql:mysql /run/mysqld

# Copy Python script and requirements
COPY create_db.py /workspace/create_db.py
COPY requirements.txt /workspace/requirements.txt

WORKDIR /workspace

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Copy entrypoint script
COPY devcontainer-entrypoint.sh /usr/local/bin/devcontainer-entrypoint.sh
RUN chmod +x /usr/local/bin/devcontainer-entrypoint.sh

# Entrypoint
ENTRYPOINT ["/usr/local/bin/devcontainer-entrypoint.sh"]
