'''
import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'item-name'}):
            href = "https://buckysroom.org" + link.get('href')
            title = link.string
            print(href)
            print(title)
        page += 1


trade_spider(1)
'''

import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        # url = 'https://thenewboston.com/search.php?type=0&sort=reputation&page==' + str(page)
        url = 'https://www.tehnomanija.rs/index.php?mod=catalog&op=browse&view=brand&brand_sef=lenovo&category_sef=&_html=&filters%5BRobna+marka%5D%5B0%5D=Lenovo&pg=' + str(
            page)
        source_code = requests.get(url, allow_redirects=False)
        # plain_text = source_code.text.encode('ascii', 'replace')
        plain_text = source_code.text.encode('utf-8', 'replace')
        soup = BeautifulSoup(plain_text, 'html.parser')
        # for link in soup.findAll('a', {'class': 'user-name'}):
        '''
        for link in soup.findAll('a', {'class': 'product-link'}):
            href = link.get('href')
            title = link.string
            print(title)
            print(href)
        '''
        for link in soup.findAll('img', {'class': 'js-add-to-basket-img'}):
            src = link.get('src')
            title = link.title
            print(title)
            print(src)
        page += 1


trade_spider(1)

