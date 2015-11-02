# -*- coding: UTF-8 -*-
# usesearch
# create at 2015/10/31
# autor: qianqians
import sys
sys.path.append('../')
import pymongo
from doclex import doclex

collection_page = None
collection_key = None

def find_page(input):
    keys = doclex.splityspace(input)
    for k in keys:
        collection_key.insert({"key":k})
    page_list = []
    for k in keys:
        c = collection_page.find({"key":k})
        for i in c:
            page_list.append(i)
    if len(page_list) == 0:
        keys = doclex.lex(keys)
        for k in keys:
            c= collection_page.find({"key":k})
        for i in c:
            page_list.append(i)
    return page_list

def init():
    conn = pymongo.Connection('localhost',27017)
    db = conn.webseach
    collection_page = db.webpage
    collection_key = db.keys