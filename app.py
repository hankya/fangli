import bottle
from fangli.weixin.app import setup_routing as setup_weixin_routing

app = bottle.Bottle()
setup_weixin_routing(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, accesslog='-', reloader=True)
else:
    application = app
