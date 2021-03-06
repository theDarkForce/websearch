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
    def process_keyurl(keyurl):
        if keyurl is not None:
            for key, urllist in keyurl.iteritems():
                for url in urllist:
                    urlinfo = gethtml.process_url(url)

                    if urlinfo is None:
                        continue

                    list, keyurl1 = urlinfo

                    if list is not None:
                        gethtml.collection.insert({'key':key, 'url':url, 'timetmp':time.time()})

                    #if keyurl1 is not None:
                        #process_keyurl(keyurl1)

    def process_urllist(url_list):
        for url in url_list:
            #print url,"sub url"
            urlinfo = gethtml.process_url(url)

            if urlinfo is None:
                return

            list, keyurl = urlinfo

            process_keyurl(keyurl)

            time.sleep(0.1)

    for url in urllist:
        print url, "root url"

        urlinfo = gethtml.process_url(url)

        if urlinfo is None:
            continue

        list, keyurl = urlinfo

        try:
            process_urllist(list)
            process_keyurl(keyurl)

        except:
            import traceback
            traceback.print_exc()

urllist = ["http://sina.com.cn/",
           "http://www.tom.com/",
           "http://www.qq.com/",
           "http://www.qidian.com/Default.aspx",
           "http://www.zongheng.com/",
           "http://chuangshi.qq.com/",
           "http://www.jjwxc.net/",
           "https://www.hao123.com/",
           "http://www.163.com/",
           "http://jj.hbtv.com.cn/",
           "https://www.taobao.com/",
           "http://www.jd.com/",
           "http://www.suning.com/",
           "http://jiadian.gome.com.cn/"]

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
        #urllist = seach(urllist)
        seach(urllist)