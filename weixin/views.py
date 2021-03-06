from wechat_sdk import WechatConf, WechatBasic
from bottle import request, response
from fangli.weixin import const
from fangli.coupon.bot import CouponBot

wechat_conf = WechatConf(token=const.Token,
                         appid=const.AppId,
                         appsecret=const.AppSecret,
                         encrypt_mode="normal",
                         encoding_aes_key=const.EncodingAESKey)
wx_sdk = WechatBasic(conf=wechat_conf)


def wx_validate_view():
    signature = request.query.get("signature")
    timestamp = request.query.get("timestamp")
    nonce = request.query.get("nonce")
    echostr = request.query.get("echostr")
    from_wx = wx_sdk.check_signature(signature, timestamp, nonce)
    if from_wx:
        response.status = 200
        return echostr
    else:
        response.status = 403
        return "invalid"


def wx_bot_view():
    signature = request.query.get("signature")
    timestamp = request.query.get("timestamp")
    nonce = request.query.get("nonce")
    try:
        wx_sdk.parse_data(request.body.read(), signature, timestamp, nonce)
        msg = wx_sdk.message.content
    except:
        msg = "服务器打了个盹- -"
    response.status = 200
    resp = CouponBot.respond(msg)
    wx_resp = wx_sdk.response_text(resp)
    response.status = 200
    return wx_resp
