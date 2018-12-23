import urllib


class Downloader(object):
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
        proxy = {'http': '206.125.41.135:80'}
        proxy_handler = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_handler)
        urllib.request.install_opener(opener)

    def download_html(self,url):
        try:
            req = urllib.request.Request(url = url,headers = self.headers)
            response = urllib.request.urlopen(req,timeout = 3)
            return response
        except Exception as e:
            print("Downloader error in web:{}".format(url))

    def download_pic(self,name,url):
        try:
            urllib.request.urlretrieve(url,"./save/{}".format(name))
            print("download a pic of {}".format(name))
        except Exception as e:
            print("pictiure download failed {}".format(name))

