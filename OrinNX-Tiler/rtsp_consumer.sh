#!/bin/bash

uri_default="rtsp://10.0.0.5:8554/test"

uri="${1:-$uri_default}"

gst-launch-1.0 -v rtspsrc location=${uri} latency=0 ! application/x-rtp, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! autovideosink sync=false

# gst-launch-1.0 -v rtspsrc location=${uri} latency=0 ! application/x-rtp, payload=96 ! rtph264depay ! nvv4l2decoder enable-max-performance=1 ! nv3dsink sync=false

