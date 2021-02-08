import bs4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


news_url = 'https://news.google.com/news/'
source_code = requests.get(news_url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text)

for link in soup.findAll('a', {'class': 'VDXfz'}):
    href = link.get('href')
    for news_links in soup.findAll('h3', {'class': 'ipQwMb ekueJc RD0gLb'}):
        body = news_links.find('a', {'class': 'DY5T1d'})
        title = body.string
        print('https://news.google.com/news/' + href)
        print(title)
