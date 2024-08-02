# Use a minimal base image of Debian
FROM debian:bullseye-slim

# Set the maintainer of the image
LABEL maintainer="dfproffesional@gmail.com"

# Update package list and install necessary dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    debhelper \
    ruby-full  \
    fakeroot    \
    dh-python    \
    python3-all   \
    python3-pip    \
    python3-dev     \
    python3-stdeb    \
    python3-setuptools  \
    && apt-get clean     \
    && rm -rf /var/lib/apt/lists/*

# Install fpm
RUN gem install fpm

# Set Compile folder
RUN mkdir /compile
WORKDIR /compile
COPY ./requirements.txt /compile/requirements.txt

# Install Python dependences
RUN pip3 install -r requirements.txt

# Set the default command
CMD ["bash"]
