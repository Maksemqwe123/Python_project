from bs4 import BeautifulSoup
import requests

url = f'https://www.russianfood.com/recipes/bytype/?fid=45'

response = requests.get(url=url)

pages_info = BeautifulSoup(response.text, 'html.parser')

cooks = pages_info.find_all('div', class_='recipe_l in_seen v2')

data_1 = []
cook_data_1 = []

for cook in cooks:
    urls = "https://www.russianfood.com"+cook.find('div', class_='title').find('a').get('href')
    description = cook.find('div', class_='title').find('a').text

    data_1.append([urls])
    cook_data_1.append([description])
