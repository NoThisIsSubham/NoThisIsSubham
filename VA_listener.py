import speech_recognition as sr

def listener():
    with sr.Microphone() as device:
        try:
            record = sr.Recognizer().listen(device)
            string_data = sr.Recognizer.recognize_google(record)

            return string_data

        except:
            return "None"
        

