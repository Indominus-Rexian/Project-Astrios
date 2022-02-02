from ast import In
from googlesearch import search
from selenium import webdriver
from PyDictionary import PyDictionary
import pytube
from youtubesearchpython import VideosSearch

class Internet():
    def __init__(self) -> None:
        self.loc = None

    def InternetOpener(self, query:str):
        for x in search(query, stop=5):
            url = x
        opts = webdriver.ChromeOptions()
        opts.add_argument("--no-sandbox");
        opts.add_argument("--disable-dev-shm-usage");
        opts.add_experimental_option("detach", True);
        opts.add_argument("--disable-gpu")        
        browser = webdriver.Chrome(options=opts)
        browser.get(url)

    def Youtube(self, query:str):
        video_search = VideosSearch(query, limit=1)
        results = video_search.result()
        yt_link = results['result'][0]['link']
        self.yt_id = results['result'][0]['id']
        yt = pytube.YouTube(url=yt_link)
        try:
            stream = yt.streams.get_highest_resolution()
            self.loc = stream.download('cdn')
        except Exception as e:
            stream = yt.streams.first()
            self.loc = stream.download('cdn')  

    def GetMeaning(self, query:str):
        dictionary=PyDictionary()
        self.meaning = dictionary.meaning(query)

    def GetAntonym(self, query:str):
        dictionary=PyDictionary()
        self.antonym = dictionary.antonym(query)        

    def GetSynonym(self, query:str):
        dictionary=PyDictionary()
        self.synonym = dictionary.synonym(query)            
