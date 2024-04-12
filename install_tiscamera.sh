#!/bin/bash
# sudo apt install -y git cmake

mkdir tis-install
cd tis-install

# mkdir tiscamera
# cd tiscamera

# wget https://s1-dl.theimagingsource.com/api/2.5/packages/software/sdk/tiscamera/f47b5b18-a6c1-552d-b952-dd912ad94952/tiscamera_1.1.0.4139_amd64_ubuntu_1804.deb
# sudo apt install -y ./tiscamera*.deb


# tiscamera
git clone https://github.com/TheImagingSource/tiscamera.git
cd tiscamera
git checkout v-tiscamera-1.1.0

sudo ./scripts/dependency-manager install
mkdir build
cd build

cmake ..

make
sudo make install



# tcam-properties
# echo "Installing tcam-properties"
# cd ../..
# git clone https://github.com/TheImagingSource/tiscamera-tcamprop.git

# cd tiscamera-tcamprop
# mkdir build
# cd build
# cmake ..
# make
# make package
# sudo apt install ./tiscamera-tcamprop*.deb



# Install tcamdutils
echo "Installing tcamdutils"
cd ..

mkdir tcamdutils
cd tcamdutils

wget https://s1-dl.theimagingsource.com/api/2.5/packages/software/gstreamer/tiscameradutilsamd64/b0132f21-4cff-525a-87ef-89df286de160/tcamdutils_1.0.0.560_amd64.deb
sudo apt install -y ./tcamdutils*.deb