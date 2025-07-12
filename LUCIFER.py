import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
from ecapture import ecapture as ec
import time
import subprocess
import wolframalpha
import requests
import pyautogui as pygui
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from LUCYGUI import Ui_LUCYGUI
import sys
import random
import re
import pprint
import urllib.parse
import pywhatkit

GREETINGS = ["hello lucy", "lucy", "wake up lucy", "you there lucy", "time to work lucy", "hey lucy",
             "ok lucy", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

print('Loading your AI personal assistant Lucy ')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

def write(var):
    pygui.typewrite(var + "\n", 0.5)
def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
def startup():
    speak("Initializing Lucy.")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am Lucy. Online and ready sir. Please tell me how may I help you")
def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None







class MainTherad(QThread):

    def __init__(self):
        super(MainTherad,self).__init__()


    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        startup()

        while True:


            self.statement = self.takeCommand().lower()


            if "goodbye" in self.statement or "okbye" in self.statement or "stop" in self.statement or "Thankyou" in self.statement:
                speak('your personal assistant lucy is shutting down,Good bye')
                print('your personal assistant lucy is shutting down,Good bye')
                break

            elif self.statement in GREETINGS:
                speak(random.choice(GREETINGS_RES))

            elif 'wikipedia' in self.statement:
                speak('Searching Wikipedia...')
                statement = self.statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)


            elif 'open youtube' in self.statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")



            elif 'open google' in self.statement or "open chrome" in self.statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google chrome is open now")


            elif 'open gmail' in self.statement:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail open now")

            elif "weather" in self.statement:
                api_key = "8ef61edcf1c576d65d836254e11ea420"
                base_url = "https://api.openweathermap.org/data/2.5/weather?"
                speak("whats the city name")
                city_name = self.takeCommand()
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in kelvin unit is " +
                          str(current_temperature) +
                          "\n humidity in percentage is " +
                          str(current_humidiy) +
                          "\n description  " +
                          str(weather_description))
                    print(" Temperature in kelvin unit = " +
                          str(current_temperature) +
                          "\n humidity (in percentage) = " +
                          str(current_humidiy) +
                          "\n description = " +
                          str(weather_description))

                else:
                    speak(" City Not Found ")


            elif 'tell me' in self.statement:
                queryy = self.statement.replace("tell me", "")
                app_id = "5PKUHJ-85LRET7P89"
                client = wolframalpha.Client(app_id)
                res = client.query(queryy)
                answer = next(res.results).text

                print(answer)
                speak(answer)

            elif 'time' in self.statement:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            elif 'who are you' in self.statement or 'what can you do' in self.statement:
                speak('I am lucy version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                      'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,'
                      'predict weather '
                      'in different cities , get top headline news from times of india and you can ask me computational '
                      'or geographical questions too!')


            elif "who made you" in self.statement or "who created you" in self.statement or "who discovered you" in self.statement:
                speak("I was built by Sushil Mishra, dude! he is graet ")
                print("I was built by Mirthula")

            elif "open stackoverflow" in self.statement:
                webbrowser.open_new_tab("https://stackoverflow.com/login")
                speak("Here is stackoverflow")


            elif 'news' in self.statement:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Happy reading')


            elif 'search' in self.statement:
                statement = self.statement.replace("search", "")
                webbrowser.open_new_tab(statement)





            elif "log off" in self.statement or "sign out" in self.statement:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])

            elif "write" in self.statement:
                statement = self.statement.replace("write", "")
                write(statement)
            elif "put " in self.statement:
                statement = self.statement.replace("put", "")
                write(statement)
            elif "fill with" in self.statement:
                statement = self.statement.replace("fill with", "")
                write(statement)

            elif "type" in self.statement:
                statement = self.statement.replace("type", "")
                write(statement)
            

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=0.1, phrase_time_limit=7)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            print("Pardon me, please say that again")
            return "None"
        return statement

startExecution=MainTherad()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_LUCYGUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie=QtGui.QMovie("C:/Users/SATISH/Desktop/ui.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
     
        startExecution.start()

    def showTime(self):
        curent_time=QTime.currentTime()
        label_time=current_time.toString("hh:mm:ss")
        self.ui.textBrowser.setText(label_time)


app=QApplication(sys.argv)
Lucy=Main()
Lucy.show()
exit(app.exec_())
