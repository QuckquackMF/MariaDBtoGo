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

# Copy scripts
COPY create_db.py /workspace/create_db.py
COPY entrypoint.sh /workspace/entrypoint.sh
COPY requirements.txt /workspace/requirements.txt

WORKDIR /workspace

# Install Python requirements
RUN pip3 install -r requirements.txt

# Make entrypoint executable
RUN chmod +x /workspace/entrypoint.sh

ENTRYPOINT ["/workspace/entrypoint.sh"]
