# sudo docker run -it --rm --network=host --device=/dev/dri aravis

FROM ubuntu:22.04

ARG DEBIAN_FRONTEND="noninteractive"

# Label for base image and ARG setup
LABEL stage="base-image" description="Base image setup with Ubuntu 22.04 and noninteractive ARG"

# Step 1: Install system dependencies and Python
RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common gpg-agent curl && \
    add-apt-repository -y ppa:deadsnakes \
    && apt-get update \
    && apt-get install -y \
    python3.11 \
    python3.11-distutils \
    python3.11-dev \
    && curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11 \
    && pip3 install meson ninja 



LABEL stage="system-dependencies" description="Install system dependencies and Python"
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    net-tools \
    iputils-ping \
    git \
    intel-media-va-driver \
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
    gstreamer1.0-alsa \
    gstreamer1.0-gl \
    gstreamer1.0-vaapi \
    libgstrtspserver-1.0-dev \
    libcairo2-dev \
    libxt-dev \
    libgirepository1.0-dev \
    gir1.2-gst-rtsp-server-1.0 \
    libxml2-dev \
    libglib2.0-dev \
    cmake \
    libusb-1.0-0-dev \
    gobject-introspection \
    libgtk-3-dev \
    gtk-doc-tools \
    xsltproc \
    && rm -rf /var/lib/apt/lists/*


# Step 2: Install ARAVIS
LABEL stage="install-aravis" description="Clone and install ARAVIS library"
RUN git clone https://github.com/AravisProject/aravis.git && \
    cd aravis && \
    meson setup build -Dviewer=disabled -Dintrospection=disabled && \
    ninja -C build && \
    ninja -C build install && \
    cd .. && rm -rf aravis

# Step 3: Install TISCAMERA
LABEL stage="install-tiscamera" description="Clone and install TISCAMERA library"
WORKDIR /tisinstall
# tiscamera trenger sudo... Se: tiscamera/scripts/dependency-manager

RUN apt-get update && apt-get install sudo libzip-dev -y && pip3 install sphinx
RUN git clone https://github.com/TheImagingSource/tiscamera.git && \
    cd tiscamera && \
    git checkout v-tiscamera-1.1.0 && ./scripts/dependency-manager install && \
    mkdir build && cd build && cmake .. \
    -DTCAM_BUILD_ARAVIS=OFF \
    -DTCAM_BUILD_TOOLS=OFF \
    -DTCAM_BUILD_LIBUSB=OFF \
    -DTCAM_BUILD_V4L2=OFF && \ 
    make && make install && \
    cd ../.. && rm -rf tiscamera

# Step 4: Install TCAMDUTILS
LABEL stage="install-tcamdutils" description="Download and install TCAMDUTILS package"
WORKDIR /tisinstall/tcamdutils
RUN wget https://s1-dl.theimagingsource.com/api/2.5/packages/software/gstreamer/tiscameradutilsamd64/f286591a-43c8-52ae-a41a-9b8b6e928c52/tiscamera-dutils_1.0.0_amd64.deb && \
    apt-get install -y ./tiscamera-dutils_1.0.0_amd64.deb && \
    rm ./tiscamera-dutils_1.0.0_amd64.deb

# Step 5: Set environment variables
LABEL stage="set-environment-variables" description="Set environment variables for GStreamer and library paths"
ENV GST_PLUGIN_PATH="/usr/local/lib/x86_64-linux-gnu/gstreamer-1.0:$GST_PLUGIN_PATH"
ENV LD_LIBRARY_PATH="/usr/local/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH"

# Step 6: Copy application code
LABEL stage="copy-application-code" description="Copy application code to the container"
WORKDIR /app
COPY rtsp_aravis.py /app

# Label for CMD instruction
# LABEL stage="cmd-instruction" description="Set CMD to run the application"
# CMD ["python3.11", "rtsp_aravis.py"]
