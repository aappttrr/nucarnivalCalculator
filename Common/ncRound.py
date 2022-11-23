from decimal import Decimal

'''
ROUND_CEILING（朝向无限），
ROUND_DOWN（朝向零），
ROUND_FLOOR（朝向无限），
ROUND_HALF_DOWN（最接近，领带朝向零），
ROUND_HALF_EVEN（到最近的，领带到最近的偶数整数），
ROUND_HALF_UP（最接近零）或ROUND_ UP（远离零）。
ROUND_05UP（如果向零舍入后的最后一位数字为0或5，则远离零；否则为零）
'''


def roundCeiling(value=0, arg="1."):
    return int(Decimal(value).quantize(Decimal(arg), rounding='ROUND_CEILING'))


def roundDown(value=0, arg="1."):
    return int(Decimal(value).quantize(Decimal(arg), rounding='ROUND_DOWN'))


def roundHalfEven(value, arg="0.01"):
    return float(Decimal(value).quantize(Decimal(arg), rounding='ROUND_HALF_EVEN'))
