from bs4 import BeautifulSoup
import gzip
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
with open('sample.bytes', 'rb') as file:
    content = file.read()
    # dom = BeautifulSoup(gzip.decompress(content))
    data = gzip.decompress(content)
    soup = BeautifulSoup(data, 'html.parser')
    links = soup.find_all('a', {'class':'l _HId'})
    for link in links:
        print(link.get('href'))
    # print(soup.prettify())
