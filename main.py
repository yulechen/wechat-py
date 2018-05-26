# -*- coding: utf-8 -*-
# filename: main.py
# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle
from web.wsgiserver import CherryPyWSGIServer

#CherryPyWSGIServer.ssl_certificate = "server.crt"
#CherryPyWSGIServer.ssl_private_key = "server.key"

urls = (
    '/wx', 'Handle'
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()