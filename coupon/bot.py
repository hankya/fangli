COUPON_TPL = """已为您找到<a href="{url}">{q}的优惠券</a>"""
CMD_TPL = """1. 查找优惠券请以"找"开头，例如\"找面膜\""""
TARGET_TPL = """http://varnish.chunqiufanli.cn/ProductList.aspx?m=search&a=index&keyWord={q}&ReferralId=8548"""


class CouponBot:
    @staticmethod
    def respond(msg):
        index = msg.find("找")
        if index >= 0:
            q = msg[index + 1:].strip()
            return COUPON_TPL.format(q=q, url=TARGET_TPL.format(q=q))
        else:
            return CMD_TPL.format(msg)
