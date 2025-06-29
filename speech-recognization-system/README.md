# 🎙️ Speech Recognition System in Python

Welcome to the **Speech Recognition System** – a simple Python project that captures speech through a microphone and converts it into text using the Google Speech Recognition API.

🔗 **GitHub Repository**:  
https://github.com/arnabkundu03/speech-recognition-system/tree/master/speech-recognization-system

---

## 🧠 Features

- Captures real-time audio from your microphone.
- Adjusts to ambient noise for more accurate recognition.
- Converts spoken words to text using Google’s API.
- Provides feedback on errors like unclear audio or connection issues.

---

## 🚀 Getting Started

Follow these steps to run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/arnabkundu03/speech-recognition-system.git
cd speech-recognition-system/speech-recognization-system
```

### 2. (Optional) Create a Virtual Environment

```python -m venv venv```
Activate the environment:
On Windows:
```venv\Scripts\activate```
On macOS/Linux:
```source venv/bin/activate```

### 3. Install Required Packages

```pip install -r requirements.txt```

⚠️ PyAudio Installation Note (Windows Users)
If you face issues with pyaudio, install it via pipwin:

```
pip install pipwin
pipwin install pyaudio
```

### ▶️ Run the Speech Recognition System

```python main.py```
Speak into your microphone when prompted, and the system will transcribe your voice to text.

### 📦 Requirements

The ```requirements.txt``` file includes:
```
SpeechRecognition
pyaudio
```

### ❓ Troubleshooting

1. ```ModuleNotFoundError: No module named 'pyaudio'```
→ Install it using ```pipwin install pyaudio``` on Windows.

2. Microphone not recognized
→ Ensure your microphone is properly connected and configured.
