**[ Work in progress ]**


## TheImagingSource
Use libaries from the-imaging-source, called tiscamera. See their [GitHub](https://github.com/TheImagingSource/tiscamera).  
Installation can be done using `install_tiscamera.sh` found in the `scripts`-directory. This script install with default [CMakeOptions](https://github.com/TheImagingSource/tiscamera/blob/master/CMakeOptions.cmake).

The IPC docker image comes with the tiscamera-library installed. This is built without any tools.

`tiscamera` is by default built with several tools.
They are run from the command line.

### Tools
**tcam-capture** is a GUI for showing the camera stream and changing camera setting. This can also control zoom and focus

**tcam-gigetool** is a CLI for setting gige-settings of the camera. See [docs](https://www.theimagingsource.com/en-us/documentation/tiscamera/tcam-gigetool.html) for usage.


# Troubleshooting


