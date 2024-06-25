## Build docker
```


```

## Run Docker
```
docker run --gpus all -it --rm --net=host --privileged -v /tmp/.X11-unix:/tmp/.X11-unix -v/home/seaonics/Dev/VideoWall:/dev/VideoWall -e DISPLAY=$DISPLAY dsimage
```


## Baseline-pipeline
```
gst-launch-1.0 tcambin  device-caps=video/x-bayer,width=1920,height=1080,framerate=54/1,format=rggb ! queue leaky=1 max-size-time=0 max-size-bytes=0 max-size-buffers=1 ! videoconvert  n-threads=4 ! fpsdisplaysink text-overlay=no video-sink=xvimagesink sync=false -v
```


