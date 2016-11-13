import urllib.request
from bs4 import BeautifulSoup
import re
import pdb

url = 'https://www.baidu.com'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")
print(soup)
