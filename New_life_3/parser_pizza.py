from bs4 import BeautifulSoup
import requests

url = f'https://ym1.by/akczii/'

response = requests.get(url=url)

pages_info = BeautifulSoup(response.text, 'html.parser')

ref = pages_info.find('article', class_='akcii-i post-1011 akczii type-akczii status-publish has-post-thumbnail hentry').find('a').get('href')



# car_names = pages_info.find_all('a', class_='listing-item__link')
#         for name in car_names:
#             self.items.append(name.text)
#             self.urls.append(f"https://cars.av.by/bmw{name['href']}")