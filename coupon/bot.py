COUPON_TPL = """已为您找到 *{q}*, 点此前往{}"""
CMD_TPL = """
1. 查找优惠券请以"找"开头，例如"找面膜"
"""


class CouponBot:
    @staticmethod
    def respond(msg):
        index = msg.index("找")
        if index >= 0:
            q = msg[index+1:].strip()
            return COUPON_TPL.format(q=q)
        else:
            return CMD_TPL.format(msg)