import requests
url = 'https://www.blagues-api.fr/api/type/dark/random'
headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTE3NzU1NTIyNjc4NjUyOTQ5IiwibGltaXQiOjEwMCwia2V5IjoiREYxaVlob0VGUUVoU2prdlM0YkR6SFd3SEdFWHhBM1BNV0VCWGF0RE4xTlJuRE0xSjUiLCJjcmVhdGVkX2F0IjoiMjAyMC0xMC0yOFQxNToyNzozMyswMTowMCIsImlhdCI6MTYwMzg5NTI1M30.VBLJ4COYLaTnXTm6EmxaqenPom_XHbsPSE0-dgw2-k0'}

r = requests.get(url, headers=headers)
j = r.json()["joke"]
a = r.json()["answer"]
print(j,a,sep=": ")