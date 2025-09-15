# Start from a base image with necessary tools.
# For example, use a a Debian or Ubuntu image.
FROM mcr.microsoft.com/devcontainers/base:bullseye

# Install necessary tools. This is where you would add
# any language runtimes or other dependencies for your project.
# For example, you might need Node.js, Python, or PHP.
# This example installs Node.js
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends mariadb-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
