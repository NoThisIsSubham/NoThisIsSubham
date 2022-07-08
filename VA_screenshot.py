import pyautogui
from datetime import datetime
from VA_voice import say

def takeShot():
    captured_frame = pyautogui.screenshot()
    captured_frame.save(r"C:\Users\NoThisIsSubham\Pictures\Screenshots\Screenshot1" + datetime.now().strftime("Screenshot taken on %a, %I %M %p, %B %Y")+ ".png")
    say("screen was successful.")


