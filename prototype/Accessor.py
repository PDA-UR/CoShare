#gst-launch-1.0 -v udpsrc port=5000 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96" ! rtph264depay ! decodebin ! videoconvert ! autovideosink
import subprocess

class Accessor:
    def __init__(self):
        print("Accessor alive")

    def access_stream(self):
        print("Accessor benachrichten!") #TODO
        subprocess.Popen("gst-launch-1.0 -v udpsrc port=5000 "
                         "caps = \"application/x-rtp, media=(string)video, "
                         "clock-rate=(int)90000, encoding-name=(string)H264, "
                         "payload=(int)96\" ! rtph264depay ! decodebin ! videoconvert ! autovideosink", shell=True)
        #io.connect