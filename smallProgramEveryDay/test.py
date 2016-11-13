import urllib.request
url = 'http://www.baidu.com'
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

request = urllib.request.Request(url)
request.add_header('user-agent','Mozilla/5.0')
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))
