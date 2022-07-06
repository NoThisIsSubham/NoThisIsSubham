import cv2
from PIL import ImageGrab
from win32api import GetSystemMetrics as GSM
from numpy import array
from datetime import datetime

from VA_voice import say

def webrecorder():

    file_format = cv2.VideoWriter_fourcc("m", "p", "4", "v")
    video_writer = cv2.VideoWriter(datetime.now().strftime("Recorded on %a, %I %M %p, %B %Y") + ".mp4", file_format, 15, (GSM(0), GSM(1)))
    say("Recorder activated...")
    smv = 0

    while smv<100:
        Screen = ImageGrab.grab(bbox=(0, 0, GSM(0), GSM(1)))
        np_array = array(Screen)
        imp_final = cv2.cvtColor(np_array, cv2.COLOR_BGR2RGB)
        video_writer.write(imp_final)
        smv+=1

    say("Recording completed successfully!")

        