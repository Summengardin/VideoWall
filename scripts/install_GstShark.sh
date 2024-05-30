#!/bin/bash

sudo apt install graphviz libgraphviz-dev

git clone https://github.com/RidgeRun/gst-shark/
cd gst-shark

meson setup build --prefix /usr/
cd build
ninja
sudo ninja install