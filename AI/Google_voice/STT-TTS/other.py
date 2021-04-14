#%%
from pocketsphinx import LiveSpeech
#for phrase in LiveSpeech(): print(phrase)
#%%
from pocketsphinx import LiveSpeech

#speech = LiveSpeech(lm=False, keyphrase='forward', kws_threshold=1e-20)
#for phrase in speech:
    #print(phrase.segments(detailed=True))
#%%s
import speech_recognition as sr
recognizer = sr.Recognizer()

#%%
response = {
    "success":True,
    "error":"",
    "transcription":""
}

recognizer = sr.Recognizer()
i=0
while(i<4):
    with sr.Microphone() as microphone:
        recognizer.adjust_for_ambient_noise(microphone)
        try:
            audio = recognizer.listen(microphone)
            try:
                response["transcription"] = recognizer.recognize_google(audio)
            except sr.RequestError:
                response["success"] = False
            except sr.UnknownValueError:
                response["success"] = False
        except sr.WaitTimeoutError:
            pass   
        print(response)
    i+=1
#%%
import googletrans
#%%
from googletrans import Translator
translator = Translator()
translator.translate('안녕하세요.')