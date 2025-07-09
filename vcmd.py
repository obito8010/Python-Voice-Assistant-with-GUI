import speech_recognition as sr
import os

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio).lower()
            print(f"You said: {text}") 

            if text == "stop":
                print("Stopping the program...")
                break 

            elif text == "open youtube":
                print("Opening YouTube...")
                os.startfile('1.bat')
                
            elif text == "open google":
                print("Opening Google...")
                os.startfile('2.bat')
            
        except Exception as e:
            print(f"Error recognizing speech: {e}")
