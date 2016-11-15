import urllib.request

class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        if(response.getcode() != 200):
            return None
        data = response.read().decode("UTF-8",'ignore')
        return data
