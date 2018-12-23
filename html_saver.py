import urllib.request
class Saver(object):
    def save(self,serial,html):
        try:
            if type(html) != bytes:
                with open("./save/{}.html".format(serial),'w') as f:
                    f.write(html)
        except Exception as e:
            print("saver error of {}".format(e))
