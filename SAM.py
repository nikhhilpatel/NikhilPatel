import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import time
import os # to remove created audio files
from PIL import Image
import subprocess
import pyautogui #screenshot
import pyttsx3
import bs4 as bs
import urllib.request
import pyscreenshot as ImageGrab
import smtplib
import datetime
from tkinter import *



class person:
    name = ''
    def setName(self, name):
        self.name = name

class sam:
    name = ''
    def setName(self, name):
        self.name = name

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        engine_speak("Good Morning!")

    elif hour>=12 and hour<18:
        engine_speak("Good Afternoon!")   

    else:
        engine_speak("Good Evening!")  

    engine_speak("I am your Desktop Assistant SAM . Please tell me how may I help you")       

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your_mail_id', 'PWD')
    server.sendmail('mail_id', to, content)
    server.close()

def online():
    engine_speak('ok sir')
    engine_speak('starting all system applications')
    engine_speak('installing all drivers')
    os.system('start c:/Rainmeter.exe')
    engine_speak('every driver is installed')
    engine_speak('all systems have been started')
    engine_speak('now i am online sir')

def respond(voice_data):
    # 1: greeting
    if there_exists(['hey','hi','hello']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            engine_speak("whats with my name ")
        else:
            engine_speak("i dont know my name . what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name) # remember name in person object
    
    if there_exists(["your name should be"]):
        sam_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + sam_name)
        sam_obj.setName(sam_name) # remember name in sam object

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)

    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        engine_speak(time)

    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")

     #7: get stock price
    if there_exists(["price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")
    


     #8 time table
    if there_exists(["show my time table"]):
        im = Image.open(r"C:/-/")
        im.show()
    
     #9 weather
    if there_exists(["weather"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")
     

     #10 stone paper scisorrs
    if there_exists(["game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves=["rock", "paper", "scissor"]
    
        cmove=random.choice(moves)
        pmove=voice_data
        

        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        #engine_speak("hi")
        if pmove==cmove:
            engine_speak("the match is draw")
        elif pmove== "rock" and cmove== "scissor":
            engine_speak("Player wins")
        elif pmove== "rock" and cmove== "paper":
            engine_speak("Computer wins")
        elif pmove== "paper" and cmove== "rock":
            engine_speak("Player wins")
        elif pmove== "paper" and cmove== "scissor":
            engine_speak("Computer wins")
        elif pmove== "scissor" and cmove== "paper":
            engine_speak("Player wins")
        elif pmove== "scissor" and cmove== "rock":
            engine_speak("Computer wins")

     #11 toss a coin
    if there_exists(["toss","flip","coin"]):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        engine_speak("The computer chose " + cmove)

     #12 calc
    if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")
        
     #13 screenshot
    if there_exists(["capture","my screen","screenshot","take a snap"]):
        myScreenshot = pyautogui.screenshot()
        engine_speak("Ok done")
        myScreenshot.save('C:/-/screen.png') 
    
     #14 to search wikipedia for definition
    if there_exists(["definition of"]):
        definition=record_audio("what do you need the definition of")
        url=urllib.request.urlopen('https://www.wikipedia.org//'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                engine_speak('im sorry i could not find that definition, please try a web search')
            elif definitions[1]:
                engine_speak('here is what i found '+definitions[1])
            else:
                engine_speak ('Here is what i found '+definitions[2])
        else:
                engine_speak("im sorry i could not find the definition for "+definition)

     #15 PDF file search
    if there_exists(["pdf files","show PDF files"]):
        for root,dirs,files in os.walk('C:/'):
            for file in files:
                if file.endswith('.pdf'):
                    print(os.path.join(root,file))
                    engine_speak("Here is what i found")
    


     #16 PLAY music
    if there_exists(["play music","music"]):
        music_dir = r'C:\Users\Nik\Desktop\Believer.mp3'
        songs = os.startfile(music_dir)
        print(songs)
        engine_speak("Playing the song")
        os.startfile(os.path.join(music_dir, songs[0]))

     #17 Open Chrome
    if there_exists(["open chrome"]): 
            engine_speak("opening Google Chrome") 
            os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    
     #18 Open Word
    if there_exists(["open word"]): 
            engine_speak("opening microsoft word") 
            os.startfile(r"C:\Users\Nik\AppData\Local\Kingsoft\WPS Office\ksolaunch.exe")
     
     #19 Open Excel
    if there_exists(["open excel"]): 
            engine_speak("opening microsoft excel") 
            os.startfile(r"C:\Users\Nik\AppData\Local\Kingsoft\WPS Office\11.2.0.9150\office6\wps.exe")
     
     #20 Send Email
    if there_exists(["email to nikhil","Email"]):
            try:
                engine_speak("What should I say?")
                content = record_audio()
                to = "nikhilpatel.np508@gmail.com"    
                sendEmail(to, content)
                engine_speak("Email has been sent!")
            except Exception as e:
                print(e)
                engine_speak("Sorry my friend nik. I am not able to send this email")
     #21 latest news   
    if there_exists(["Latest News"]):
        search_term = voice_data.split("on")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")

     #22 WORD file search
    if there_exists(["word files","show word files"]):
        for root,dirs,files in os.walk('C:/'):
            for file in files:
                if file.endswith('.docx'):
                    print(os.path.join(root,file))
                    engine_speak("Here is what i found")

     #23 JPG file search
    if there_exists(["photo","show my photos "]):
        for root,dirs,files in os.walk('C:/'):
            for file in files:
                if file.endswith('.jpg','.png'):
                    print(os.path.join(root,file))
                    engine_speak("Here is what i found")

     #24 EXIT
    if there_exists(["exit", "quit", "goodbye"]):
        engine_speak("bye sir!!")
        exit()

     #25 WHO I AM
    if there_exists(['who are you']):
        engine_speak("I am SAM your Desktop assistant")


time.sleep(1)

person_obj = person()
sam_obj = sam()
sam_obj.name = 'SAM'
engine = pyttsx3.init()


while(1):
    voice_data = record_audio(" ") # get the voice input
    print("Done")
    print("Your query :", voice_data)
    respond(voice_data) # respond
