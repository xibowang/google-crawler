#!/usr/bin/env python3
import gzip
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from .structures import SearchResults, SearchItem


REQUEST_URL = "https://{}/{}"
BASE_URL = "www.google.co.uk"
GOOGLE_NEWS_QUERY = "search?hl=en&q={}&tbm=nws"
GOOGLE_NEWS_URL_CUSTIME_DATE_QUERY = "search?hl=en&q={}&tbm=nws&tbs=cdr:1,cd_min:{},cd_max:{}"
CHARSET = "ISO-8859-1"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
HTML_PARSER = 'html.parser'


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


def search(query, date_start=None, date_end=None):

    if date_start is not None and date_end is not None:
        url = GOOGLE_NEWS_URL_CUSTIME_DATE_QUERY.format(url_encode(query), url_encode_date(dt_start), url_encode_date(date_end))
    else:
        url = GOOGLE_NEWS_QUERY.format(url_encode(query))

    content = fetch_page(url)

    dom = BeautifulSoup(content, HTML_PARSER)
    search_result = SearchResults(query)
    links = dom.find_all('a', {'class':'l _HId'})
    for link in links:
        search_result.append(SearchItem(link.text, link.get('href')))

    return search_result


def url_encode_date(date):
    return url_encode("{}/{}/{}".format(date.day, date.month, date.year))


def write_to_local(content):
    with open("sample.html", "w") as text_file:
        text_file.write(content.decode())


def write_bytes(bytes):
    with open("sample.bytes", "wb") as text_file:
        text_file.write(bytes)
