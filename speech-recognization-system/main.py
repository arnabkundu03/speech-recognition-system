import speech_recognition as sr

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\n🔄 Adjusting for ambient noise... (1 sec)")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            print("🎙️ Speak now...")
            audio = recognizer.listen(source)

            print("🧠 Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"\n✅ You said: {text}")

    except sr.UnknownValueError:
        print("😕 Could not understand your speech.")
    except sr.RequestError:
        print("🚫 Could not connect to the speech recognition service.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    print("🗣️ Speech Recognition System Initialized")
    recognize_speech_from_mic()
