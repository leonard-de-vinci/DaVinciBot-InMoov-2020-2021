# %% Import libraries
from google.cloud import texttospeech
from google.oauth2 import service_account
from playsound import playsound
import os
import time

dir_ = "/home/flavien/Documents/STT-TTS/"


#%%
import json
import requests
from pytube import YouTube
import os
import subprocess
from playsound import playsound



def Download(video_id):
    parent_dir = "sons/"
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"

    YouTube(youtube_url).streams.filter(file_extension = "mp4").all()[0].download(output_path=parent_dir)

    default_filename = YouTube(youtube_url).streams.filter(file_extension = "mp4").all()[0].default_filename  # get default name using pytube API

    '''subprocess.call([                              
        'ffmpeg',
        '-i', os.path.join(parent_dir, default_filename),
        os.path.join(parent_dir, "temp.mp3"),    
    ])''' 
    language_code = "fr"
    country_code = "FR"
    voice_gender = 0
    speaking_rate = 0.9
    pitch = 1.5

    gtts.set_parameters(speaking_rate=speaking_rate, pitch=pitch)
    val_nom = default_filename.replace('.mp4',"")
    gtts.synthetize(f"D'accord, je mets {val_nom}")   

    playsound(f"sons/{default_filename}")
    os.remove(f"sons/{default_filename}")

def Play_video(nom):
    url = "https://youtube.googleapis.com/youtube/v3/search?"
    part="id"
    maxResults="1"
    q=nom
    type_="video"
    key="AIzaSyC7HmJZ3AnZ40XX1HNPYqpGTbDIWKDCe8w"

    url+=f"&part={part}&maxResults={maxResults}&q={q}&type={type_}&key={key}"
    r = requests.get(url)

    if r.status_code == 200:
        video_id = r.json()["items"][0]['id']["videoId"]
        Download(video_id)
        #playsound(f"sons/temp.mp3")
        #os(f"sons/temp.mp3")

    else:
        print("Erreur: " + r)

#%% GoogleTTS
class GoogleTTS:
    """Class to interface with Google Translate’s text-to-speech API"""
    
    def __init__(self, ws_path="/home/flavien/Documents/TTS/audio_files/", credentials = service_account.Credentials.from_service_account_file('inmoovkey.json')):
        """Instantiates a client with the following parameters:
        - ws_path: path of the workspace directory (ex: /home/user/...)
        - credentials: credentials to use the google api"""
        self.client = texttospeech.TextToSpeechClient(credentials=credentials)
        self.ws_path = ws_path
        self.temp_path = ""

    def set_parameters(self, language_code="fr", country_code="FR" , voice_gender=0, voice_quality="w", format = "wav", pitch = 2.5, speaking_rate = 0.95, temp=True):
        """Synthesize a text into speech with the following parameters:
        - language code (ex: fr)
        - country code (ex: FR)
        - voice gender (0:male or 1:female)
        - voice quality (b:basic or w:wavenet)
        - format (wav or mp3)
        - pitch (double: [-20.0,20.0])
        - speaking_rate (double: [0.25, 4.0])
        - temp (if you want the file to be deleted once open)"""

        gender_nb = "B"
        gender = texttospeech.SsmlVoiceGender.MALE
        if voice_gender == 1:
            gender = texttospeech.SsmlVoiceGender.FEMALE
            gender_nb = "A"


        if voice_quality == "w":
            name = language_code.lower() + "-" + country_code.upper() + "-" + "Wavenet" + "-" + gender_nb
        else:
            name = language_code.lower() + "-" + country_code.upper() + "-" + "Standard" + "-" + gender_nb

        audio = texttospeech.AudioEncoding.LINEAR16
        if format == "mp3":
            audio = texttospeech.AudioEncoding.MP3

        self.voice = texttospeech.VoiceSelectionParams(
            language_code=language_code.lower()+"-"+country_code.upper(), name=name, ssml_gender=gender
        )
        self.audio_config = texttospeech.AudioConfig(
            audio_encoding=audio,
            effects_profile_id=["handset-class-device"],
            pitch = pitch,
            speaking_rate = speaking_rate
        )
        self.temp = temp

    def synthetize(self, text, name="temp", play = True, debug=False):
        """Synthesize a text into speech with the following parameters:
        - text: text to synthetize (ex: Hello World)
        - name: name of the file if not temp (ex: welcolme)
        - play: if you want to play the sound
        - debug: display the answer or not"""
        synthesis_input = texttospeech.SynthesisInput(text=text)
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=self.voice, audio_config=self.audio_config
        )
        self.temp_path = self.ws_path+name+"."+"wav"
        
        try:
            with open(self.temp_path, "wb") as out:
                out.write(response.audio_content)
            if debug:
                print(f'Audio content written to file {name}.mp3')
            if play:
                playsound(self.temp_path)
                if temp:
                    os.remove(self.temp_path)
        except  NameError:
            if debug:
                print("Le nom du fichier incorrect")
        except FileNotFoundError:
            if debug:
                print("Fichier introuvable")
        except :
            if debug:
                print(response)


