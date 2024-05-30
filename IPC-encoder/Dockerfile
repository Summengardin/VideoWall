# sudo docker run -it --rm --network=host --device=/dev/dri 

FROM ubuntu:22.04

ARG DEBIAN_FRONTEND="noninteractive"

RUN cd 

# Make virtual environment
RUN apt-get update && apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:deadsnakes && \
    apt-get update
RUN apt-get install -y python3.11 python3.11-distutils python3.11-dev


# Update and install system packages
RUN apt-get update && apt-get install -y \
    libgstreamer1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    libgstreamer-plugins-good1.0-dev \
    libgstreamer-plugins-bad1.0-dev \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav \
    gstreamer1.0-tools \
    #gstreamer1.0-x \
    gstreamer1.0-alsa \
    gstreamer1.0-gl \
    #gstreamer1.0-gtk3 \
    #gstreamer1.0-pulseaudio \
    libgstrtspserver-1.0-dev \
    libcairo2-dev \
    libxt-dev \
    libgirepository1.0-dev \
    gir1.2-gst-rtsp-server-1.0
# RUN rm -rf /var/lib/apt/lists/*


# RUN apt-get update && apt-get install -y kmod wget
RUN apt-get install -y net-tools


RUN apt-get install -y curl && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11 && \
    pip3 install meson && \
    pip3 install ninja

# Install ARAVIS
RUN apt-get install -y libxml2-dev libglib2.0-dev cmake libusb-1.0-0-dev gobject-introspection \
libgtk-3-dev gtk-doc-tools  xsltproc libgstreamer1.0-dev \
libgstreamer-plugins-base1.0-dev libgstreamer-plugins-good1.0-dev \
libgirepository1.0-dev cmake

RUN apt-get install git -y && \
    git clone https://github.com/AravisProject/aravis.git && \
    cd aravis && \
    meson setup build -Dviewer=disabled -Dintrospection=disabled && \
    ninja -C build && \
    ninja -C build install

ENV GST_PLUGIN_PATH="$GST_PLUGIN_PATH:/usr/local/lib/x86_64-linux-gnu/gstreamer-1.0"
ENV LD_LIBRARY_PATH="/usr/local/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH"

RUN apt-get -y install iputils-ping intel-media-va-driver gstreamer1.0-vaapi

WORKDIR /app

COPY rtsp_aravis.py /app

# RUN    ninja build && \
#     ninja build install

# RUN cp src/aravis.rules /etc/udev/rules.d



