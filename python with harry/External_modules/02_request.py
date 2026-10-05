import requests
r = requests.get('https://www.google.com')


with open("agro_mind.txt", "w", encoding="utf-8") as f:
    f.write(r.text)