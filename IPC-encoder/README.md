## Run the docker container
To build the docker image, be inside the folder of the Dockerfile and run  
```
docker build . -t rtsparavis
```  
This will create a new docker image called `rtsparavis`

To run a container with this image  
```
sudo docker run -it --rm --network=host --device=/dev/dri rtsparavis
```


## Set the network settings
[HowTo](https://www.freecodecamp.org/news/setting-a-static-ip-in-ubuntu-linux-ip-address-tutorial/) \
[Example](https://www.reddit.com/r/Ubuntu/comments/njpjsw/ubuntu_server_20042_dhcp_to_static_ip_netplan/
)

Check `/etc/netplan` of the device. In my case it included `00-installer-config.yaml` which contained setting for the network adapters. Check possible other .yaml files. If non are present, create a new one. Use the included `00-installer-config.yaml` for inspiration.

To edit the file, run
```
sudo nano 00-installer-config.yaml
```

Then, run the followin BEFORE rebooting 
```
sudo netplan apply
``` 
# Troubleshooting
## tiscamera
Installing the `tiscamera`-library required several unmentioned libraries. tiscamera/scripts/dependency-manager needed sudo to run for example.  
From **apt-get**:
- sudo
- libzip-dev  

From **pip**:
- sphinx

tiscamera is built without tools. These are all CMakeOptions differing from the default:  
    -DTCAM_BUILD_ARAVIS=OFF \
    -DTCAM_BUILD_TOOLS=OFF \
    -DTCAM_BUILD_LIBUSB=OFF \
    -DTCAM_BUILD_V4L2=OFF 