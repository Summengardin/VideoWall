#!/bin/bash

# Example usage: bash display.sh camera-rgb 0

opt_default="aravis-bayer"
dbg_default="0"

opt="${1:-$opt_default}"

dbg="${2:-$dbg_default}"

# Simplest test-stream
if [ "$opt" == "test" ]; then
    GST_DEBUG=$dbg gst-launch-1.0 videotestsrc ! autovideosink
elif [ "$opt" == "camera" ]; then
    GST_DEBUG=$dbg gst-launch-1.0 pylonsrc capture-error=keep stream::MaxNumBuffer=1 ! "video/x-raw,width=1920,height=1200,framerate=60/1,format=YUY2" ! videoconvert ! autovideosink sync=false
elif [ "$opt" == "camera-simple" ]; then
    GST_DEBUG=$dbg gst-launch-1.0 pylonsrc ! videoconvert ! autovideosink
elif [ "$opt" == "camera-rgb" ]; then
    GST_DEBUG=$dbg gst-launch-1.0 pylonsrc ! "video/x-raw,width=1920,height=1080,framerate=60/1,format=RGB" ! videoconvert ! autovideosink
elif [ "$opt" == "camera-yuv422" ]; then
    GST_DEBUG=$dbg gst-launch-1.0 pylonsrc capture-error=keep stream::MaxNumBuffer=10 ! "video/x-raw,width=1920,height=1080,framerate=60/1,format=YUY2" ! videoconvert ! autovideosink sync=false
elif [ "$opt" == "camera-bayer" ]; then
    GST_DEBUG=$dbg gst-launch-1.0 pylonsrc capture-error=keep ! "video/x-bayer,width=1920,height=1200,framerate=60/1,format=rggb" ! bayer2rgb ! videoconvert ! autovideosink
elif [ "$opt" == "camera-tcam" ]; then
    GST_DEBUG=$dbg gst-launch-1.0 pylonsrc capture-error=keep ! "video/x-bayer,width=1920,height=1200,framerate=60/1,format=rggb" ! bayer2rgb ! videoconvert ! autovideosink
elif [ "$opt" == "camera-ttest" ]; then
    GST_DEBUG=$dbg gst-launch-1.0 videotestsrc ! "video/x-bayer,framerate=60/1,format=rggb" ! tcamdutils ! video/x-raw,format=BGRx ! videoconvert ! autovideosink
elif [ "$opt" == "tcamsrc" ]; then
    GST_DEBUG=$dbg gst-launch-1.0 tcamsrc ! video/x-raw,format=BGRx ! videoconvert ! autovideosink
elif [ "$opt" == "tcambin" ]; then
    GST_DEBUG=$dbg gst-launch-1.0 tcambin ! video/x-raw,format=BGRx ! videoconvert ! autovideosink
elif [ "$opt" == "tcambin-bayer" ]; then
    GST_DEBUG=$dbg gst-launch-1.0 tcambin device-caps="video/x-bayer,format=rggb" ! video/x-raw,format=BGRx ! videoconvert ! autovideosink
elif [ "$opt" == "aravis" ]; then
    GST_DEBUG=$dbg gst-launch-1.0 aravissrc ! videoconvert ! autovideosink
elif [ "$opt" == "aravis-bayer" ]; then
    GST_DEBUG=$dbg gst-launch-1.0 aravissrc ! video/x-bayer,width=1920,height=1200,framerate=60/1,format=rggb ! tcamconvert ! videoconvert ! autovideosink
elif [ "$opt" == "traceb" ]; then
    GST_DEBUG="GST_TRACER:7" GST_TRACERS="latency(flags=element)" gst-launch-1.0 aravissrc ! video/x-bayer,width=1920,height=1200,framerate=999/1,format=rggb  ! bayer2rgb ! videoconvert ! autovideosink > traces.log 2>&1
elif [ "$opt" == "tracet" ]; then
    GST_DEBUG="GST_TRACER:7" GST_TRACERS="latency(flags=element)" gst-launch-1.0 aravissrc ! video/x-bayer,width=1920,height=1200,framerate=999/1,format=rggb ! tcamconvert ! videoconvert ! autovideosink > traces.log 2>&1
elif [ "$opt" == "tracec" ]; then
    GST_DEBUG="GST_TRACER:7" GST_TRACERS="latency(flags=element)" gst-launch-1.0 pylonsrc capture-error=keep stream::MaxNumBuffer=1 ! "video/x-raw,width=1920,height=1200,framerate=60/1,format=YUY2" ! videoconvert ! autovideosink sync=false > traces.log 2>&1
else
    echo "Unknown option: $opt"
fi
