import requests
from bs4 import BeautifulSoup

url='http://www.airindia.in/board-of-directors.htm'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.text)