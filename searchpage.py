# -*- coding: UTF-8 -*-
# usesearch
# create at 2015/10/31
# autor: qianqians
import sys
sys.path.append('../')
from plask import *
import usesearch

def add_title():
    pass


def layout():
    app = plaskapp('0.0.0.0', 5000)

    p = pypage('vii', 'http://127.0.0.1:5000/', pyhtmlstyle.margin_auto)
    p.add_page_route('/')

    c = pycontainer('title_input', pyhtmlstyle.margin_auto, p)
    c.set_location(580, 350)

    titletitle = pyedit('title_edit', pyedit.text, pyhtmlstyle.float_left, c)
    titletitle.set_size(300, 20)
    titletitle.set_location(10, 0)
    button = pybutton('千度呢', 'button', pyhtmlstyle.float_left, c)
    button.set_size(60, 26)
    button.set_location(3, 0)
    ev = uievent('http://127.0.0.1:5000/', button, pyelement.onclick)
    ev.add_call_ui(add_title)
    params = jparams()
    params.append("input", titletitle.client_get_input_text())
    onsev = on_server_response()
    sev = server_event("submit", params, onsev)
    def on_click(p):
        return usesearch.find_page(p['input'])
    sev.add_onevent(on_click)
    onsev.add_call(add_title())
    ev.add_server_event(sev)
    button.register_uievent(ev)

    p.init()

    app.run()


if __name__ == '__main__':
    #usesearch.init()

    layout()