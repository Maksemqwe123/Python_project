from bs4 import BeautifulSoup
import requests

url = f'https://kinogo.film/films-2021/'

response = requests.get(url=url)

pages_info = BeautifulSoup(response.text, 'html.parser')

films = pages_info.find_all('div', class_='shortstory')

data = []
kinogo_data = []

for film in films:
    urls = film.find('h2', class_='zagolovki').find('a').get('href')
    description = film.find('h2', class_='zagolovki').find('a').text

    data.append([urls])
    kinogo_data.append([description])
