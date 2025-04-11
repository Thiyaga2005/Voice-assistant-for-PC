import pyttsx3
import speech_recognition as sr
import subprocess as sp
import os
import wikipedia
import pywhatkit
import pyautogui
import pyjokes
import imdb
import wolframalpha
import psutil
import webbrowser

from online import youtube, find_my_ip, search_on_google, get_news, weather_forecast, send_whatsapp_message, \
    get_random_advice
from datetime import datetime
from decouple import config
from random import choice
from conv import random_text

engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 2)
engine.setProperty('rate', 230)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

USER = config('USER')
HOSTNAME = config('BOT')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_me():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good morning {USER}")
    elif (hour >= 12) and (hour <= 16):
        speak(f"Good afternoon {USER}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good evening {USER}")
    speak(f"I am {HOSTNAME}. How may i assist you?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        queri = r.recognize_google(audio, language='en-in')
        print(queri)
        if not 'stop' in queri or 'exit' in queri:
            speak(choice(random_text))
        else:
            hour = datetime.now().hour
            if (hour >= 21) and (hour < 6):
                speak("Good night sir,take care!")

            else:
                speak("Have a good day sir!")
            exit()

    except Exception as e:
        print(e)
        speak("sorry i couldn't understand.can you please repeat that?")
        queri = 'None'
    return queri


def social_media(command):
    if 'facebook' in command:
        speak("opening your facebook")
        webbrowser.open("https://www.facebook.com/")
    elif 'whatsapp' in command:
        speak("opening your whatsapp")
        webbrowser.open("https://web.whatsapp.com/")
    elif 'discord' in command:
        speak("opening your discord server")
        webbrowser.open("https://discord.com/")
    elif 'instagram' in command:
        speak("opening your instagram")
        webbrowser.open("https://www.instagram.com/")
    else:
        speak("No result found")


def condition():
    usage = str(psutil.cpu_percent())
    speak(f"CPU is at {usage} percentage")
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"Boss our system have {percentage} percentage battery")

    if percentage >= 80:
        speak("Boss we could have enough charging to continue our recording")
    elif percentage >= 40 and percentage <= 75:
        speak("Boss we should connect our system to charging point to charge our battery")
    else:
        speak("Boss we have very low power, please connect to charging otherwise recording should be off...")


