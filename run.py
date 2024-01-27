import requests
import os

dirPath = os.path.dirname(__file__)

url = "https://ya.ru"
url = "https://www.sberbank.ru/ru/person"
url = "https://www.sberbank.ru/proxy/services/rates/public/v2/history?rateType=PMR-3&isoCode=A98&date=1705611600000&regionId=070"
url = "https://sberbank.ru"
#url = "https://www.sberbank.ru/privacy/cookies"

key = "russian_trusted_sub_ca_pem.crt"
key = "russian_trusted_root_ca_pem.crt"
key = "sberbank.ru.crt"
key = "consolidate.pem"
key = "cert22.pem"
key = "cert33.pem"
key = "russiantrustedca.pem"
key = "invert.pem"

keyPath = os.path.join(dirPath, key)

os.environ["REQUESTS_CA_BUNDLE"] = keyPath
#os.environ["SSL_CERT_FILE"] = keyPath

headers = {
    'Accept': 'text/html',
    'Cache-Control': 'no-cache'
}


print("=" * 50)
resp = requests.get(url) # verify=keyPath cert=(keyPath)
print(resp.status_code)
print(resp.headers)
print(resp.cookies.get_dict())
print(resp.text)

'''
default_headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/json',
}

session = requests.Session()
print(session.cookies.get_dict())
print("=" * 50)

response = session.get(url, headers=default_headers, verify=key)
print(response.headers)
print(response.request.headers)
print(session.cookies.get_dict())
print(response.status_code)
print(response.text)
print("=" * 50)
'''


'''
response = session.get(url, verify=key)
print(session.cookies.get_dict())
print(response.status_code)
print(response.text)
print("=" * 50)
'''