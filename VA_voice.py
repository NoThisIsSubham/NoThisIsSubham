import pyttsx3

def say(msg):
    speaker = pyttsx3.init()
    speaker.setProperty("rate", 180)
    speaker.say(msg)
    speaker.runAndWait()


