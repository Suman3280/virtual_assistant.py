#functionlly
import pyttsx3
import sqlite3
import speech_recognition as sr
import datetime
import os
from requests import get
import wikipedia
import time
import pyjokes  
import datetime
import json
import newsapi
import PyPDF2
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import webbrowser
import pywhatkit
import urllib 
import sys
from tkinter import *
import threading
from PIL import Image, ImageTk


sleep_zera = 1



def is_internet():
    speak("checking internet connection")
    print("checking internet connection")
    time.sleep(1)
    speak("internet is connected we are  online how may i help you")
    print("internet is connected")
    try:
        checkIN = urllib.request.urlopen("https://www.google.com",timeout=1)

    
    except Exception as e:
        speak("internt is not connected pls make sure internet conncted")    

def search():
    speak("what do want to search")
    mysearch =takecommand()
    
    pywhatkit.search(mysearch)
    return
    




#createing data base for storing diloug for assistant and storing file path 
def openfiles():
    all_files = json.load(open("path.json"))
    speak("which file")
    filename= str (takecommand()).lower()
    if filename in all_files.keys():
        speak("opening file")
        os.startfile(all_files[filename])
        return
def news():
    my_news= newsapi.NewsApiClient("56dc8aa50892475eaba5bb26261bd912")
    my_news= my_news.get_top_headlines()
    articals = my_news["articles"]
    head=[]
    day=["first","second","third", "forth" ,"fift","sixth","seventh,"]
    
    for ar in articals:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"todays {day[i]} news is {head[i]}")



    

#some  settings for audio

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    print(" hollo i am zera")
    graphic_terminal.insert(END, F"hello i am zera\n")
    hour = datetime.datetime.now().hour
    if hour > 0 and hour <12:
        speak("good morning")
    else:
        speak("good evening")
       
    
    speak("hello my name is zera your virtual assistant")
    speak(f"the time is {datetime.datetime.now()}")
    print(datetime.datetime.now().time()) 


             
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as surcoe:
        print("listening...")
        graphic_terminal.insert(END,"listining...\n" )
        r.pause_threshold=1
        global sleep_zera
        
        
        try:
            audio = r.listen(surcoe,timeout=10,phrase_time_limit=5)
            print("recongnizing...")
            graphic_terminal.insert(END, "recongnizing...\n")
            quary = r.recognize_google(audio,language="en-in")
            print(f"user said {quary}")
            graphic_terminal.insert(END, f"user said : {quary}\n")
            return quary
        except Exception as e:
            
            if sleep_zera == 0 :
                speak("say that again")
                


def read_pdf():

    speak("give me full path of pdf file")
    pdf_path =  input("Enter path:")
    pdf_file=open(pdf_path,"rb")
    pdfREader = PyPDF2.PdfFileReader(pdf_file)
    pdf_pages = pdfREader.numPages
    speak(f"this pdf has {pdf_pages} pages")
    speak("enter the page number :")
    pe = int(input("Enter page number"))
    pdf_pagenum = pdfREader.getPage(pe)
    text= pdf_pagenum.extractText()
    print(text)
    graphic_terminal.insert(END, str(text))
    speak(text)


def temprature():
    
    
    url = "https://www.google.com/search?q=tempratare+in+delhi&rlz=1C1CHBD_enIN980IN980&oq=tempratare+in+delhi&aqs=chrome..69i57j33i160.43381j1j15&sourceid=chrome&ie=UTF-8"
    
    r=get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp=data.find("div", class_="BNeawe").text
    speak(f"tempuratre in city is {temp}")
    graphic_terminal.insert(END, str(temp))
    print(temp)

def how_to_do():
    speak("what you want to search")
    search = takecommand()
    data = search_wikihow(search,1)
    data[0].print()
    graphic_terminal.insert(END,str(data[0].print) )
    speak(data[0].summary)
    speak("thanks")
    
def music_vidieo():
    
    speak("what to search for ?")
    myq = takecommand()
    speak("searching online..")
    pywhatkit.playonyt(myq)
    
            


     








def peformtask():
    while True:
        my_command= takecommand()
        my_command= str(my_command).lower()
        
        #open system file
        if "open notepad" in my_command:
            os.startfile("C:\\Windows\\system32\\notepad.exe")
        if "exit" in my_command :
            break
        if "ip address"in my_command:
            ip=get("https://api.ipify.org").text
            speak(f"your ip address is {ip} ")
        #wikipidia search
        if "wikipedia" in my_command:
            try:
                speak("serching online")
                my_command= my_command.replace("wikipedia","")
                result = wikipedia.summary(my_command, sentences=2)
                speak("here is some result")
                print(result)
                graphic_terminal.insert(END, str(result))
                speak(result)
            except Exception as e:
                speak("can't able to search try again")    
        
        if "open file" in my_command:
            openfiles()
        if "news" in my_command:
            news()
        if "music" in my_command:
            music_vidieo()   
        if "sleep" in my_command:
            global sleep_zera
            sleep_zera = 1
            speak("i am going to sleep you can call me any time by saying wake up")
            break
        if "joke" in my_command:
            joke =  pyjokes.get_joke()
            speak(joke)
            print(joke)
        if "read pdf" in my_command:
            read_pdf()
        if "temperature" in my_command:
            temprature()
        if "how to do"in my_command:
            how_to_do()

        if "search" in my_command:
            search()
        if "restart" in my_command:
            speak("do you want to restart computer ? ")
            restartcheck= str(takecommand()).lower()
            if "yes" in restartcheck:
                os.system("shutdown /r /t 30")
                speak("restaring in 30 seconds")
                print("restarting in 30 secs...")
                sys.exit()
            else:
                speak("sure")
                continue
        if "shutdown" in my_command:
            speak("do you want  to shutdown computer ? ")
            restartcheck= str(takecommand()).lower()
            if "yes" in restartcheck:
                os.system("shutdown /s /t 30")
                speak("shutdown in 30 seconds")
                print("restarting in 30 seconds")
                sys.exit()
            else:
                speak("sure")
                continue        
                
          
def zera_backend():
    wish()
    is_internet()
    while True:

        statzera= str(takecommand()).lower()
        if "wake up" in statzera:
            sleep_zera = 0
            speak("i am at your service how may help you")
            peformtask()
        elif "shutdown" in statzera:
            speak("thanks for using me have a nice day")
            break





#zera gui
zera_window = Tk()
zera_window.geometry("500x500")

bg = PhotoImage(file = "b.png")
background_lebal=Label(image=bg)
background_lebal.place(x=0,y=0,relwidth=1)
graphic_terminal = Text(width=40,height=10,background="black", foreground="White")
#graphic_terminal.insert(END, "hritik")
graphic_terminal.pack(side="bottom")
date_time=Text(background="black", foreground="White",height=4,width=20)
date_time.pack(side="top",anchor="nw")
date_time.insert(END,f"Date - { datetime. datetime.today().strftime('%Y-%m-%d')}\n" )
date_time.insert(END, "      WELCOME")
zera_window.title('zera vitual assistant')
t1= threading.Thread(target=zera_backend)


t1.start()

zera_window.mainloop()
    

