import requests
import os

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