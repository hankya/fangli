from fangli.weixin.views import wx_validate_view, wx_bot_view

def setup_routing(app):
    app.route("/api/v1/weixin", "GET", wx_validate_view)
    app.route("/api/v1/weixin", "POST", wx_bot_view)