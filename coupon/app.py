from fangli.coupon.views import bot_view


def setup_routing(app):
    app.route("/api/v1/coupon/bot", "GET", bot_view)
