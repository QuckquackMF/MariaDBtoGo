# Use Ubuntu 22.04
FROM ubuntu:22.04

# Non-interactive installs
ENV DEBIAN_FRONTEND=noninteractive

# Install MariaDB, Python, Git, sudo
RUN apt-get update && apt-get install -y \
    mariadb-server \
    python3 \
    python3-pip \
    git \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Set root user for Codespaces
USER root

# Setup MariaDB directories
RUN mkdir -p /run/mysqld && chown -R mysql:mysql /run/mysqld

# Setup workspace
RUN mkdir -p /workspace && chown -R root:root /workspace
WORKDIR /workspace

# Copy requirements if exists
COPY requirements.txt /workspace/requirements.txt
RUN pip3 install -r /workspace/requirements.txt || true
