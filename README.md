# 🗣️ Python Voice Assistant with GUI

This is a beginner-friendly **Voice Assistant** application built using Python. It features a simple graphical user interface (GUI) and allows users to interact using voice commands. The assistant can listen to your speech, recognize specific keywords, and respond using speech output or perform actions like opening websites.

---

## 📌 What This Project Teaches

- How to use `tkinter` to create a GUI in Python.
- How to integrate `speech_recognition` for voice input.
- How to use `pyttsx3` for text-to-speech (TTS) output.
- How to interact with external files (like `.bat` scripts).
- Basic command handling and automation using voice.

---

## 📦 Features

- 🎙️ Listens to your voice through a microphone.
- 🧠 Uses Google Speech API to recognize spoken words.
- 💬 Speaks back using the system's speech engine.
- 🖥️ Has a clean and responsive GUI using `tkinter` and `ttk`.
- 🧾 Recognizes and handles basic commands:
  - `"open youtube"`
  - `"open google"`
  - `"stop"`

---

## 🧠 How It Works

1. When you click **Start Listening**, the microphone starts recording.
2. Your voice is converted to text using the Google Speech API via the `speech_recognition` library.
3. The recognized text is matched against known commands.
4. If a command is matched, a corresponding action is performed:
   - For example, `open youtube` runs a `.bat` file that launches YouTube.
5. The assistant also responds by speaking using the `pyttsx3` text-to-speech engine.

---

## 🖥️ Requirements

Make sure you have Python 3.7 or higher installed. Then install the necessary Python packages:

```bash
pip install pyttsx3 speechrecognition
pip install pipwin
pipwin install pyaudio
