import json
import requests
import datetime
from bs4 import BeautifulSoup

page = requests.get("https://www.republika.co.id")
obj = BeautifulSoup(page.text, 'html.parser')
current = datetime.datetime.now()

latest = {}
count = 0

a = open("result.json", "w")
a.close()

for terkini in obj.find_all('div', class_='teaser_conten1'):
    latest['category'] = terkini.find('p').text
    latest['title'] = terkini.find('h2').text
    latest['upload'] = terkini.find('div', class_='date').text
    latest['update'] = current.strftime('%I:%M:%S %p')
    with open("result.txt", "a") as json_file:
        json.dump(latest, json_file)
        json_file.write("\n")