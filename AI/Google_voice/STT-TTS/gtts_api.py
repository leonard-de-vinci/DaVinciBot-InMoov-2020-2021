# %% Import libraries
from google.cloud import texttospeech
from google.oauth2 import service_account
from playsound import playsound
import os
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


#%% Launch at the beginning
gtts = GoogleTTS()
#%%
from googletrans import Translator
translator = Translator()

def translate(text, language_code):
    if language_code != "fr":
        text = translator.translate(text, dest=language_code).extra_data['translation'][0][0]
    return text

#%%
import pycountry

language_code = "fr"
country_code = "FR"
voice_gender = 0
speaking_rate = 0.9
pitch = 1.5

gtts.set_parameters(speaking_rate=speaking_rate, pitch=pitch)
gtts.synthetize(f"Bonjour, je m'appelle In moov. Parles tu français ?")
rep = input()
if rep != "oui":
    language_code = "en"
    country_code = "US"
    gtts.set_parameters(voice_gender=0, speaking_rate=0.9, pitch=1.5,language_code=language_code, country_code=country_code)
    gtts.synthetize(f"Alright, what language do you speak ?")
    language = input()
    try:
        language_code = pycountry.languages.get(name=language).alpha_2
        gtts.synthetize(f"Where do you come from ?")
        country = input()
        country_code = pycountry.countries.get(name=country).alpha_2
    except AttributeError:
        gtts.synthetize(f"I'm sorry, I didn't found your language, we will continue in english")  

    gtts.set_parameters(voice_gender=0, speaking_rate=0.9, pitch=1.5, 
    language_code=language_code, country_code=country_code)
    gtts.synthetize(translate("J'espère que tu me comprends mieux maintenant.", language_code))
    

gtts.synthetize(translate("Comment t'appelles-tu ?", language_code))
name = input()
gtts.synthetize(translate(f"Je suis ravi de te rencontrer {name}", language_code))
gtts.synthetize(translate(f"Quel âge as tu {name}?", language_code))
age = input()
gtts.synthetize(translate(f"D'accord, donc tu as {age} ans", language_code))


# %%
gtts.set_parameters(language_code="en",format="wav", country_code="US",speaking_rate=speaking_rate, pitch=pitch, temp=False)
gtts.synthetize(f'Hi, how are you !',name="audio")

#%%
