import ctypes
import datetime
import os
import random
import subprocess
import webbrowser

import pyautogui
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import wikipedia
import wolframalpha


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('je vous écoute')

        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("traitement")

            Query = r.recognize_google(audio, language='fr-FR')

            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            print("veuillez répéter")
            return "None"

        return Query


def speak(audio):
    engine = pyttsx3.init()

    engine.getProperty('voices')

    engine.setProperty('voice', 'french')
    engine.setProperty('rate', 150)
    engine.say(audio)

    engine.runAndWait()


def tellDay():
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Lundi', 2: 'Mardi',
                3: 'Mercredi', 4: 'jeudi',
                5: 'vendredi', 6: 'samedi',
                7: 'Dimanche'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("aujourd'hui nous sommes " + day_of_the_week)


def Hello():
    speak("bonjour")


def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


def Take_query():
    global time
    Hello()


def meteo():
    city = "Lausanne"
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=<2e3f2c15427eb61245d95866c3b3a163>&units=metric").json()
    temp = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    speak(f"La température est de {format(temp2)} degrée \n La météo est {format(temp)}")

    while (True):

        query = takeCommand().lower()
        if "ouvre youtube" in query or "lance youtube" in query:
            speak("je lance youtube bg ")

            webbrowser.open("www.youtube.com")
            continue

        elif "météo" in query:
            meteo()

        elif "ouvre google" in query or "lance google" in query:
            speak("ouverture en cour de Google ")
            webbrowser.open("www.google.com")
            continue

        elif "quel jour sommes-nous" in query:
            tellDay()
            continue

        elif 'mets la musique de' in query:
            chanteur = query.replace('mets la musique de', '')
            print(chanteur)
            pywhatkit.playonyt(chanteur)

        elif "déconnecte moi" in query:
            speak("verifier que les fenetres soient fermer avant ")
            subprocess.call(["shutdown", "/l"])

        elif 'bloque window' in query:
            speak("d'accord")
            ctypes.windll.user32.LockWorkStation()

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif 'heure' in query:
            time = datetime.datetime.now().strftime("%H:%M")
            print(time)
            speak('il est actuelement: ' + time)

        elif 'qui est' in query:
            person = query.replace("qui est", "")
            wikipedia.set_lang("fr")
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)
        elif "créer une alarme" in query:
            print("exemple de temps d'entrée:- 10 et 10 et 10")
            speak("Régler l'heure")
            a = input("quelle heure voulez-vous :- ")
            alarm(a)
            speak("c'est fait")

        elif "créer une note" in query:
            speak("que voulez vous que j'ecrive")
            note = takeCommand()
            file = open('natasha.txt', 'w')
            file.write(note)

        elif "montre-moi la note" in query:
            speak("la voici")
            file = open("natasha.txt", "r")
            speak(file.read(1000))

        elif "est-ce que tu veux être ma dulcinée" in query or "veux-tu être ma femme" in query:
            speak("je ne suis pas encore sur de ça,........peut être devrions nous prendre notre temps")

        elif "au revoir" in query:
            speak("Au revoir n'hesiter pas à me rappeler")
            exit()

        elif "je t'aime" in query:
            speak(" il en est de même pour moi , à part si vous n'êtes pas mon créateur")

        elif "calcul" in query:

            app_id = "2UWU65-WWG9PXP9Q3"
            client = wolframalpha.Client(app_id)
            index = query.lower().split().index('calcul')
            query = query.split()[index + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("le résulta est  " + answer)
            speak("le résultat est " + answer)


        elif "comment tu t'appelle" in query:
            speak("je suis natasha, t'as douce assistante")

        elif "merci" in query:
            speak("il n'y a pas de quoi")

        elif "question " in query:
            speak(
                'Je peux répondre à des questions informatiques et géographiques et quelle question voulez-vous poser maintenant')
            question = takeCommand()
            '2UWU65-WWG9PXP9Q3'
            client = wolframalpha.Client('2UWU65-WWG9PXP9Q3')
            res = client.query(question)
            answer = next(res.results).text
            speak("réponse")
            speak(answer)

        elif "comment tu vas" in query or "comment ça va" in query:
            speak("je vais bien, j'espère que vous aussi")


        elif "blague" in query:
            jokes = [
                "C’est la maîtresse qui demande à Toto « Cite-moi un mammifère qui n’a pas de dents »… « Ma grand-mère ? »",
                "C’est l’histoire de la maîtresse qui demande à Toto : « Récite-moi le verbe marcher au présent. » Toto répond ""« Je…marche…tu…tu…marches… », mais la maîtresse le presse, allez, plus vite Toto ! ""Ce à quoi il répond « je cours ..…tu cours il court… »"]
            speak(random.choice(jokes))

        elif "dépressif" in query or "dépression" in query:
            depressif = ["De nombreuses solutions existent pour se sentir mieux"
                         "Adopter un mode de vie sain : pratiquer un sport, une activité de relaxation (méditation, yoga…), respecter ses cycles de sommeil et manger de façon équilibrée peuvent être un premier rempart contre la dépression.",
                         "Sortir tous les jours, afin de vous exposer à la lumière naturelle du jour",
                         "Avoir une vie sociale riche. Que ce soit entre amis ou en famille, les liens sociaux sont très importants pur la bonne santé mentale.",
                         "Consulter dès les premiers signes de tristesse. Prenez rendez vous chez un psychologue, un psychothérapeute ou un psychanalyste afin de désamorcer rapidement les premiers symptômes. Le bouche-à-oreille vous permettra de trouver un bon praticien."]
            speak(random.choice(depressif))

        elif "c'est quoi " in query or "qui est" in query or "qu'est-ce que" in query:

            client = wolframalpha.Client("2UWU65-WWG9PXP9Q3")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

        elif 'cherche' in query:
            query = query.replace("cherche", "")
            webbrowser.open(query)


        elif ' cherche sur Wikipédia' in query:
            speak('recherche...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("selon wikipedia")
            print(results)
            speak(results)

        elif ("screen" in query):
            pyautogui.screenshot(str(()) + ".png").show()

            continue


if __name__ == '__main__':
    Take_query()
