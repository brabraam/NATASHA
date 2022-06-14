import pyttsx3
import datetime
import os

def speak(audio):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice', 'french')
    engine.setProperty('rate', 150)
    engine.say(audio)

    engine.runAndWait()

extractedtime = open("Alarmtext.txt","r")
time = extractedtime.read()
time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt","r")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("natsha","")
    timenow = timenow.replace("créer une alarm","")
    timenow = timenow.replace("et", "")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True :
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("l'alarme sonne")
            os.startfile("music.mp3")
        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(time)