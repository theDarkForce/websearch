# -*- coding: UTF-8 -*-
# usesearch
# create at 2015/10/31
# autor: qianqians

import sys
sys.path.append('../')
from pagecache import *
import pymongo
import time
from doclex import doclex
from webget import gethtml

collection_page = None
collection_key = None

def find_page(input, index):
    keys = doclex.splityspace(input)
    for k in keys:
        collection_key.insert({"key":k})

    if cache_page.has_key(input):
        cache_page['input']['timetmp'] = time.time()
        return cache_page['input']['urllist']

    page_list = []
    for k in keys:
        if key_page.has_key(k):
            key_page['input']['timetmp'] = time.time()
            page_list = key_page['input']['urllist']
        else:
            c = collection_page.find({"key":k})
            for i in c:
                page = {}
                page['url'] = i['url']
                page['timetmp'] = i['timetmp']
                page['key'] = i['key']
                page_list.append(page)
            key_page['input'] = {}
            key_page['input']['timetmp'] = time.time()
            key_page['input']['urllist'] = page_list

    if len(page_list) == 0:
        #keys = doclex.lex(keys)
        for k in keys:
            if key_page.has_key(k):
                key_page['input']['timetmp'] = time.time()
                page_list = key_page['input']['urllist']
            else:
                c = collection_page.find({"key":k})
                for i in c:
                    page = {}
                    page['url'] = i['url']
                    page['timetmp'] = i['timetmp']
                    page['key'] = i['key']
                    page_list.append(page)
                key_page['input'] = {}
                key_page['input']['timetmp'] = time.time()
                key_page['input']['urllist'] = page_list

    cache_page['input'] = {}
    cache_page['input']['timetmp'] = time.time()
    cache_page['input']['urllist'] = page_list

    page_list = page_list[index*10: index*1+10]

    for url in page_list:
        c = gethtml.collection_url_profile.find({'key':url['url']})
        for i in c:
            url["profile"] = i['urlprofile']
        c = gethtml.collection_url_title.find({'key':url['url']})
        for i in c:
            url["title"] = i['title']

    print page_list

    return page_list

def init():
    pass