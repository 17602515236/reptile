import Manager,html_downloader,html_saver,html_parser
import threading
flags = 0
class Scheduler(object):
    def __init__(self):
        self.manager = Manager.Manager()
        self.downloader = html_downloader.Downloader()
        self.saver = html_saver.Saver()
        self.parser = html_parser.Parser(self.manager)
        self.manager.add_one_url("https://book.douban.com/")
        self.t = threading.Thread(target = self.download_thread,args=("1",))
        self.t1 = threading.Thread(target = self.download_thread,args=("2",))
        self.t2 = threading.Thread(target = self.download_thread,args=("3",))
        self.t3 = threading.Thread(target = self.download_thread,args=("4",))
        self.t.start()
        self.t1.start()
        self.t2.start()
        self.t3.start()
        self.limits = 500
        
    def download_thread(self,n):
        global flags
        print("start to download picture")
        count = 0
        while True:
            pic = self.manager.get_one_pic()
            if pic:
                self.downloader.download_pic("{}_{}{}".format(n,count,pic[1]),pic[0])
                count += 1
            else:
                if flags == 1:
                    print("download over")
                    exit()

    def run(self):
        global flags
        current=1
        pic_set = set()
        while self.manager.get_newurl_len() and self.limits != current:
                tmp_url = self.manager.get_one_url()#获取一个url
                response = self.downloader.download_html(tmp_url)#下载html页面
                if response:
                    pic_set = self.parser.parse(response)
                    print("serial={}\turl={}".format(current,tmp_url))
                else:
                    print("serial={} failed\turl={}".format(current,tmp_url))
                current += 1
        else:
            flags = 1
            self.t.join()
            self.t1.join()
            self.t2.join()
            self.t3.join()
            print("exit,length of new_url={}".format(len(self.manager.No_used_url)))


if __name__ == "__main__":
    my_scheduler = Scheduler()
    my_scheduler.run()
