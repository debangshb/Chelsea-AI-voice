import sys
import webbrowser
import pyttsx3
import os
from requests.api import head
import speech_recognition as sr
import datetime
import random
import requests
import wikipedia
import pywhatkit as kit
import smtplib
import pyjokes
import pyautogui
import time
from geopy.geocoders import Nominatim


engiene=pyttsx3.init('sapi5')
voices= engiene.getProperty('voices')
print(voices[1].id)
engiene.setProperty('voice', voices[2].id)

def speak(audio):
    engiene.say(audio)
    print(audio)
    engiene.runAndWait()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=2
        r.energy_threshold=700
        audio=r.listen(source, timeout=1, phrase_time_limit=5)


        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            speak("Please say that again....")
            return 'none'
        return query


def wishme():
    hour=int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<12:
        watch = datetime.date.today()
        speak("Good Morning")
        speak(f"I am chelsea Sir. It is {watch} and the time is {tt} . Please tell me how can i help you?")

    elif hour>=12 and hour<18:
        watch = datetime.date.today()
        
        speak("Good Afternoon")
        speak(f"I am chelsea Sir. It is {watch} and the time is {tt} . Please tell me how can i help you?")


    else:
        watch = datetime.date.today()
        
        speak("Good Evening")
        speak(f"I am chelsea Sir. It is {watch} and the time is {tt} . Please tell me how can i help you?")


    


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    speak("sir put your email id and password")
    email = input()
    password=input()
    server.login(f'{email}', f'{password}')
    server.sendmail(email, to, content)
    server.close()


def news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=55c8054b804f4e16a6f7c465f022538e'

    main_page = requests.get(main_url).json()
    articles = main_page['articles']
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear()
    wishme()
    while True:

        query=takeCommand().lower()

        if 'open notepad' in query:
            ntpath = 'C:\\Windows\\system32\\notepad.exe'
            os.startfile(ntpath)

        elif 'close notepad' in query:
            speak("Okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'open adobe reader' in query:
            adrpath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\adobereaderx.ink'
            os.startfile(adrpath)

        elif 'close adobe reader' in query:
            speak("Okay sir, closing notepad")
            os.system("taskkill /f /im adobereaderx.ink")

        elif 'open command prompt' in query:
            cmdpath = 'C:\\Windows\\system32\\cmd.exe'
            os.startfile(cmdpath)

        elif 'close command prompt' in query:
            speak("Okay sir, command prompt")
            os.system("taskkill /f /im cmd.exe")

        
        # elif 'open camera' in query:
        #     cap = 
        # elif "camera" in query or "take a photo" in query:
        #     ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif 'play music' in query:
            music_dir = "D:\\e backup\\Manna"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, rd))

        elif 'stop music' in query:
            speak("Okay sir, stopping music")
            os.system("taskkill /f /im wmplayer.exe")

        elif 'open google' in query:
            crmpath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(crmpath)

        elif 'close google' in query:
            speak("Okay sir, closing google")
            os.system("taskkill /f /im chrome.exe")

        
        elif 'ip address' in query:
            ip = requests.get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")
            print(ip)

        elif 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'close youtube' in query:
            speak("Okay sir, closing youtube")
            os.system("taskkill /f /im iexplore.exe")
            

        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com")

        elif 'close instagram' in query:
            speak("Okay sir, closing instagram")
            os.system("taskkill /f /im chrome.exe")

        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")

        elif 'close facebook' in query:
            speak("Okay sir, closing facebook")
            os.system("taskkill /f /im chrome.exe")


        elif 'open geeksforgeeks' in query:
            webbrowser.open("www.geeksforgeeks.org")

        elif 'close geeksforgeeks' in query:
            speak("Okay sir, closing geeksforgeeks")
            os.system("taskkill /f /im chrome.exe")


        elif 'search something' in query:
            speak("What do you want to search")
            sch= takeCommand().lower()
            webbrowser.open(f"{sch}")

        elif 'send a message' in query:
          speak("what should i say sir")
          msg=takeCommand()
          speak("to whom should i send")
          to=takeCommand()
          hr= int(datetime.datetime.now().hour)
          min= int(datetime.datetime.now().minute)  
          kit.sendwhatmsg(f"+91{to}",f"{msg}" ,20,13)

        elif 'listen a song on youtube' in query:
            speak("what do you want to listen sir")
            music = takeCommand()
            kit.playonyt(f"{music}")

        elif 'email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                speak("Sir please write the email id To whom should i send")    
                to = input()
                sendEmail(to, content)
                speak("Email has been sent Sir")

            except Exception as e:
                print(e)
                speak("Sorry Sir, I am unable to send this email")

        elif 'elif set alarm' in query:
            nm= int(datetime.datetime.now().hour)
            speak("When should i set the alarm Sir?")
            alrm= takeCommand()
            if nm==alrm:
                music_dir = 'D:\\e backup\\MANER MANUS'
                songs=os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        elif 'you can sleep' in query:
         speak("Thanks for using me sir, have a good day")       
         sys.exit()

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'shutdown the system' in query:
            os.system("shutdown /s /t S")

        elif 'restart the system' in query:
            os.system("shutdown /r /t S")

        elif 'sleep the system' in query:
            os.system("Rundll32.exe powrprof.dll,SetSuspendState Sleep 0,1,0")  

        elif 'switch the window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif 'tell me the news' in query:
            speak("Please wait sir, fetching the latest news")
            news()

        elif 'Where i am' in query or 'where we are' in query:
            speak("Please wait Sir, let me check")
            try:
                ipadd = requests.get('https://api.ipify.org').text
                print(ipadd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"Sir I am not sure but I think we are in {city} city of country {country}")
            except Exception as e:
                speak("Sorry sir due to network issue i am not able to find where we are")
                pass

        # elif 'profile picture' or 'instagram profile' in query:
        #     speak("sir please enter the user name correctly")
        #     name = input("Enter the username here : ")
        #     webbrowser.open(f"www.instagram.com/{name}")
        #     speak(f"here is the profile of {name}")
        #     time.sleep(10)
        #     speak("Sir would you like to download the profile picture of this account.")
        #     condition = takeCommand().lower()
        #     if 'yes' in condition:
        #         mod = insta


        elif 'take screenshot' in query or 'take a screenshot' in query:
            speak("Please tell me the name for this screenshot file")
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done sir. The screenshot is saved in our main folder")

        else:
            pass
            