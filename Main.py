import pyttsx4 as n
import speech_recognition as sr
from news import *
from selenium_web import *
from yt_seleniu import *
import randfacts

engine = n.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()

speak("Hello sir, Im ceez your Voice assistant..")

with sr.Microphone() as source:  # Corrected: parentheses after Microphone
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("I'm also having a good day sir")
speak("what can i do for you")

with sr.Microphone() as source:  # Corrected: parentheses after Microphone
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("You Need information related to which topic?")
    with sr.Microphone() as source:  # Corrected: parentheses after Microphone
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)

    speak("Searching {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)
elif "play" and "video" in text2:
    speak("you want me to play which video")
    with sr.Microphone() as source:  # Corrected: parentheses after Microphone
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
        print("play {} on youtube".format(vid))
        speak("play {} on youtube".format(vid))

        assist = youtube()
        assist.play(vid)
elif "news" in text2:
    print("Sure Sir, Now i'll read news for you")
    speak("Sure Sir, Now i'll read news for you")
    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" or "facts" in text2:
    speak("Sure Sir")
    x = randfacts.get_fact()
    print(x)
    speak("Did You know that, " + x)
