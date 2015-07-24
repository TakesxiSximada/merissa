#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    port = int(os.environ.get('VCAP_APP_PORT', 8000))
    application.listen(port)
    tornado.ioloop.IOLoop.current().start()
