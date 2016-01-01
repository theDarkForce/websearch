# -*- coding: UTF-8 -*-
# usesearch
# create at 2015/10/31
# autor: qianqians
import sys
sys.path.append('../')
from plask import *
import pymongo
import usesearch
from webget import gethtml

def add_title():
    code = "\nvar board = document.getElementById(\"search_output_1\");\n"
    code += "for(var i in value['urllist']){\n"
    code += "   var url = value['urllist'][i];"
    code += "   var dc = document.createElement(\"div\");\n"
    code += "   dc.style.margin = \"20px 0px 20px 0px\";\n"
    code += "   dc.style.clear = \"both\";\n"
    code += "   var d = document.createElement(\"div\");\n"
    code += "   d.innerHTML = url[\"title\"];"
    code += "   d.href = url[\"url\"];"
    code += "   d.style.fontSize = \"120%\";\n"
    code += "   var dt = document.createElement(\"div\");\n"
    code += "   var textnode=document.createTextNode(url[\"profile\"]);\n"
    code += "   dt.appendChild(textnode);\n"
    code += "   dt.style.fontSize = \"100%\";\n"
    code += "   var dz = document.createElement(\"div\");\n"
    code += "   dz.style.fontSize = \"80%\";\n"
    code += "   dz.style.cssFloat=\"left\";\n"
    code += "   dz.setAttribute(\"url_id\",url[\"url\"]);\n"
    code += "   var textnode=document.createTextNode(url[\"url\"]);\n"
    code += "   dz.appendChild(textnode);\n"
    code += "   var textnode=document.createTextNode('      ');\n"
    code += "   dz.appendChild(textnode);\n"
    code += "   var textnode=document.createTextNode(url[\"date\"]);\n"
    code += "   dz.appendChild(textnode);\n"
    code += "   dc.appendChild(d);\n"
    code += "   dc.appendChild(dt);\n"
    code += "   dc.appendChild(dz);\n"
    code += "   if (board.firstChild){board.insertBefore(dc, board.firstChild);}else{board.appendChild(dc);}\n"
    code += "}"

    return code

def on_search(p):
    print 'on_search'
    return {"urllist":usesearch.find_page(p['input'], p['index'])}

def layout():
    app = plaskapp('0.0.0.0', 5000)

    p = pypage('websearch', 'http://127.0.0.1:5000/', pyhtmlstyle.margin_auto)
    p.add_page_route('/')

    c = pycontainer('title_input', pyhtmlstyle.margin_auto, p)
    c.set_location(580, 320)

    b = pycontainer('search_output', pyhtmlstyle.margin_auto, p)
    b.set_visibility(False)

    pnotes = pytext("千度又如何", "notes", pyhtmlstyle.margin_auto, c)
    pnotes.set_font_size(200)
    pnotes.set_font_color((100, 100, 200))
    pnotes.left = 100
    titletitle = pyedit('title_edit', pyedit.text, pyhtmlstyle.float_left, c)
    titletitle.set_size(300, 24)
    titletitle.set_location(10, 0)
    button = pybutton('千度吧', 'button', pyhtmlstyle.float_left, c)
    button.set_size(80, 30)
    button.set_location(3, 0)
    ev = uievent('http://127.0.0.1:5000/', button, pyelement.onclick)
    params = jparams()
    params.append("input", titletitle.client_get_input_text())
    params.append("index", '0')
    onsev = on_server_response()
    sev = server_event("submit", params, onsev)
    onsev.add_call(c.server_set_visible(False))
    onsev.add_call(b.server_set_visible(True))
    onsev.add_call(add_title())
    sev.add_onevent(on_search)
    ev.add_server_event(sev)
    button.register_uievent(ev)

    p.init()

    app.run()


if __name__ == '__main__':
    conn = pymongo.Connection('localhost',27017)
    db = conn.webseach
    usesearch.collection_page = db.webpage
    usesearch.collection_key = db.keys
    print usesearch.collection_page,usesearch.collection_key
    gethtml.collection = db.webpage
    gethtml.collection_url_profile = db.urlprofile
    gethtml.collection_url_title = db.urltitle

    layout()