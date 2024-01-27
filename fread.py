import os
from html.parser import HTMLParser

fileName = 'parse/response.html'

filePath = os.path.join(os.path.dirname(__file__), fileName)


f = open(filePath, "r")
print(f.read())