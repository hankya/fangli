COUPON_TPL = """已为您找到<a href="{url}">{q}的优惠券</a>"""
CMD_TPL = """1. 查找优惠券请以"找"开头，例如\"找面膜\""""
PROXY_URL_TPL = """http://fanyi.baidu.com/transpage?query={target}&from=cht&to=zh&source=url&render=1"""
TARGET_TPL = """http://taoxmall.com/ProductList.aspx?m=search&a=index&keyWord={q}&ReferralId=8548"""


def gen_url(q):
    target = TARGET_TPL.format(q=q)
    from urllib.parse import quote_plus
    return PROXY_URL_TPL.format(target=quote_plus(target))


class CouponBot:
    @staticmethod
    def respond(msg):
        index = msg.find("找")
        if index >= 0:
            q = msg[index + 1:].strip()
            return COUPON_TPL.format(q=q, url=gen_url(q))
        else:
            return CMD_TPL.format(msg)
