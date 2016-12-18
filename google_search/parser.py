#!/usr/bin/env python3
from bs4 import BeautifulSoup
import gzip
import sys
import io


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

HTML_PARSER = 'html.parser'


def read_bytes_data():
    with open('sample.bytes', 'rb') as file:
        content = file.read()
        # dom = BeautifulSoup(gzip.decompress(content))
        data = gzip.decompress(content)
        # soup = BeautifulSoup(data, 'html.parser')
        # links = soup.find_all('a', {'class':'l _HId'})
        # for link in links:
        #     print(link.get('href'))
        # print(soup.prettify())


def read_html_data():
    with open('sample.html', 'r') as file:
        print('start reading html')
        content = file.read()
        dom = BeautifulSoup(content, HTML_PARSER)
        links = dom.find_all('a', {'class':'l _HId'})
        for link in links:
            print(link.text)
            print(link.get('href'))
        # print(dom.prettify())


if __name__ == '__main__':
    read_html_data()
