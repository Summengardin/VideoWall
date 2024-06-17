## Deepstream 

### Environment variables
'export USE_NEW_NVSTREAMMUX=yes'
'export DISPLAY=:0.0'


### Docker

Run using 
```
docker run -it --rm --net=host --runtime nvidia  -e DISPLAY=$DISPLAY -w /opt/nvidia/deepstream/deepstream-7.0 -v /tmp/.X11-unix/:/tmp/.X11-unix nvcr.io/nvidia/deepstream:7.0-triton-multiarch
```

### Local
Sample configs are located at `/opt/nvidia/deepstream/deepstream/samples/configs`



## Missing Dependencies
With a fresh flash, some dependencies were missing on the Jetson.

#### GST_RTSP_SERVER
`libgstrtspserver-1.0.so.0`: no such file or directory.  
Install using
```
sudo apt install libgstrtspserver-1.0-0
```


## Flashing

Use [this](https://wiki.seeedstudio.com/reComputer_Industrial_Getting_Started/) guide to flash the Jetson. This ensures all correct drivers for the industrial version.  
*Note: As of 30.05.2024, there is no official JetPack 6.0 option for the reComputer Industrial.*

### Problems Post-Flash using NVIDIA SDK Manager

After flashing using the NVIDIA SDKManager, some drivers might be missing for the reComputer Industrial J4011. 
In my case on of the network interfaces were not showing up in settings. Running `lshw -c network` shows one of them as UNCLAIMED:

```
-network UNCLAIMED       
       description: Ethernet controller
       product: Microchip Technology / SMSC
       vendor: Microchip Technology / SMSC
       physical id: 0
       bus info: pci@0001:01:00.0
       version: 11
       width: 64 bits
       clock: 33MHz
       capabilities: cap_list
       configuration: latency=0
       resources: memory:20a8000000-20a8001fff memory:20a8002000-20a80020ff memory:20a8002100-20a80021ff
```

To fix this, run the official installation guide from Seeds Studio instead, as described.
