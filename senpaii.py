from PIL import Image
import requests   
filename = "8.jpg"
url = "https://media.discordapp.net/attachments/661736437552513024/851892606983602246/8.jpg"
headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get(url, allow_redirects=True, headers=headers)
im = Image.open("8.jpg")
with open(filename, 'wb') as f:
    for chunk in r.iter_content(1024):
        f.write(chunk)
im.show()