import speech_recognition as sr
import pygame
pygame.mixer.init()

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300

def Speech(recognizer,microphone, response):
    try:
        audio = recognizer.listen(microphone,timeout=0.5)
        try:
            response["transcription"] = recognizer.recognize_google(audio, language = "fr-FR")
        except sr.RequestError:
            response["success"] = False
        except sr.UnknownValueError:
            response["success"] = False
    except sr.WaitTimeoutError:
        pass   
    
    return response


pygame.mixer.music.load("debut.wav")
pygame.mixer.music.play()
with sr.Microphone() as microphone:
    recognizer.adjust_for_ambient_noise(microphone)

    while True:
        response = {
        "success":True,
        "error":"",
        "transcription":""
        }

        response = Speech(recognizer,microphone, response)
        if response["success"] and response["transcription"] == "écoute":
            pygame.mixer.music.load("notif.mp3")
            pygame.mixer.music.play()
            print("Comment puis-je vous aider ?")
            response = Speech(recognizer,microphone, response)
            print(response["transcription"])
        elif response["success"] and response["transcription"] == "stop":
            pygame.mixer.music.load("fin.mp3")
            pygame.mixer.music.play()
            print("FIN")            
            break


