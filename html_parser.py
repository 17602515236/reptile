import re,Manager
class Parser(object):
    def __init__(self,_manager):
        self.pat = re.compile(r'(https?://[^\s";]+(\.(\w|/)*))')
        self.manager = _manager

    def parse(self,html):
        picture_set = set()
        try:
            html = html.read().decode()
        except Exception as e:
            return picture_set
            #查找所有url（包括图片等）
        suburl = re.findall(self.pat,html)
        #循环每个url，图片则添加到图片序列返回，网页url添加到等待序列
        for s in suburl:
            resualt = re.search(r"((.jpg)|(.png)|(.bmp)|(.tif)|(.gif))$",s[0])
            if resualt:
                picture_set.add((s[0],resualt.groups()[0]))
            else:
                self.manager.add_one_url(s[0])
        return picture_set