#%%
gtts = GoogleTTS()
#%%
from googletrans import Translator
translator = Translator()
#text = translator.translate("Hello", dest="fr").extra_data['translation'][0][0]
#%%
'''
def translate(text, language_code):
    if language_code != "fr":
        text = translator.translate(text, dest=language_code).extra_data['translation'][0][0]
    return text
'''
def translate(text, language_code, text_language_code="fr"):
    url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl={text_language_code}&tl={language_code}&dt=t&q={text}'
    r = requests.get(url)
    return r.json()[0][0][0]
#%%
import json
import copy
import numpy as np

class api_infos():
    def __init__(self):
        self.name = 'api_keys.json'
        self.load_json_file()
        
    def load_json_file(self):
        self.data = {}
        try:
            with open(self.name,"r") as json_file:
                self.data = json.load(json_file)
        except IOError:
            self.save_api_infos()

    def add_api_infos(self,name,based_url,credentials,args,returned_args,sep_args,sep_arg_val,example): #keys doit être un dico
        self.data[name] = {"based_url":based_url,"credentials":credentials, "args":args,"returned_args":returned_args,"sep_args":sep_args,"sep_arg_val":sep_arg_val, "example":example}
        
    def save_api_infos(self):
        try:
            with open(self.name,'w') as json_file:
                json.dump(self.data,json_file,indent=4)
            return True
        except IOError:
            return False   

        
