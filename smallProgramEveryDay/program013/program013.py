import os
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse

rootUrl = 'http://tieba.baidu.com/p/2166231880'
data = ''
urlList = set()

response = urllib.request.urlopen(rootUrl)
if(response.getcode() != 200):
    print('download error!')
else:
    data = response.read().decode("UTF-8",'ignore')
soup = BeautifulSoup(data,'html.parser')
links = soup.find('div',attrs={"id":'post_content_29397351011'}).find_all('img',attrs={"class":'BDE_Image'})
for link in links:
    newUrl = link['src']
    newFullUrl = urllib.parse.urljoin(rootUrl,newUrl)
    urlList.add(newFullUrl)
count = 0

for url in urlList:
    img =  urllib.request.urlopen(url).read()
    try:
        f = open('D://tuzhenyu/GitHub/python_project/smallProgramEveryDay/program013/images' + str(count)+'.jpg','wb')
        f.write(img)
        count = count + 1
        f.close()
    except Exception as e:
        print(e)
        print('write error!')
