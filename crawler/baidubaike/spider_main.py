import html_parser,html_outputer,html_downloader,url_manager
import io
import sys

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):
        count = 1
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
        self.urls.add_new_url(root_url)
        while(self.urls.has_new_url()):
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s'%(count,new_url))
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if(count > 50):
                    break
                count = count + 1
            except Exception as e:
                print(e)
                print('craw file')
        self.outputer.output_html()



if __name__=="__main__":
    root_url = 'http://baike.baidu.com/item/Python'
    # root_url = 'http://baike.baidu.com/item/TOM/39488'
    spider = SpiderMain()
    spider.craw(root_url)
