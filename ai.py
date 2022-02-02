import sys
import time
import requests
from threading import Thread
from colorama import Fore
import speech_recognition as sr
import pyttsx3
from src.tker import Tker
from src.internet import Internet

internet = Internet()
engine = pyttsx3.init()
recognizer = sr.Recognizer()

newVoiceRate = 135
engine.setProperty('rate',newVoiceRate)

def listener():
    print('Say!')
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)   
                text = text.lower()
                try:
                    text = text.replace('astros','')
                except:
                    text = text.replace('astrios','')  

                print(Fore.GREEN+"User:"+text) 
                
                if 'search google' in text:
                    query = text.split('search google')[-1]
                    engine.say('Searching Google for'+query)
                    print(Fore.LIGHTWHITE_EX+'Astrios: Searching Google for'+query)
                    engine.runAndWait()
                    engine.stop()
                    open_int = Thread(target=internet.InternetOpener, args=(query,))
                    open_int.start()
                    open_int.join()

                elif 'search youtube for' in text or 'search on youtube' in text:
                    try:
                        query = text.split('search youtube for')[-1]
                        engine.say('Opening video for'+query)
                        print(Fore.LIGHTWHITE_EX+'Astrios: Opening video for'+query)
                        engine.runAndWait()
                        engine.stop()                        
                        internet.Youtube(query)
                    except:
                        query = text.split('search on youtube')[-1]
                        engine.say('Opening video for'+query)
                        print(Fore.LIGHTWHITE_EX+'Astrios: Opening video for'+query)
                        engine.runAndWait()
                        engine.stop()                        
                        internet.Youtube(query)

                    tker = Tker()
                    tker.Player(loc=internet.loc)
                    
                if 'close' == text or 'shutdown' == text:
                    engine.say('Okay then! Closing myself!')
                    print(Fore.YELLOW+"Astrios:Okay then! Closing myself!")
                    engine.runAndWait()
                    engine.stop()
                    time.sleep(3)
                    sys.exit()
                else:
                    url = f'http://api.brainshop.ai/get?bid=158354&key=JjfNethGc6x46w9R&uid=none&msg={text}'    
                    r = requests.get(url)
                    json = r.json()   
                    text = json['cnt']   
                    print(Fore.CYAN+'Astrios:'+text)
                    engine.say(text)
                    engine.runAndWait()
                    engine.stop()
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(Fore.RED+f"Google error{e}")

if __name__ == '__main__':
    listener()
