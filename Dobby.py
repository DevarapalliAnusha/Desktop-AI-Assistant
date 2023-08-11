from calendar import month
from http import server
from msvcrt import kbhit
from re import search
import secrets
import pyjokes
import os
import psutil
import pyautogui
import pyttsx3
import datetime
import smtplib
import wikipedia
import webbrowser as wb
import speech_recognition as sr
run=pyttsx3.init()
def speak(audio):
    run.say(audio)
    run.runAndWait()
def time():
    Time=datetime.datetime.now().strftime('%H:%M:%S')
    speak(Time)
def date():
    date=datetime.datetime.now().day
    month=datetime.datetime.now().month
    year=datetime.datetime.now().year
    speak(date)
    speak(month)
    speak(year)
def wishing():
    hour=datetime.datetime.now().hour
    if hour>=1 and hour<12:
        speak('Good Morning Anusha')
    elif hour>=12 and hour<18:
        speak('Good Afternoon Anusha')
    elif hour>=18 and hour<24:
        speak('Good Evening Anusha')
    else:
        print('Good Evening')
    speak('The Current Time is')
    time()
    speak('The Current Date is')
    date()
    speak('I am Dobby. How may I help you today?')
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as pat:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(pat)
    try:
        print('Recognizing....')
        query=r.recognize_google(audio, language='en_in')
        print(query)
    except Exception as e:
        print(e)
        speak('say that again please...')
        return 'None'
    return query
def screenshot():
    img=pyautogui.screenshot()
    img.save('C:/Users/xyz/Dobby/ss.png')
def cpu():
    U=str(psutil.cpu_percent())
    speak('cpu is at '+U)
    B=psutil.sensors_battery()
    battery=B.percent
    speak('the battery is at'+str(battery))
def jokes():
    speak(pyjokes.get_joke())
if __name__=='__main__':
    wishing()
    while True:
        query=takecommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak('what should i search?')
            H=takecommand().lower()
            speak('Searching....')
            #k=query.replace('wikipedia','')
            result=wikipedia.summary((H),sentences=2)
            print(result)
            speak(result)
        elif 'chrome' in query:
            speak('what do i search?')
            Chromepath='C:/program Files/Google/Chrome/Application/chrome.exe %s'
            search=takecommand().lower()
            wb.get(Chromepath).open_new_tab(search+'.com')
        elif 'logout' in query:
            os.system("shutdown -1")
        elif 'shutdown' in query:
            os.system('shutdown /s/t/1')
        elif 'restart' in query:
            os.system('shutdown /r/t/1')
        #elif 'play songs' in query:
        #    songs_dir=
        elif 'remember that' in query:
            speak('what should i remember')
            D=takecommand().lower()
            speak('you said me to remember'+D)
            remember=open('D.txt','w')
            remember.write(D)
            remember.close()
        elif 'forgot' in query:
            P=open('D.txt','r')
            speak('you said me to remember that'+P.read())
        elif 'screenshot' in query:
            screenshot()
            speak('Done')
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'offline' in query:
            speak('ok Have a Good Day')
            quit()
