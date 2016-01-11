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

                    if keyurl1 is not None:
                        process_keyurl(keyurl1)

    def process_urllist(url_list):
        for url in url_list:
            #print url,"sub url"
            urlinfo = gethtml.process_url(url)

            if urlinfo is None:
                continue

            list, keyurl = urlinfo

            if list is not None:
                process_urllist(list)

            if keyurl is not None:
                process_keyurl(keyurl)

            time.sleep(0.1)


    suburl = []
    subkeyurl = {}

    for url in urllist:
        print url, "root url"

        urlinfo = gethtml.process_url(url)

        if urlinfo is None:
            continue

        list, keyurl = urlinfo

        suburl.extend(list)
        subkeyurl.update(keyurl)

    try:
        process_urllist(suburl)
        process_keyurl(subkeyurl)

    except:
        import traceback
        traceback.print_exc()

urllist = ["http://www.qidian.com/Default.aspx",
           "http://www.zongheng.com/",
           "http://chuangshi.qq.com/"
           ]

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