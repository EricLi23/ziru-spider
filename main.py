# coding=utf-8
import requests
from pyquery import PyQuery as pq


class Zspider():
    def __init__(self, qwd):
        self.url = "http://www.ziroom.com/z/nl/z3-g2.html"
        self.qwd = qwd
        self. headers = {'user-agent': 'my-app/0.0.1'}

    def stater(self):
        res = requests.get(self.url, params={"qwd": self.qwd}, headers=self.headers)
        # print res.url
        content = res.text
        return content
        # print "res===>%s" % content

    def paraser(self,content):
        doc = pq(content)
        item = doc("#houseList li")
        for li in item.items():
            atag = li('.clearfix .txt h3 a')
            href = atag.attr.href
            title,orit = atag.text().replace(" ", "").split("-")
            print title, href[2:],orit
            #  .clearfix .txt h3 a
            # href = item.attr.href
        # print"href====>%s"%href

if __name__ == "__main__":
    z1 = Zspider("牡丹园东里")
    content = z1.stater()
    z1.paraser(content)



