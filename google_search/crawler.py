#!/usr/bin/env python3
import random
import gzip
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from .structures import SearchResults, SearchItem
import os


REQUEST_URL = "https://{}/{}"
BASE_URL = "www.google.co.uk"
GOOGLE_SEARCH = "search?hl=en&q={}"
SEARCH_NEWS = "&tbm=nws"
CUSTOMIZED_DATE = "&tbs=cdr:1,cd_min:{},cd_max:{}"
HTML_PARSER = 'html.parser'


def fetch_page(query):
    url = REQUEST_URL.format(BASE_URL, query)
    request = urllib.request.Request(url)
    request.add_header('User-agent', _random_user_agent())
    request.add_header('connection', 'keep-alive')
    request.add_header('Accept-Encoding', 'gzip, deflate, sdch, br')
    request.add_header('referer', REQUEST_URL.format(BASE_URL, ""))
    print(url)
    response = urllib.request.urlopen(request)

    data = response.read()
    print(type(data))
    return gzip.decompress(data)


def search_news(query, date_start=None, date_end=None):
    url = GOOGLE_SEARCH + SEARCH_NEWS
    url = url.format(_url_encode(query))

    if date_start is not None and date_end is not None:
        url += CUSTOMIZED_DATE.format(_url_encode_date(date_start), _url_encode_date(date_end))

    content = fetch_page(url)
    dom = BeautifulSoup(content, HTML_PARSER)
    search_result = SearchResults(query)
    links = dom.find_all('a', {'class': 'l _HId'})
    for link in links:
        search_result.append(SearchItem(link.text, link.get('href')))

    return search_result


def search_web(query, date_start=None, date_end=None):
    url = GOOGLE_SEARCH.format(_url_encode(query))

    if date_start is not None and date_end is not None:
        url += CUSTOMIZED_DATE.format(_url_encode_date(date_start), _url_encode_date(date_end))

    content = fetch_page(url)
    dom = BeautifulSoup(content, HTML_PARSER)
    print(dom.prettify())
    search_result = SearchResults(query)
    links = dom.find_all('h3', {'class':'r'})
    for link in links:
        search_result.append(SearchItem(link.a.text, link.a.get('href')))

    return search_result


def _url_encode(data):
    return urllib.parse.quote_plus(data)


def _url_encode_date(date):
    return _url_encode("{}/{}/{}".format(date.day, date.month, date.year))


def _random_user_agent():
    file_path = '{}/useragents'.format(os.path.dirname(__file__))
    with open(file_path, 'r') as file:
        user_agents = file.read().splitlines()
        line_num = len(user_agents)
        return user_agents[random.randrange(line_num)]


def write_to_local(content):
    with open("sample.html", "w") as text_file:
        text_file.write(content.decode())


def write_bytes(content):
    with open("sample.bytes", "wb") as text_file:
        text_file.write(content)
