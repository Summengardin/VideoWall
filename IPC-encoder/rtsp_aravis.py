#!/bin/usr/python3

import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GLib, GstRtspServer

class VideoServerRTSP:

    def __init__(self):

        self.loop = self._generate_gst_rtsp_server()
        self.loop.run()

    def _generate_gst_rtsp_server(self):

        Gst.init(None)

        pipeline = (
            "aravissrc ! video/x-raw,format=RGB,width=1280,height=720,framerate=30/1 ! "
            "videoconvert ! video/x-raw,format=NV12 ! vaapih264enc ! rtph264pay name=pay0 pt=96"
        )

        #pipeline = "v4l2src device=/dev/video0 ! videoconvert ! videoscale ! video/x-raw,width=[1,640],height=[1,480] ! x264enc tune=zerolatency bitrate=250 ! rtph264pay pt=96 name=pay0"
        # gst-launch-1.0 aravissrc ! video/x-raw,format=RGB,width=1280,height=720,framerate=30/1 ! videoconvert ! video/x-raw,format=I420 ! vaapih264enc ! fakesink
        # gst-launch-1.0 videotestsrc ! video/x-raw,format=I420 ! vaapih264enc ! fakesink

        server = GstRtspServer.RTSPServer.new()
        server.set_service(str('5050'))
        mounts = server.get_mount_points()

        factory = GstRtspServer.RTSPMediaFactory.new()
        factory.set_launch(pipeline)
        #factory.set_shared(True)
        mounts.add_factory('/test', factory)

        server.attach()
        loop = GLib.MainLoop()

        print("Ret loop")
        return loop


if __name__ == '__main__':
    print("Running")
    server = VideoServerRTSP()