def example():
    api = api_infos()
    name = "News"
    based_url = "http://newsapi.org/v2/"
    keys = "d931f89016084e26aa8e0714ce06afbc"
    args = {"top-headlines?":{"args":["country","category","sources","q","page_size","page","apiKey"],"val":[["ae", "ar", "at", "au" ,"be", "bg", "br", "ca", "ch", "cn", "co", "cu", "cz", "de", "eg", "fr", "gb", "gr", "hk", "hu", "id", "ie", "il", "in", "it", "jp", "kr", "lt", "lv", "ma", "mx", "my", "ng", "nl", "no", "nz", "ph", "pl", "pt", "ro", "rs", "ru", "sa", "se", "sg", "si", "sk", "th", "tr", "tw", "ua", "us", "ve", "za"],["business", "entertainment", "general", "health", "science", "sports", "technology"],None,None,[i for i in range(100)],None,None],"Required":[-1]},
            "everything?":{"args":["q","qInTitle","sources","domains","excludeDomains","from","to","language","sortBy","pageSize","page","apiKey"],"val":[None,None,None,None,None,None,None,["ar","de","en","es","fr","he","it","nl","no","pt","ru","se","ud","zh"],["relevancy", "popularity", "publishedAt"],[i for i in range(100)],None,None],"Required":[-1]},
            "sources?":{"args":["category","language","country","apiKey"],"val":[["business", "entertainment", "general", "health", "science", "sports", "technology"],["ar","de","en","es","fr","he","it","nl","no","pt","ru","se","ud","zh"],["ae", "ar", "at", "au" ,"be", "bg", "br", "ca", "ch", "cn", "co", "cu", "cz", "de", "eg", "fr", "gb", "gr", "hk", "hu", "id", "ie", "il", "in", "it", "jp", "kr", "lt", "lv", "ma", "mx", "my", "ng", "nl", "no", "nz", "ph", "pl", "pt", "ro", "rs", "ru", "sa", "se", "sg", "si", "sk", "th", "tr", "tw", "ua", "us", "ve", "za"],None],"Required":[-1]}}
    returned_args = {"top-headlines?":["status","totalResults",{"articles":["source","author","title", "description","url","urlToImage","publishedAt","content"]}],
                     "everything":["status","totalResults",{"articles":["source","author","title", "description","url","urlToImage","publishedAt","content"]}],
                     "sources":["status",{"sources":["id","name","description", "url","category","language","country"]}]}
    sep_args = "&"
    sep_arg_val = "="
    example = "http://newsapi.org/v2/top-headlines?country=us&apiKey=d931f89016084e26aa8e0714ce06afbc"
    
    api.add_api_infos(name,based_url,keys,args,returned_args,sep_args,sep_arg_val,example)
    api.save_api_infos() 

import requests  

class Api():
    def __init__(self,name):
        self.api_infos = api_infos()
        self.data = self.api_infos.data[name]
        
        class_ = [x for x in self.data["args"]]
        
        self.args = copy.deepcopy(self.data["args"])
        for element in class_:
            del self.args[element]["val"]
        self.returned_args = self.data["returned_args"]        
        
    def request(self,type_,args_list_with_indices,args_values,return_args_desired):
        args = np.array(self.args[type_]["args"])[args_list_with_indices]
        sepa = self.data["sep_args"]
        sepv = self.data["sep_arg_val"]
        url = self.data["based_url"]+type_
        for arg,arg_value in zip(args,args_values):
            url+=arg+sepv+arg_value+sepa
        url+="apiKey"+sepv+self.data["credentials"]
        response = requests.get(url)
        print(response)
        result={}
        if response.status_code == 200:
            for element in return_args_desired:
                result[element]=response.json()[element] 
        else:
            print("Error")
        return result        

def top_news():
    api = Api("News")
    result = api.request("top-headlines?",[0,1,4],["fr","general","3"],["articles"])

    i = 0
    retour = {"title":[],"description":[]}
    while i < 3:
        retour["title"].append(result["articles"][i]["title"])
        retour["description"].append(result["articles"][i]["description"])
        #print(result["articles"][i]["publishedAt"])
        i+=1
    return retour

def lastest_news():
    api = Api("News")
    result = api.request("top-headlines?",[0,1,4],["fr","technology","3"],["articles"])

    i = 0
    retour = {"title":[],"description":[]}
    while i < 3:
        retour["title"].append(result["articles"][i]["title"])
        retour["description"].append(result["articles"][i]["description"])
        #print(result["articles"][i]["publishedAt"])
        i+=1
    return retour

def TopNews():
    retour = top_news()
    language_code = "fr"
    country_code = "FR"
    voice_gender = 0
    speaking_rate = 0.9
    pitch = 1.5

    gtts.set_parameters(speaking_rate=speaking_rate, pitch=pitch)
    gtts.synthetize("Voici les infos les plus en vogue aujourd'hui:")
    for title,description in zip(retour["title"],retour["description"]): 
        gtts.synthetize(title)
        gtts.synthetize(description)
        time.sleep(0.5)

def LastestNews():
    retour = lastest_news()
    language_code = "fr"
    country_code = "FR"
    voice_gender = 0
    speaking_rate = 0.9
    pitch = 1.5

    gtts.set_parameters(speaking_rate=speaking_rate, pitch=pitch)
    gtts.synthetize("Voici les dernière infos:")
    for title,description in zip(retour["title"],retour["description"]): 
        gtts.synthetize(title)
        gtts.synthetize(description)
        time.sleep(0.5)

