import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import requests
import json
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("  hello iqbal iam jarvis sir how may i help you")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...........")
        r.pause_threshold=1
        audio=r.listen(source) 
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("say it again.....")
        return "None"
    return query
if __name__=="__main__":
    wishme()
    while True:
        query1= takecommand()
        sites=[["youtube","https://youtube.com"],["wikipedia","https://wikipedia.com"],["google","https://google.com"],["amazon:","https://amazon.com"],["instagram","https://instagram.com"],["stack overflow","https://stackoverflow.com"]]
        for site in sites:
            if f"open {site[0]} ".lower() in query1.lower():
                 speak(f"opening {site[0]} sir....")
                 webbrowser.open(site[1])
        if(query1=="stop"):
            speak("ok iam stopping opening websites iqbal")
            speak("Now what do you want?")
            break
    query=takecommand()
    query="today's news"
    speak("what type of news do you want to hear :")

    # if (query2 in ):
    #         print("ok sir im finding")
    url="https://newsapi.org/v2/everything?q=tesla&from=2024-05-17&sortBy=publishedAt&apiKey=API_KEY"
    r=requests.get(url)
    news=json.loads(r.text)
    for article in news["articles"]:
        print(article['title'])
        print(article['description'])
        speak(article['title'])
        speak(article['description'])
    

        
        
        








