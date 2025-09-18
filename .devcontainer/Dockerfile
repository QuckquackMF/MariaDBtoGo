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

# Copy Python script
COPY create_db.py /workspace/.devcontainer/create_db.py

WORKDIR /workspace

# Install Python requirements
COPY requirements.txt /workspace/requirements.txt
RUN pip3 install -r requirements.txt
