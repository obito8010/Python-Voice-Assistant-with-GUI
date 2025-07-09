import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import pyttsx3
import os

# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init()

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to handle the speech recognition
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...", foreground="blue")
        speak("Listening...")
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            result_label.config(text=f"You said: {text}")  # Update label with recognized text
            speak(f"You said: {text}")

            if text.lower() == "stop":
                speak("Stopping the program...")
                close_application()  # Cleanly close the app
            elif text.lower() == "open youtube":
                os.startfile("1.bat")
                speak("Opening YouTube")
            elif text.lower() == "open google":
                os.startfile("2.bat")
                speak("Opening Google")
            else:
                result_label.config(text="Command not recognized.")
                speak("Sorry, I didn't understand the command.")
        except Exception as e:
            print("Error:", e)
            speak("Sorry, I could not understand your speech.")
            result_label.config(text="Error: Unable to recognize speech.")

# Function to handle proper cleanup on exit
def close_application():
    speak("Goodbye!")
    engine.stop()  # Stop the text-to-speech engine
    root.destroy()  # Destroy the Tkinter window and exit

# Create the main Tkinter window
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#2b2b2b")  # Set background color

# Create a style for ttk widgets
style = ttk.Style()
style.theme_use("clam")

# Style configurations
style.configure(
    "TLabel",
    font=("Arial", 14),
    background="#2b2b2b",
    foreground="#ffffff",
)
style.configure(
    "TButton",
    font=("Arial", 12, "bold"),
    padding=10,
    background="#4caf50",
    foreground="white",
)
style.map(
    "TButton",
    background=[("active", "#45a049")],
    foreground=[("active", "white")],
)

# Add a header label
header_label = ttk.Label(root, text="Voice Assistant", font=("Arial", 18, "bold"))
header_label.pack(pady=20)

# Add a label for status
status_label = ttk.Label(root, text="Press the button to start listening.")
status_label.pack(pady=10)

# Add a label for displaying recognized speech
result_label = ttk.Label(root, text="Say something...")
result_label.pack(pady=20)

# Add a button to start listening
listen_button = ttk.Button(root, text="Start Listening", command=listen)
listen_button.pack(pady=10)

# Add a close button
close_button = ttk.Button(root, text="Exit", command=close_application)
close_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
