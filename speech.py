import speech_recognition as sr
import pyttsx3
from gemini import Provider

recognizer = sr.Recognizer()


mic_index = 0 


recognizer = sr.Recognizer()


try:
    with sr.Microphone(device_index=mic_index) as mic:
        print(f"\nUsing microphone:")
        recognizer.adjust_for_ambient_noise(mic, duration=0.5)
        print("Please say something into the microphone.")
        audio = recognizer.listen(mic, timeout=5)
        print("Audio captured successfully!")

        
        try:
            text = recognizer.recognize_google(audio)
            text = text.lower()

            desc = Provider(text)
            print('Description: \n',desc)

        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

except sr.WaitTimeoutError:
    print("Listening timed out while waiting for phrase to start")
except Exception as e:
    print(f"An error occurred: {e}")
            
        