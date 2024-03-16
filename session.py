import requests
import os
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    links = []

    def handle_starttag(self, tag, attrs):
        if (tag != 'script'): return
        
        for attr in attrs:
            if (attr[0] == 'src'): 
                print(attr)
                self.links.append(attr[1])

dirPath = os.path.dirname(__file__)

responseDir = "parse"
responsePath = os.path.join(dirPath, responseDir)

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"

url = "https://ya.ru"
url = "https://www.sberbank.ru/proxy/services/rates/public/v2/history?rateType=PMR-3&isoCode=A98&date=1705611600000&regionId=070"
root_url = "https://www.sberbank.ru"

key = "russian_trusted_root_ca_pem.crt"
keyPath = os.path.join(dirPath, key)

session = requests.Session()

session.headers.update({'User-Agent': user_agent})
session.verify = keyPath

print("*" * 50)
response = session.get(url) # , verify=keyPath 

if (response.status_code != 200): 
    print("Load root error")
    exit()


filePath = os.path.join(responsePath, "root.html")
f = open(filePath, "w")
f.write(response.text)
f.close()

parser = MyHTMLParser()
parser.feed(response.text)
parser.close()

for link in parser.links:
    partName = link[-2:] + '.js'
    response = session.get(root_url + link)
    if response.status_code != 200:
            print("Load part", partName)
            exit()

    filePath = os.path.join(responsePath, partName)
    f = open(filePath, "w")
    f.write(response.text)
    f.close()


'''
print(response.status_code)
print("-" * 50)
print(response.headers)
print("-" * 50)
print(response.request.headers)
print(session.cookies.get_dict())
print(response.text)
'''