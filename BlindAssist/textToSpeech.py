from gtts import gTTS
import pygame, os, time


def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    # Wait until the audio finishes playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)  # Sleep for a while to avoid busy-waiting

    # Uninitialize the mixer to release the file
    pygame.mixer.quit()

    # Clean up the audio file
    os.remove("output.mp3")

