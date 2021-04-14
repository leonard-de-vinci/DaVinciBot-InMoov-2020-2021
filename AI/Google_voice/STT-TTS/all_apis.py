#%%
import requests
import time
#%%
def Insult():
    url = 'https://evilinsult.com/generate_insult.php?lang=fr&type=json'
    r = requests.get(url, headers=headers)
    print(r.json())
Insult()

#%%
def I():
    url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTE3NzU1NTIyNjc4NjUyOTQ5IiwibGltaXQiOjEwMCwia2V5IjoiREYxaVlob0VGUUVoU2prdlM0YkR6SFd3SEdFWHhBM1BNV0VCWGF0RE4xTlJuRE0xSjUiLCJjcmVhdGVkX2F0IjoiMjAyMC0xMC0yOFQxNToyNzozMyswMTowMCIsImlhdCI6MTYwMzg5NTI1M30.VBLJ4COYLaTnXTm6EmxaqenPom_XHbsPSE0-dgw2-k0'}

    r = requests.get(url, headers=headers)
    print(r.json())

