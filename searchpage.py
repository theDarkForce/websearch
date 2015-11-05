# -*- coding: UTF-8 -*-
# usesearch
# create at 2015/10/31
# autor: qianqians
import sys
sys.path.append('../')
from plask import *
import usesearch

def add_title():
	code = "var board = document.createElement(\"div\");"
	code += "var dc = document.createElement(\"div\");"
	code += "for(var url in value['urllist']){"
	code += "	"
	code += "}"
	code += "dc.setAttribute(\"id\",value[\"title_id\"]);"
	code += "dc.style.margin = \"10px auto auto 0px\";"
	code += "dc.style.width = \"1200px\";"
	code += "dc.style.borderStyle = \"solid\";"
	code += "dc.style.borderWidth = \"1px\";"
	code += "dc.style.clear = \"both\";"
	code += "var d = document.createElement(\"div\");"
	code += "d.setAttribute(\"id\",value[\"id_1\"]);"
	code += "d.style.fontSize = \"150%\";"
	code += "var textnode=document.createTextNode(value[\"title\"]);"
	code += "d.appendChild(textnode);"
	code += "var dt = document.createElement(\"div\");"
	code += "dt.setAttribute(\"id\",value[\"id_1_1\"]);"
	code += "var textnode=document.createTextNode(value[\"input\"]);"
	code += "dt.appendChild(textnode);"
	code += "var dz = document.createElement(\"div\");"
	code += "dz.style.fontSize = \"50%\";"
	code += "dz.style.cssFloat=\"left\";"
	code += "dz.style.margin = \"10px auto 5px auto\";"
	code += "var textnode=document.createTextNode(\"作者:\");"
	code += "dz.appendChild(textnode);"
	code += "var dzu = document.createElement(\"div\");"
	code += "dzu.style.cssFloat=\"left\";"
	code += "dzu.style.fontSize = \"50%\";"
	code += "dzu.style.margin = \"10px 5px 5px auto\";"
	code += "var textnode=document.createTextNode(value[\"username\"]);"
	code += "dzu.appendChild(textnode);"
	code += "var dl = document.createElement(\"div\");"
	code += "var textnode=document.createTextNode(\"联系方式:\");"
	code += "dl.style.cssFloat=\"left\";"
	code += "dl.style.fontSize = \"50%\";"
	code += "dl.style.margin = \"10px auto 5px auto\";"
	code += "dl.appendChild(textnode);"
	code += "var dlc = document.createElement(\"div\");"
	code += "var textnode=document.createTextNode(value[\"contact\"]);"
	code += "dlc.appendChild(textnode);"
	code += "dlc.style.fontSize = \"50%\";"
	code += "dlc.style.margin = \"10px auto 5px auto\";"
	code += "dc.appendChild(d);"
	code += "dc.appendChild(dt);"
	code += "dc.appendChild(dz);"
	code += "dc.appendChild(dzu);"
	code += "dc.appendChild(dl);"
	code += "dc.appendChild(dlc);"
	code += "if (board.firstChild){board.insertBefore(dc, board.firstChild);}else{board.appendChild(dc);}"
	return code

def on_search(p):
    return {"urllist":usesearch.find_page(p['input'], p['index'])}

def layout():
    app = plaskapp('0.0.0.0', 5000)

    p = pypage('vii', 'http://127.0.0.1:5000/', pyhtmlstyle.margin_auto)
    p.add_page_route('/')

    c = pycontainer('title_input', pyhtmlstyle.margin_auto, p)
    c.set_location(580, 350)

    pnotes = pytext("千度又如何", "notes", pyhtmlstyle.margin_auto, c)
    pnotes.set_font_size(200)
    pnotes.set_font_color((100, 100, 200))
    pnotes.left = 100
    titletitle = pyedit('title_edit', pyedit.text, pyhtmlstyle.float_left, c)
    titletitle.set_size(300, 20)
    titletitle.set_location(10, 0)
    button = pybutton('千度吧', 'button', pyhtmlstyle.float_left, c)
    button.set_size(80, 20)
    button.set_location(3, 0)
    ev = uievent('http://127.0.0.1:5000/', button, pyelement.onclick)
    params = jparams()
    params.append("input", titletitle.client_get_input_text())
    params.append("index", '0')
    onsev = on_server_response()
    sev = server_event("submit", params, onsev)
    sev.add_onevent(on_search)
    onsev.add_call(c.remove())
    onsev.add_call(add_title())
    ev.add_server_event(sev)
    button.register_uievent(ev)

    p.init()

    app.run()


if __name__ == '__main__':
    #usesearch.init()

    layout()