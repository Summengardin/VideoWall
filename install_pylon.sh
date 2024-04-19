#!/bin/bash

# Check architecture
ARCH=$(dpkg --print-architecture)

if [[ $ARCH == "amd64" ]]; then
    URL="https://www2.baslerweb.com/media/downloads/software/pylon_software/pylon-7.4.0.14900_linux_x86_64_debs.tar.gz"
elif [[ $ARCH == "arm64" ]]; then
    URL="https://www2.baslerweb.com/media/downloads/software/pylon_software/pylon-7.4.0.14900_linux_aarch64_debs.tar.gz"
else
    echo "Unsupported architecture: $ARCH"
    exit 1
fi

# Install pylon SDK
if [ $(dpkg-query -W -f='${Status}' pylon | grep -c 'ok installed') -eq 0 ]; then
    echo Installing Pylon SDK
    mkdir ./pylon_setup && cd pylon_setup && \
    
    wget $URL && \
    tar -xzf pylon_*_debs.tar.gz
    
    sudo apt install ./pylon_*.deb -y
 
    if [ $(dpkg-query -W -f='${Status}' pylon | grep -c 'ok installed') -eq 0 ]; then
        echo Failed to install Pylon
    else
        echo Pylon installed
        cd .. && sudo rm -r ./pylon_setup
    fi
else
    echo Pylon is already installed
fi
