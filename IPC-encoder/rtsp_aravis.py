#!/usr/bin/env python3

import gi
import multiprocessing
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GLib, GstRtspServer

class VideoServerRTSP:

    def __init__(self, port='8554'):
        self.port = port

    def start(self):
        self.loop = self._generate_gst_rtsp_server(self.port)
        self.loop.run()

    def _generate_gst_rtsp_server(self, port):
        Gst.init(None)

        if port == '8554':
            pipeline = (
                "aravissrc ! video/x-bayer,width=1280,height=720,framerate=30/1,format=rggb ! "
                "queue max-size-time=0 max-size-bytes=0 max-size-buffers=1 ! tcamconvert ! "
                "videoconvert ! video/x-raw,format=NV12 ! vaapih264enc max-qp=30 bitrate=5000 cpb-length=1 quality-level=1 ! "
                "queue max-size-time=0 max-size-bytes=0 max-size-buffers=1 ! rtph264pay name=pay0 pt=96"
            )
        else:
            pipeline = (
            "videotestsrc ! video/x-raw,format=RGB,width=1280,height=720,framerate=30/1 ! "
            "videoconvert ! video/x-raw,format=NV12 ! vaapih264enc ! rtph264pay name=pay0 pt=96"
        )

        server = GstRtspServer.RTSPServer.new()
        server.set_service(str(port))
        mounts = server.get_mount_points()

        factory = GstRtspServer.RTSPMediaFactory.new()
        factory.set_launch(pipeline)
        factory.set_latency(0)
        mounts.add_factory('/test', factory)

        server.attach(None)
        loop = GLib.MainLoop()

        print(f"Stream is running on: rtsp://10.0.0.5:{port}/test")
        return loop


def run_server(port):
    server = VideoServerRTSP(port)
    server.start()


if __name__ == '__main__':
    print("Running")

    process1 = multiprocessing.Process(target=run_server, args=('8554',))
    process2 = multiprocessing.Process(target=run_server, args=('8555',))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
