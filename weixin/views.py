from wechat_sdk import WechatConf, WechatBasic
from bottle import request, response
from fangli.weixin import const
import json

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
    wx_sdk.parse_data(request.body.read(), signature, timestamp, nonce)
    response.status = 200
    return json.dumps(wx_sdk.message.__dict__)
