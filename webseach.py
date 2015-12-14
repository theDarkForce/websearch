# -*- coding: UTF-8 -*-
# webseach
# create at 2015/10/30
# autor: qianqians

import sys
reload(sys)
sys.setdefaultencoding('utf8')

sys.path.append('../')

from webget import gethtml
import pymongo
from doclex import doclex
import time

collection_key = None

def seach(urllist):
    for url in urllist:
        gethtml.process_link(url)

urllist = ["http://www.qidian.com/Default.aspx",
           "http://www.zongheng.com/",
           "http://chuangshi.qq.com/",
           "http://www.jjwxc.net/",
           "https://www.hao123.com/",
           "http://sports.sina.com.cn/",
           "http://www.tom.com/",
           "http://www.qq.com/",
           "http://www.163.com/"]

def refkeywords():
    c = collection_key.find()
    keywords = []
    for it in c:
        keywords.append(it["key"])
    doclex.keykorks = keywords

if __name__ == '__main__':
    conn = pymongo.Connection('localhost',27017)
    db = conn.webseach
    gethtml.collection = db.webpage
    gethtml.collection_url_profile = db.urlprofile
    gethtml.collection_url_title = db.urltitle
    collection_key = db.keys

    t = 0
    while True:
        timetmp = time.time()-t
        if timetmp > 86400:
            refkeywords()
            t = time.time()
        seach(urllist)
