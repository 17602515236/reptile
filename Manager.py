

class Manager(object):
    def __init__(self):
        self.No_used_url = set()
        self.used_url = set()
        self.max_noused_url = 1000

    def get_newurl_len(self):
        return len(self.No_used_url)

    def add_one_url(self,url):
        #限制等待序列的大小
        if self.get_newurl_len() < 1000:
            self.No_used_url.add(url)

    def get_one_url(self):
        if len(self.No_used_url) != 0:
            new_url = self.No_used_url.pop()
            self.used_url.add(new_url)
            return new_url
        else:
            return None

