FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    sudo \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create vscode user
RUN groupadd --gid 1000 vscode \
    && useradd -m -s /bin/bash --uid 1000 --gid 1000 vscode \
    && echo "vscode ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/vscode \
    && chmod 0440 /etc/sudoers.d/vscode

WORKDIR /workspace

# Copy Python requirements and install
COPY requirements.txt /workspace/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy your Python scripts
COPY create_db.py /workspace/.devcontainer/create_db.py
