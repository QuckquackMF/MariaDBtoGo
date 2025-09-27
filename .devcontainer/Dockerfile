# Use Ubuntu 22.04 base
FROM ubuntu:22.04

# Noninteractive install
ENV DEBIAN_FRONTEND=noninteractive

# Install essentials: MariaDB, Python, pip, sudo, git
RUN apt-get update && apt-get install -y \
    mariadb-server \
    python3 \
    python3-pip \
    sudo \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create vscode user (uid/gid 1000) and make sudo passwordless
RUN groupadd --gid 1000 vscode \
    && useradd -m -s /bin/bash --uid 1000 --gid 1000 vscode \
    && echo "vscode ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/vscode \
    && chmod 0440 /etc/sudoers.d/vscode

# Prepare MariaDB directories
RUN mkdir -p /run/mysqld && chown -R mysql:mysql /run/mysqld

# Workspace
RUN mkdir -p /workspace && chown -R vscode:vscode /workspace
WORKDIR /workspace

# Copy scripts
COPY create_db.py /workspace/.devcontainer/create_db.py
COPY requirements.txt /workspace/requirements.txt

# Install Python requirements
RUN pip3 install -r /workspace/requirements.txt
