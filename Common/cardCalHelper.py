from Common.ncRound import roundDown


def calBond(lv60s5=1, _bond=0):
    result = lv60s5
    match _bond:
        case 1:
            result = result * 1.05
        case 2:
            result = result * 1.1
        case 3:
            result = result * 1.2
        case 4:
            result = result * 1.3
        case 5:
            result = result * 1.5
    return result


def calStar(lv60s5=1, _star=5):
    if _star == 5 or _star <= 0:
        return lv60s5
    result = lv60s5
    for i in reversed(range(_star, 5)):
        temp = 1 + (1 / (5 + i))
        result = result / temp
    return result


def calTier(lv60s5=1, _tierValue=0.0):
    result = lv60s5 * (1 + _tierValue)
    return result


def calLv(lv60s5=1, _lv=60):
    if _lv == 60 or _lv <= 0:
        return lv60s5
    result = lv60s5
    for i in reversed(range(_lv, 60)):
        result = result / 1.05
    return result


def calDamageOrHeal(_atk, _magnification):
    damageOrHeal = _atk * _magnification
    damageOrHeal = roundDown(damageOrHeal)
    return damageOrHeal

