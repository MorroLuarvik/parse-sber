import os
import requests
import time
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    links = []

    def handle_starttag(self, tag, attrs):
        if tag != 'script': return

        for link in (val for attr, val in attrs if attr == 'src'):
            self.links.append(link)


DIR_PATH = os.path.dirname(__file__)

CERT = "russian_trusted_root_ca_pem.crt"
CART_PATH = os.path.join(DIR_PATH, CERT)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"


def load_files(url: str, download_folder: str) -> list:
    'Скачивает страницу и сохраняет указанные там js файлы'
    files = []
    with requests.Session() as session:
        session.headers.update({'User-Agent': USER_AGENT})
        session.verify = CART_PATH
        response = session.get(url)
        if response.status_code != 200: 
            raise requests.ConnectionError(f'Expected status code 200, but got {format(response.status_code)}')
        
        main_name = time.strftime('%Y.%m.%d_%H.%M.%S')
        file_name = os.path.join(download_folder, main_name+".html")
        with open(file_name, "w") as f:
            f.write(response.text)
            """
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
            """



