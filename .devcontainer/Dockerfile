# Base image
FROM ubuntu:22.04

# Install necessary packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        mariadb-server \
        python3 \
        python3-pip \
        git \
        sudo \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Copy requirements if exists
COPY requirements.txt /workspace/requirements.txt

# Install Python dependencies
RUN pip3 install -r /workspace/requirements.txt || true
