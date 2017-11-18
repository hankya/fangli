import logging

import sys

import bottle
from fangli.weixin.app import setup_routing as setup_weixin_routing

app = bottle.Bottle()
setup_weixin_routing(app)

log_format = "%(asctime)s %(levelname)s %(process)d %(message)s"
root = logging.getLogger()
root.handlers = []  # fix reimport issue
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
ch.setFormatter(log_format)
root.addHandler(ch)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, accesslog='-', reloader=True)
else:
    application = app
