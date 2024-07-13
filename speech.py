import speech_recognition
import pyttsx3
from gemini import Provider

recognizer = speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google_cloud(audio)
            text = text.lower()
            desc = Provider(text)
            print(desc)
    
    except speech_recognition.UnknownValueError():
        recognizer = speech_recognition.Recognizer()
        continue

            
        