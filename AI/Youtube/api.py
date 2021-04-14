#%%
import json
import requests
#%%
url = "https://youtube.googleapis.com/youtube/v3/search?"
part="id"
maxResults="1"
q="sambadobrazil"
key="AIzaSyC7HmJZ3AnZ40XX1HNPYqpGTbDIWKDCe8w"

url+=f"&part={part}&maxResults={maxResults}&q={q}&key={key}"

#%%
r = requests.get(url)

#%%
if r.status_code == 200:
    video_id = r.json()["items"][0]['id']["videoId"]
    print(video_id)

else:
    print("Erreur: " + r)

# %%
from pytube import YouTube
import os
import subprocess

parent_dir = "sons/"
youtube_url = f"https://www.youtube.com/watch?v={video_id}"

YouTube(youtube_url).streams.filter(file_extension = "mp4").all()[0].download(output_path=parent_dir)
# %%
default_filename = YouTube(youtube_url).streams.filter(file_extension = "mp4").all()[0].default_filename  # get default name using pytube API

subprocess.call([                              
    'ffmpeg',
    '-i', os.path.join(parent_dir, default_filename),
    os.path.join(parent_dir, "temp.mp3"),    
])

os.remove(f"sons/{default_filename}")
# %%
