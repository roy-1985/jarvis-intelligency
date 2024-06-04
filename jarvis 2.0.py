import time
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import webbrowser
import os
import cv2
import socket
import wikipedia
import pywhatkit as kit
import sys
import pyjokes
import pyautogui
import PyPDF2


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=e2d196f3b259479fa402456a1051aa30"

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for x in articles:
        head.append(x["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")



def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        print("listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
        except Exception as e:
            speak("I couldn't recognise sir")
            return "none"
        return query

def pdf_reader():
    book = open("EndTerm QPF (studify.space) 2 (1).pdf","rb")
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    speak(f"total pages in this pdf is {pages}")
    speak("shouvik enter page number that i have to read")
    pg = int(takeCommand())
    page = pdfreader.getPage(pg)
    text = page.extractText()
    speak(text)

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<= 12:
        speak("good morning shouvik")
    elif hour>12 and hour<18:
        speak("good evening shouvik")
    else:
        speak("good evening shouvik")
    speak("hey im ramlal how could i help you")

if __name__ == "__main__":
    wish()
    while True:
        query = takeCommand().lower()
        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://google.com"]]
        for x in sites:
            if f"Open {x[0]}".lower() in query:
                speak(f"Jarvis is opening {x[0]} for you SHOUVIK")
                webbrowser.open(x[1])

        if "open notepad".lower() in query:
            path = "C:\\Windows\\WinSxS\\wow64_microsoft-windows-notepad_31bf3856ad364e35_10.0.22621.1_none_db050381981eadad"
            speak("jarvis is opening notepad for you")
            os.startfile(path)
        elif "open powerpoint".lower() in query:
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
            speak("jarvis is opening powerpoint for you")
            os.startfile(path)
        elif "open camera".lower() in query:
            speak("jarvis is opening camera for you shouvik")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(40)
                if k == 7:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif "ip address".lower() in query:
            def get_ip_address(hostname):
                try:
                    ip_address = socket.gethostbyname(hostname)
                    return ip_address
                except socket.error as e:
                    print(f"Error: {e}")
                    return None


            # Example: Get the IP address of www.example.com
            hostname_to_lookup = "www.google.com"
            ip_address = get_ip_address(hostname_to_lookup)

            if ip_address:
                speak(f"The IP address is {ip_address}")
            else:
                speak(f"Failed to retrieve the IP address")

        elif "wikipedia".lower() in query:
            speak("searching sir..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences= 3)
            speak("according to wikipedia")
            speak(results)

        elif "want to know".lower() in query:
            speak("what do you want to know Shouvik?")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message".lower() in query:
            speak("whom do you want to send")
            number = takeCommand()
            speak("what do you wnat to text")
            text = takeCommand()
            kit.sendwhatmsg(number, text)

        elif "play songs".lower() in query:
            speak("which song you want to listen shouvik")
            kit.playonyt(takeCommand())

        elif "tell me a joke".lower() in query:
            joke = pyjokes.get_jokes()
            speak(joke)
        elif "shutdown system".lower() in query:
            os.system("shutdown /s /t 5")
        elif "restart system".lower() in query:
            os.system("shutdown /r /t 5")
        elif "switch the window".lower() in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif "no thanks".lower() in query:
            speak("Thank you shouvik have a great day")
            sys.exit()
        elif "today's news".lower() in query:
            speak("please wait shouvik, fetching the news")
            news()

        elif "where am i".lower() in query or "where we are".lower() in query:
            speak("let me analyse shouvik")
            try:
                ipadd = requests.get("https://api.ipify.org").text
                print(ipadd)
                url = "https://get.geojs.io/v1/ip/geo"+ipadd+".json"
                geo_request = requests.get(url)
                geo_data = geo_request.json()
                city = geo_data["city"]
                state = geo_data["state"]
                con = geo_data["country"]
                speak(f"we are at {city} of {state} in {con}")
            except Exception as e:
                speak("sorry shouvik i couldn't analyse where we are")
                pass
        elif "take screenshot".lower() in query:
            speak("what would you like to name the screenshot")
            name = takeCommand().lower()
            speak("wait for seconds im taking screenshot")
            time.sleep(5)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("im done shouvik you may check")
        elif "read pdf".lower() in query:
            pdf_reader()
        elif "hide all files".lower() in query or "visible for everyone".lower() in query:
            speak("do you want to hide or make it visible")
            condition = takeCommand().lower()
            if "hide".lower() in condition:
                os.system("attrib +h /s /d")
                speak("all the files are hidden successfully")
            elif "visible".lower() in condition:
                os.system("attrib -h /s /d")
                speak("all the files are visible now")
            elif "leave it".lower() in condition:
                speak("ok shouvik")

        speak("anything else i could do for you shouvik")











