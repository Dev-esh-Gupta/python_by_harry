import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import pygame
import os

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
NEWSAPI = "c45f74b0c3784c79a23346498a1e91b8"

def old_speak(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")


def process_command(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        print(c)
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        print("Hi")
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWSAPI}")

        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            titles = [article['title'] for article in articles]
            for i, title in enumerate(titles, start=1):
                speak(f"{i}. {title}")
                if int(i) == 10:
                    break
        else:
            speak(f"Failed to retrieve news: {response.status_code}")
    else:
        # We can add any AI client that answers you
        # I will gonna try llma 2 later on
        pass

    

if __name__ == "__main__":
    speak("Initialization of Jarvis.....")
    # Listen for the wake word "Jarvis"
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            # print("Sphinx thinks you said " + r.recognize_sphinx(audio))
            print("Recognising...")
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes Devesh")
                # Listen for Command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    process_command(command)


            # print(command)
        except Exception as e:
            print("Error; {0}".format(e))