#TopNews()
#LastestNews()
#%%
def Musique():
    language_code = "fr"
    country_code = "FR"
    voice_gender = 0
    speaking_rate = 0.9
    pitch = 1.5

    gtts.set_parameters(speaking_rate=speaking_rate, pitch=pitch)
    gtts.synthetize("Quel musique veux tu que je mettes ?")    
    name = Speech(recognizer, response)["transcription"]
    Play_video(name)
#%%
import requests
import time

def Blague():
    url = 'https://www.blagues-api.fr/api/type/blondes/random'
    url = 'https://www.blagues-api.fr/api/random?disallow=global&disallow=dev&disallow=dev'
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTE3NzU1NTIyNjc4NjUyOTQ5IiwibGltaXQiOjEwMCwia2V5IjoiREYxaVlob0VGUUVoU2prdlM0YkR6SFd3SEdFWHhBM1BNV0VCWGF0RE4xTlJuRE0xSjUiLCJjcmVhdGVkX2F0IjoiMjAyMC0xMC0yOFQxNToyNzozMyswMTowMCIsImlhdCI6MTYwMzg5NTI1M30.VBLJ4COYLaTnXTm6EmxaqenPom_XHbsPSE0-dgw2-k0'}

    language_code = "fr"
    country_code = "FR"
    voice_gender = 0
    speaking_rate = 0.9
    pitch = 1.5

    gtts.set_parameters(speaking_rate=speaking_rate, pitch=pitch)
    r = requests.get(url, headers=headers)
    j = r.json()["joke"]
    a = r.json()["answer"]

    gtts.synthetize(j) 
    time.sleep(1)
    gtts.synthetize(a) 

#Blague()
#%%
def Insult():
    url = 'https://evilinsult.com/generate_insult.php?lang=fr&type=json'
    r = requests.get(url)
    gtts.synthetize(f"Alexis {r.json()['insult']}") 
    
#Insult()
#%%
def Advice():
    url = 'https://api.adviceslip.com/advice'

    language_code = "en"
    country_code = "US"
    voice_gender = 0
    speaking_rate = 0.9
    pitch = 1.5

    gtts.set_parameters(language_code=language_code, country_code = country_code,speaking_rate=speaking_rate, pitch=pitch)
    r = requests.get(url)
    gtts.synthetize(r.json()["slip"]["advice"]) 

#Advice()
#%%
def Chucknorris():
    url = 'https://api.chucknorris.io/jokes/random'

    language_code = "en"
    country_code = "US"
    voice_gender = 0
    speaking_rate = 0.9
    pitch = 1.5

    gtts.set_parameters(language_code=language_code, country_code = country_code,speaking_rate=speaking_rate, pitch=pitch)
    r = requests.get(url, headers=headers)
    gtts.synthetize(r.json()["value"]) 

#%%
def Chucknorris():
    url = 'https://api.chucknorris.io/jokes/random'

    language_code = "en"
    country_code = "US"
    voice_gender = 0
    speaking_rate = 0.9
    pitch = 1.5

    gtts.set_parameters(language_code=language_code, country_code = country_code,speaking_rate=speaking_rate, pitch=pitch)
    r = requests.get(url, headers=headers)
    gtts.synthetize(r.json()["value"]) 

#Chucknorris()
#%%
import pycountry
import time

