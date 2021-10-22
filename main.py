import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import pandas as pd
from bs4 import BeautifulSoup
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

# link for extract html data
def getdata(url):
    r = requests.get(url)
    return r.text

def run_alexa():
    command = take_command()
    print(command)
    if 'hr' in command:
        link = "https://sites.google.com/calcey.com/calcey-hr/home"
        # with urllib.request.urlopen(link) as f:
        # # f = urllib.urlopen(link)
        #     myfile = f.read()
        #     print(myfile)
        #     talk('Calcey HR')
        #     talk(myfile)

        # response = requests.get('http://hiscore.runescape.com/index_lite.ws?player=zezima')
        # print (response.status_code)
        # print (response.content)
        # talk('Calcey HR')
        # talk(response.content)

        webbrowser.open(link)  # Go to hr site

        htmldata = getdata(link)
        soup = BeautifulSoup(htmldata, 'html.parser')
        data = ''
        talk('Calcey HR')
        for data in soup.find_all("p"):
            talk(data)
            print(data.get_text())

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()