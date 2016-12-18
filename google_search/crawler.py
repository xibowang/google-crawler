#!/usr/bin/env python3
import gzip
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from .structures import SearchResults, SearchItem


REQUEST_URL = "https://{}/{}"
BASE_URL = "www.google.co.uk"
GOOGLE_SEARCH = "search?hl=en&q={}"
SEARCH_NEWS = "&tbm=nws"
CUSTOMIZED_DATE = "&tbs=cdr:1,cd_min:{},cd_max:{}"
HTML_PARSER = 'html.parser'
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"


def fetch_page(query):
    url = REQUEST_URL.format(BASE_URL, query)
    request = urllib.request.Request(url)
    request.add_header('User-agent', USER_AGENT)
    request.add_header('connection','keep-alive')
    request.add_header('Accept-Encoding', 'gzip, deflate, sdch, br')
    request.add_header('referer', REQUEST_URL.format(BASE_URL, ""))
    print(url)
    response = urllib.request.urlopen(request)

    data = response.read()
    print(type(data))
    return gzip.decompress(data)


def url_encode(data):
    return urllib.parse.quote_plus(data)


def search_news(query, date_start=None, date_end=None):
    url = GOOGLE_SEARCH + SEARCH_NEWS
    url = url.format(url_encode(query))

    if date_start is not None and date_end is not None:
        url += CUSTOMIZED_DATE.format(url_encode_date(date_start), url_encode_date(date_end))

    content = fetch_page(url)
    dom = BeautifulSoup(content, HTML_PARSER)
    print(dom.prettify())
    search_result = SearchResults(query)
    links = dom.find_all('a', {'class':'l _HId'})
    for link in links:
        search_result.append(SearchItem(link.text, link.get('href')))

    return search_result


def search_web(query, date_start=None, date_end=None):
    url = GOOGLE_SEARCH.format(url_encode(query))

    if date_start is not None and date_end is not None:
        url += CUSTOMIZED_DATE.format(url_encode_date(date_start), url_encode_date(date_end))

    content = fetch_page(url)
    dom = BeautifulSoup(content, HTML_PARSER)
    print(dom.prettify())
    search_result = SearchResults(query)
    links = dom.find_all('h3', {'class':'r'})
    for link in links:
        search_result.append(SearchItem(link.a.text, link.a.get('href')))

    return search_result


def url_encode_date(date):
    return url_encode("{}/{}/{}".format(date.day, date.month, date.year))


def write_to_local(content):
    with open("sample.html", "w") as text_file:
        text_file.write(content.decode())


def write_bytes(bytes):
    with open("sample.bytes", "wb") as text_file:
        text_file.write(bytes)
