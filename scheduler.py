import Manager,html_downloader,html_saver,html_parser

class Scheduler(object):
    def __init__(self):
        self.manager = Manager.Manager()
        self.downloader = html_downloader.Downloader()
        self.saver = html_saver.Saver()
        self.parser = html_parser.Parser(self.manager)
        self.manager.add_one_url("https://book.douban.com/")
        #self.manager.add_one_url("https://www.baidu.com/")
        self.limits = 100

    def run(self):
        current=1
        pic_set = set()
        while self.manager.get_newurl_len() and self.limits != current:
                tmp_url = self.manager.get_one_url()#获取一个url
                response = self.downloader.download_html(tmp_url)#下载html页面
                if response:
                    pic_set = self.parser.parse(response)
                    for v,pic_url in enumerate(pic_set):
                        self.downloader.download_pic("{}_{}{}".format(current,v,pic_url[1]),pic_url[0])
                    print("serial={}\turl={}".format(current,tmp_url))
                else:
                    print("serial={} failed\turl={}".format(current,tmp_url))
                current += 1
        else:
            print("exit,length of new_url={}".format(len(self.manager.No_used_url)))


if __name__ == "__main__":
    my_scheduler = Scheduler()
    my_scheduler.run()
