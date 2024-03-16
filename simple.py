import requests
import os
import time

url = "https://www.sberbank.ru/ru/person"
url = "https://sberbank.ru"
url = "https://ya.ru"


r = requests.get(url)

print("=" * 50)
print(r.status_code)
print("-" * 50)
print(r.headers)
print("-" * 50)
print(r.cookies.get_dict())


print("=" * 50)
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    links = []

    def handle_starttag(self, tag, attrs):
        if tag != 'script': return
        #if not len(attrs): return

        for link in (val for attr, val in attrs if attr == 'src'):
            self.links.append(link)

        '''
        links = self.links
        map(lambda val: links.append(val), [val for attr, val in attrs if attr == 'src'])
        print(attrs)

        for attr in attrs:
            if attr[0] == 'src': 
                print(attr)
                self.links.append(attr[1])
        '''

parser = MyHTMLParser()
parser.feed(r.text)
parser.close()
print(parser.links)