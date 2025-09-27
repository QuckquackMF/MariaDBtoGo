FROM ubuntu:22.04

# Install everything: python, pip, git, MariaDB
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        python3 python3-pip python3-dev git mariadb-server mariadb-client sudo && \
    rm -rf /var/lib/apt/lists/*

# Set workspace
WORKDIR /workspace

# Install Python requirements if they exist
COPY requirements.txt /workspace/ || true
RUN pip3 install -r /workspace/requirements.txt || true

# Prepare MariaDB
RUN mkdir -p /run/mysqld && chown -R mysql:mysql /run/mysqld

# Configure git globally to avoid "dubious ownership"
RUN git config --global --add safe.directory /workspace && \
    git config --global user.name "Codespaces User" && \
    git config --global user.email "codespaces@example.com"

# Initialize git repo and main branch automatically
RUN git init /workspace && git checkout -b main