def MiniChat():
    language_code = "fr"
    country_code = "FR"
    voice_gender = 0
    speaking_rate = 0.9
    pitch = 1.5

    gtts.set_parameters(speaking_rate=speaking_rate, pitch=pitch)
    gtts.synthetize("Comment t'appelles-tu ?")    
    print("a")
    name = Speech(recognizer, response)["transcription"].lower()
    print("c")
    gtts.synthetize(f"Je suis ravi de te rencontrer {name}", language_code)
    gtts.synthetize(f"Quel âge as tu {name}?", language_code)
    age = Speech(recognizer, response)["transcription"].lower()
    gtts.synthetize(f"D'accord, donc tu as {age}", language_code)
    #gtts.synthetize(f"Bonjour, je m'appelle In moov. Parles tu français ?") 
    #rep = Speech(recognizer, response)["transcription"].lower()
    
    if rep != "oui":
        language_code = "en"
        country_code = "US"
        gtts.set_parameters(voice_gender=0, speaking_rate=0.9, pitch=1.5,language_code=language_code, country_code=country_code)
        gtts.synthetize(f"Alright, what language do you speak ?")
        language = Speech(recognizer, response,lang="en-US")["transcription"].lower()
        try:
            language_code = pycountry.languages.get(name=language).alpha_2
            gtts.synthetize(f"Where do you come from ?")
            country = Speech(recognizer, response,lang="en-US")["transcription"].lower()
            country_code = pycountry.countries.get(name=country).alpha_2
        except AttributeError:
            gtts.synthetize(f"I'm sorry, I didn't found your language, we will continue in english")  
            language_code = "en"
            country_code = "US"

        gtts.set_parameters(voice_gender=0, speaking_rate=0.9, pitch=1.5, 
        language_code=language_code, country_code=country_code)
        gtts.synthetize(translate("J'espère que tu me comprends mieux maintenant.", language_code))

    gtts.synthetize(translate("Comment t'appelles-tu ?", language_code))    
    name = Speech(recognizer, response)["transcription"].lower()
    gtts.synthetize(translate(f"Je suis ravi de te rencontrer {name}", language_code))
    gtts.synthetize(translate(f"Quel âge as tu {name}?", language_code))
    age = Speech(recognizer, response)["transcription"].lower()
    gtts.synthetize(translate(f"D'accord, donc tu as {age}", language_code))
    

#%%
import speech_recognition as sr
import pygame
pygame.mixer.init()

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300

def Speech(recognizer,response, lang="fr-FR"):
    with sr.Microphone() as microphone:
        recognizer.adjust_for_ambient_noise(microphone)
        try:
            audio = recognizer.listen(microphone)
            print("b")
            try:
                response["transcription"] = recognizer.recognize_google(audio, language = lang)
            except sr.RequestError:
                response["success"] = False
            except sr.UnknownValueError:
                response["success"] = False
        except sr.WaitTimeoutError:
            pass   
        print(response)
        return response


#%%
def IsEcoute(val):
    tab = val.split(" ")
    for element in tab:
        if element == "écoute":
            return True
    return False

def IsMusique(val):
    tab = val.split(" ")
    for element in tab:
        if element == "musique":
            return True
    return False 

def IsBlague(val):
    tab = val.split(" ")
    for element in tab:
        if element == "blague":
            return True
    return False 

# %%
pygame.mixer.music.load(f"{dir_}debut.wav")
pygame.mixer.music.play()

while True:
    response = {
    "success":True,
    "error":"",
    "transcription":""
    }
    response = Speech(recognizer,response)
    if response["success"] and IsEcoute(response["transcription"]): #response["transcription"] == "écoute":
        pygame.mixer.music.load(f"{dir_}notif.wav")
        pygame.mixer.music.play()
        MiniChat()
    elif response["success"] and IsMusique(response["transcription"]):
        pygame.mixer.music.load(f"{dir_}notif.wav")
        pygame.mixer.music.play()
        Musique()
    elif response["success"] and IsBlague(response["transcription"]):
        pygame.mixer.music.load(f"{dir_}notif.wav")
        pygame.mixer.music.play()
        Blague()
    elif response["success"] and response["transcription"] == "stop":
        pygame.mixer.music.load(f"{dir_}fin.wav")
        pygame.mixer.music.play()
        print("FIN")            
        break
# %%

