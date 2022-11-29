from bs4 import BeautifulSoup
import requests

url = f'https://litnet.com/ru/top/fentezi'

response = requests.get(url=url)

pages_info = BeautifulSoup(response.text, 'html.parser')

books = pages_info.find_all('div', class_='row book-item')
# print(books)

datas = []
litres_data = []

for book in books:
    urls = "https://litnet.com"+book.find('h4', class_='book-title').find('a').get('href')
    description = book.find('h4', class_='book-title').find('a').text

    datas.append([urls])
    litres_data.append([description])
    # print(urls)