# Use a minimal base image of Debian
FROM debian:bullseye-slim

# Set the maintainer of the image
LABEL maintainer="dfproffesional@gmail.com"

# Update package list and install necessary dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    debhelper \
    fakeroot \
    dh-python \
    python3-all \
    python3-pip  \
    python3-stdeb \
    python3-setuptools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy application files to the container
COPY . /compile

# Set the working directory
WORKDIR /compile

# Build the Debian package
RUN pip3 install .

# Set the default command
CMD ["bash"]
