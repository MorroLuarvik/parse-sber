import requests
from requests.adapters import HTTPAdapter, Retry
import os

dirPath = os.path.dirname(__file__)

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"

url = "https://ya.ru"
url = "https://www.sberbank.ru/proxy/services/rates/public/v2/history?rateType=PMR-3&isoCode=A98&date=1705611600000&regionId=070"

key = "russian_trusted_sub_ca_pem.crt"
key = "cert22.pem"
key = "russian_trusted_root_ca_pem.crt"
key = "russiantrustedca.pem"

keyPath = os.path.join(dirPath, key)

session = requests.Session()

session.headers.update({'User-Agent': user_agent})
session.verify = keyPath

print("*" * 50)
response = session.get(url) # , verify=keyPath 

print(response.status_code)
print("-" * 50)
print(response.headers)
print("-" * 50)
print(response.request.headers)
print(session.cookies.get_dict())
print(response.text)


'''
print("*" * 50)
response = session.get(url) # , verify=keyPath 

print(response.status_code)
print("-" * 50)
print(response.headers)
print("-" * 50)
print(response.request.headers)
print(session.cookies.get_dict())
print(response.text)
'''