if "__main__" == __name__:
    greet_me()
    while True:
        query = take_command().lower()
        if "how are you" in query:
            speak(f"I am absolutely fine sir. what about you")

        if "good bye" in query or "ok bye" in query or "stop" in query:
            speak('your personal assistant FRIDAY is shutting down,Good bye')
            print('your personal assistant FRIDAY is shutting down,Good bye')
            break

        if "time" in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir,the time is {strTime}")

        elif "open command prompt" in query:
            speak("Opening command prompt for you sir")
            os.system("start cmd")

        elif "open camera" in query:
            speak("Opening camera for you sir")
            sp.run('start microsoft.windows.camera:', shell=True)

        elif 'wikipedia' in query:
            speak("searing in wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to wikipedia,")
            print(results)
            speak(results)

        elif 'tell me about' in query:
            ask = query.replace('tell me about', '')
            info = wikipedia.summary(ask, 2)
            print(info)
            speak(info)

        elif 'play' in query:
            query = query.replace('play', '')
            speak('playing' + query)
            pywhatkit.playonyt(query)

        elif 'mute' in query:
            speak("I'm Muting sir...")
            break

        elif "open youtube" in query:
            speak("what do you want to play on youtube sir?")
            video = take_command().lower()
            youtube(video)

        elif "open google" in query:
            speak(f"what do you want to search on google {USER}")
            query = take_command().lower()
            search_on_google(query)

        elif 'who are you' in query or 'what can you do' in query:
            speak('I am FRIDAY version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,predict time,take a photo,search wikipedia,predict weather'
                  'in different cities , get top headline news and you can ask me computational or geographical '
                  'questions too!')
            print('I am FRIDAY version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,predict time,take a photo,search wikipedia,predict weather'
                  'in different cities , get top headline news and you can ask me computational or geographical '
                  'questions too!')

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = pyjokes.get_joke()
            speak("For your convenience, I am printing it on the screen sir.")
            print(joke)
            speak(joke)

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by THIYAGARAJAN")
            print("I was built by THIYAGARAJAN")

        elif 'exit program' in query:
            speak("I'm Leaving sir, BYE!")
            quit()

        elif 'open chrome' in query:
            speak("Opening Chrome for you sir... ")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk")
            while True:
                chromeQuery = take_command().lower()
                if "search" in chromeQuery:
                    youtubeQuery = chromeQuery
                    youtubeQuery = youtubeQuery.replace("search", "")
                    pyautogui.write(youtubeQuery)
                    pyautogui.press('enter')
                    speak('searching...')

                elif "close chrome" in chromeQuery or "exit chrome" in chromeQuery or "exit google" in chromeQuery or "close window" in chromeQuery or "close this window" in chromeQuery:
                    pyautogui.hotkey('ctrl', 'w')
                    speak("closing chrome sir...")
                    break

        elif " what can you do for me" in query:
            speak('Yes sir,Nice Question')
            speak('anything you want i do for you sir')

        elif "cool" in query or "nice" in query or "awesome" in query or "thank you" in query or "great" in query:
            speak("Yes sir, That's my Pleasure!")

        elif "waste" in query or "useless" in query:
            speak("Please Don't say boss, I do my best for you")

        elif "minimize" in query or 'minimise' in query:
            speak('minimizing Sir')
            pyautogui.hotkey('win', 'down', 'down')

        elif "maximize" in query or 'maximise' in query:
            speak('Maximize Sir')
            pyautogui.hotkey('win', 'up', 'up')

        if "volume up" in query or "volume increase" in query:
            speak('volume increasing sir...')
            pyautogui.press('volumeup')

        if "volume down" in query or "volume decrease" in query:
            speak('volume decreasing sir...')
            pyautogui.press('volumedown')

        if 'volume mute' in query:
            speak('volume muteing sir...')
            pyautogui.press('volumemute')

        elif "close the window" in query or 'close the application' in query or "close window" in query or "close application" in query:
            speak('closing Sir')
            pyautogui.hotkey('ctrl', 'w')

        elif "screenshot" in query:
            speak("Taking screenshot sir...")
            pyautogui.press('prtsc')

        elif "open notepad" in query:
            speak("opening notepad sir...")
            os.startfile("C:\\Windows\\SysWOW64\\notepad.exe")
            while True:
                notepadQuery = take_command().lower()
                if "paste" in notepadQuery:
                    pyautogui.hotkey('ctrl', 'v')
                    speak("done sir")
                elif "save this file" in notepadQuery:
                    pyautogui.hotkey('ctrl', 's')
                    speak("Sir, Please Specify a name for this file")
                    notepadSavingQuery = take_command()
                    pyautogui.write(notepadSavingQuery)
                    pyautogui.press('enter')
                elif 'type' in notepadQuery:
                    speak("please Tell me what should i write...")
                    while True:
                        writeInNotepad = take_command()
                        if writeInNotepad == 'exit typing':
                            speak("Done sir")
                            break
                        else:
                            pyautogui.write(writeInNotepad)

                elif "exit notepad" in notepadQuery or 'close notepad' in notepadQuery:
                    speak('quiting notepad sir...')
                    pyautogui.hotkey('ctrl', 'w')
                    break

        elif 'play song' in query or ' sing a song' in query or 'play a song' in query:
            speak("Yes Sir Please wait a moment")
            songs = os.listdir("C:\\Users\\Admin\\Music")
            os.startfile(os.path.join("C:\\Users\\Admin\\Music", songs[0]))

        elif 'what are you doing' in query:
            speak('hmmm.. I am damn busy but you can ask something i can help you sir!')
            print('hmmm.. I am damn busy but you can ask something i can help you sir!')

        elif 'pause' in query or 'pass' in query:
            pyautogui.press('space')
            speak('done sir')

        elif 'open pycharm' in query or 'open python' in query:
            speak("Opening pycharm for you sir... ")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community "
                         "Edition 2023.2.3.lnk")

        elif "give me news" in query:
            speak(f"I am reading out the latest headline of today,sir")
            speak(get_news())
            speak("I am printing it on screen sir")
            print(get_news(), sep='\n')

        elif "movie" in query:
            movies_db = imdb.IMDb()
            speak("I can tell all movie information")
            speak("Please tell me the movie name:")
            text = take_command()
            movies = movies_db.search_movie(text)
            speak("searching for" + text)
            speak("I found these")
            for movie in movies:
                title = movie["title"]
                year = movie["year"]
                speak(f"{title}-{year}")
                info = movie.getID()
                movie_info = movies_db.get_movie(info)
                rating = movie_info["rating"]
                cast = movie_info["cast"]
                actor = cast[0:5]
                plot = movie_info.get('plot outline', 'plot summary not available')
                speak(f"{title} was released in {year} has imdb ratings of {rating}.It has a cast of {actor}. The "
                      f"plot summary of movie is {plot}")

                print(f"{title} was released in {year} has imdb ratings of {rating}.It has a cast of {actor}. The "
                      f"plot summary of movie is {plot}")

        elif "calculate" in query:
            app_id = "48XAWW-VLGUPEK9V5"
            client = wolframalpha.Client(app_id)
            ind = query.lower().split().index("calculate")
            text = query.split()[ind + 1:]
            result = client.query(" ".join(text))
            try:
                ans = next(result.results).text
                speak("The answer is " + ans)
                print("The answer is " + ans)
            except StopIteration:
                speak("I couldn't find that . Please try again")

        elif "weather" in query:
            ip_address = find_my_ip()
            speak("Tell me the name of your city")
            city = input("Enter name of your city:")
            speak(f"Getting weather report of your {city}")
            weather, temp, feels_like = weather_forecast(city)
            speak(f"The current temperature is {temp},but it feels like {feels_like}")
            speak(f"Also the weather report talks about {weather}")
            speak("I am printing weather info on screen")
            print(f"Description:{weather}\\nTemperature:{temp}\\nFeels like: {feels_like}")

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif "how much power left" in query or "battery" in query or "battery power" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")
            speak("i'm printing on screen sir...")
            print(f"system have {percentage} percent battery")

        elif "send whatsapp message" in query:
            speak(
                'On what number should I send the message sir? Please enter in the number: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_command().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            print(advice)

        if ('facebook' in query) or ('discord' in query) or ('whatsapp' in query) or ('instagram' in query):
            social_media(query)

        elif ("system condition" in query) or ("condition of the system" in query):
            speak("checking the system condition")
