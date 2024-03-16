import requests
import os
import time
from urllib.parse import urlparse, urljoin, urlunsplit

url = "https://www.sberbank.ru/proxy/services/rates/public/v2/history?rateType=PMR-3&isoCode=A98&date=1705611600000&regionId=070"

#scheme, host, *_ = 
#up = urlparse(url)

#print(up)

#nur = 

print(urljoin(url, 'kek'))