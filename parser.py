import requests
from bs4 import BeautifulSoup
url = 'https://stopgame.ru'
responce = requests.get(url)
print(responce.status_code)
print(responce.text)

Soup = BeautifulSoup(responce.text, 'html.parser')
print(Soup.title)
print(type(Soup.title))

print(Soup.a)
print(Soup.a.string)

print(Soup.a.get('href'))

image_tags = Soup.find_all('img')
for image_tags in image_tags:
    print(image_tags)

    a_tags = Soup.find_all('a')
    for a_tags in a_tags:
        print(a_tags)

big_body_div = Soup.find( 'div', class_ = 'modulebody1')

print(big_body_div)