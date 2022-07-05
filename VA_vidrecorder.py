import cv2
from PIL import ImageGrab
from win32api import GetSystemMetrics as GSM
from numpy import array


def webrecorder():
    file_format = cv2.VideoWriter_fourcc("m", "p", "4", "v")
    video_writer = cv2.VideoWriter("vid.mp4", file_format, 18, (GSM(0), GSM(1)))
    while True:
        Screen = ImageGrab.grab(bbox=(0, 0, GSM(0), GSM(1)))
        np_array = array(Screen)
        imp_final = cv2.cvtColor(np_array, cv2.COLOR_BGR2RGB)
        video_writer.write(imp_final)
        

