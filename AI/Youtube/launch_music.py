#%%
import json
import requests
from pytube import YouTube
import os
import subprocess
from playsound import playsound
from youtubesearchpython import VideosSearch



def Download(video_id):
    parent_dir = "sons/"
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"
    YouTube(youtube_url).streams.filter(file_extension = "mp4")[0].download(output_path=parent_dir)

    default_filename = YouTube(youtube_url).streams.filter(file_extension = "mp4")[0].default_filename  # get default name using pytube API

    '''subprocess.call([                              
        'ffmpeg',
        '-i', os.path.join(parent_dir, default_filename),
        os.path.join(parent_dir, "temp.mp3"),    
    ])'''    
    playsound(f"sons/{default_filename}")
    os.remove(f"sons/{default_filename}")

def youtube_api_v3():
    url = "https://youtube.googleapis.com/youtube/v3/search?"
    part="id"
    maxResults="1"
    q=input("Entrez le nom de la musique:\n")
    type_="video"
    key="AIzaSyC7HmJZ3AnZ40XX1HNPYqpGTbDIWKDCe8w"

    url+=f"&part={part}&maxResults={maxResults}&q={q}&type={type_}&key={key}"
    r = requests.get(url)

    if r.status_code == 200:
        #print(r.json())
        video_id = r.json()["items"][0]['id']["videoId"]
        Download(video_id)
        #playsound(f"sons/temp.mp3")
        #os(f"sons/temp.mp3")

    else:
        print("Erreur: " + r)

def youtube():
    q=input("Entrez le nom de la musique:\n")
    videosSearch = VideosSearch(q,limit=1,language='fr',region='FR')

    Download(videosSearch.result()['result'][0]['id'])
    

#youtube()
youtube_api_v3()
# %%


