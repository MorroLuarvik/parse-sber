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

fileName = 'parse/response.html'

filePath = os.path.join(os.path.dirname(__file__), fileName)

f = open(filePath, "r")
body = f.read() 
f.close()

parser = MyHTMLParser()
parser.feed(body)
parser.close()

print(parser.links)

#print(feed)