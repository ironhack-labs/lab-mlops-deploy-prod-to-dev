# the main library you will need for webscraping is called Beautiful Soup
from bs4 import BeautifulSoup

# the second package we will need we already know it
import requests


url = "https://en.wikipedia.org/wiki/Marie_Curie"

response = requests.get(url)
soup = BeautifulSoup(response.content)
tables = soup.find_all('table', attrs= {'class' : 'infobox biography vcard'})
for line in tables[0].find_all('th'):
  print(line.text)