import os

fileName = 'key'

filePath = os.path.join(os.path.dirname(__file__), fileName)


f = open(filePath, "r")
print(f.read())