import os
import requests
import time
from html.parser import HTMLParser
from urllib.parse import urljoin

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
        file_path = os.path.join(download_folder, main_name+".html")
        with open(file_path, "w") as f:
            f.write(response.text)
            files.append(file_path)
            
            parser = MyHTMLParser()
            parser.feed(response.text)
            parser.close()

            for link in parser.links:
                response = session.get(urljoin(url, link))
                if response.status_code != 200:
                    raise requests.ConnectionError(f'Expected status code 200, but got {format(response.status_code)}')
                
                script_name = main_name + '_' + link[-2:] + '.js'
                script_path = os.path.join(download_folder, script_name)
                with open(script_path, "w") as f:
                    f.write(response.text)
                    files.append(script_path)
    return files