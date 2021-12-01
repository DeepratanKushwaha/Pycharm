import pyjokes
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import pywhatkit as kit
from requests import get

# import cv2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning')
    elif 12 <= hour < 18:
        speak('Good Afternoon')
    else:
        speak('Good Evening!')

    speak('I am Jarvis Sir. Please tell me how may I help you')


def takeCommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print(e)
        print('Say that again please...')
        return 'None'
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('deepratankushwah@gmail.com', '*******')
    server.sendmail('deepratankushwah@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('Wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            speak(results)

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak('what should i search on google')
            m = takeCommand().lower()
            speak('searching on google')
            webbrowser.open(f'{m}')

        elif 'open stackoverflow' in query:
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')

        elif 'open github' in query:
            speak('opening github')
            webbrowser.open('github.com')

        elif 'open gmail' in query:
            speak('opening gmail')
            webbrowser.open('gmail.com')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\deepr_000\\Downloads\\meme\\audio'
            songs = os.listdir(music_dir)
            s = random.randint(0, len(songs))
            speak('playing songs')
            os.startfile(os.path.join(music_dir, songs[s]))

        elif 'time right now' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {strTime}')

        elif 'open notepad' in query:
            codePath = 'C:\\WINDOWS\\system32\\notepad.exe'
            speak('opening notepad')
            os.startfile(codePath)

        elif 'start github desktop' in query:
            codePath = 'C:\\Users\\deepr_000\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe'
            speak('opening github desktop')
            os.startfile(codePath)

        elif 'open pycharm' in query:
            codePath = "C:\\Users\\deepr_000\\PyCharm Community Edition 2020.3.3\\bin\\pycharm64.exe"
            speak('opening pycharm')
            os.startfile(codePath)

        elif 'email to me' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = 'deepratankushwah@gmail.com'
                sendEmail(to, content)
                speak('Email has been sent successfully!')
            except Exception as e:
                print(e)
                speak(f"Sorry sir, I'm not able to send this email {e}.")

        elif 'send message' in query:
            kit.sendwhatmsg('+919887410890', 'this is testing message send by a programming script', 19, 53,
                            wait_time=10, print_wait_time=True, browser='chrome', tab_close=True)

        elif 'search on youtube' in query:
            speak('what do you want to search')
            n = takeCommand().lower()
            speak(f'searching {n}')
            kit.playonyt(f'{n}')

        elif 'show my ip address' in query:
            ip = get('https://api/ipify.org').text
            speak(f'your IP Address is {ip}')

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'shut down the system' in query:
            speak('shut down the system')
            os.system('shutdown /s /t 5')

        elif 'restart the system' in query:
            speak('restart the system')
            os.system('shutdown /r /t 5')

        elif 'good night system' in query:
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        elif 'close notepad' in query:
            speak('ok sir, closing notepad')
            os.system('taskkill /f /im notepad.exe')

        elif 'open camera' in query:
            pass

        elif 'quit jarvis' in query:
            speak('Thank you sir, good bye')
            quit()
