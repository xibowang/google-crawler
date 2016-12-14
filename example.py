#!/usr/bin/env python3
import gzip
import urllib.request
import urllib.parse
import zlib
import datetime
from bs4 import BeautifulSoup


REQUEST_URL = "https://{}/{}"
BASE_URL = "www.google.co.uk"
GOOGLE_NEWS_QUERY = "search?hl=en&q={}&tbm=nws"
GOOGLE_NEWS_URL_CUSTIME_DATE_QUERY = "search?hl=en&q={}&tbm=nws&tbs=cdr:1,cd_min:{},cd_max:{}"
CHARSET = "ISO-8859-1"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
PARSER = "html.parser"

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
    # print(data.decode(CHARSET))
    # decompressed = gzip.decompress(data=data)
    # decompressed = zlib.decompress(bytes(data), 16 + zlib.MAX_WBITS)
    return data


def url_encode(data):
    return urllib.parse.quote_plus(data)


def search(query, date_start=None, date_end=None):

    if date_start is not None and date_end is not None:
        url = GOOGLE_NEWS_URL_CUSTIME_DATE_QUERY.format(url_encode(query), url_encode_date(dt_start), url_encode_date(date_end))
    else:
        url = GOOGLE_NEWS_QUERY.format(url_encode(query))
    print(url)
    return fetch_page(url)


def write_to_local(content):
    with open("example.html", "w") as text_file:
        text_file.write(str(content))


def write_bytes(bytes):
    with open("sample.bytes", "wb") as text_file:
        text_file.write(bytes)


def url_encode_date(date):
    return url_encode("{}/{}/{}".format(date.day, date.month, date.year))


if __name__ == '__main__':
    search_query = "united kingdom"
    search_url = GOOGLE_NEWS_QUERY.format(url_encode(search_query))
    dt_start = datetime.date(2016, 2, 3)
    dt_end = datetime.date(2016, 2, 3)
    html_content = search(search_query, dt_start, dt_end)
    write_bytes(html_content)
    # dom = BeautifulSoup(html_content)
    # print(dom)
    # page = fetch_page(search_url)

