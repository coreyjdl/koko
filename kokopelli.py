#!/usr/local/bin/python3
import requests, datetime, re
from bs4 import BeautifulSoup

url = "http://www.kokapellideli.com/Lunch.html"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

today = datetime.datetime.today().strftime("%A")

results = []
for elem in soup.find_all('font'):
  text = ''.join(char for char in elem.text if ord(char) < 128)
  if (text):
    results.append(text)

index_of_today = results.index(today)

with open('koko', 'w') as file:
  for item in results[index_of_today: index_of_today + 4]:
    file.write(f"{item}<br />")

