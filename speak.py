# speak.py
import pyttsx3

def speak_text(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 120)  # Speed of speech
        engine.setProperty('volume', 1)  # Volume 0.0 to 1.0
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Voice error: {e}")
