from RoleCards.enum.tierType import TierType


def getTierData(tierType: TierType, tier, isAtk=True):
    match tierType:
        case TierType.Attack:
            return getAttackTypeTierData(tier, isAtk)
        case TierType.Defense:
            return getDefenseTypeTierData(tier, isAtk)
        case TierType.Balance:
            return getBalanceTypeTierData(tier, isAtk)
    return 0


def getAttackTypeTierData(tier, isAtk=True):
    if tier < 0:
        tier = 0
    elif tier > 12:
        tier = 12

    match tier:
        case 0:
            return 0
        case 1:
            if isAtk:
                return 0.04
            else:
                return 0.12
        case 2:
            if isAtk:
                return 0.08
            else:
                return 0.26
        case 3:
            if isAtk:
                return 0.16
            else:
                return 0.33
        case 4:
            if isAtk:
                return 0.22
            else:
                return 0.435
        case 5:
            if isAtk:
                return 0.28
            else:
                return 0.54
        case 6:
            if isAtk:
                return 0.34
            else:
                return 0.61
        case 7:
            if isAtk:
                return 0.44
            else:
                return 0.68
        case 8:
            if isAtk:
                return 0.54
            else:
                return 0.75
        case 9:
            if isAtk:
                return 0.64
            else:
                return 0.82
        case 10:
            if isAtk:
                return 0.76
            else:
                return 0.89
        case 11:
            if isAtk:
                return 0.88
            else:
                return 0.96
        case 12:
            return 1


def getDefenseTypeTierData(tier, isAtk=True):
    if tier < 0:
        tier = 0
    elif tier > 12:
        tier = 12

    match tier:
        case 0:
            return 0
        case 1:
            if isAtk is False:
                return 0.04
            else:
                return 0.12
        case 2:
            if isAtk is False:
                return 0.08
            else:
                return 0.26
        case 3:
            if isAtk is False:
                return 0.16
            else:
                return 0.33
        case 4:
            if isAtk is False:
                return 0.22
            else:
                return 0.435
        case 5:
            if isAtk is False:
                return 0.28
            else:
                return 0.54
        case 6:
            if isAtk is False:
                return 0.34
            else:
                return 0.61
        case 7:
            if isAtk is False:
                return 0.44
            else:
                return 0.68
        case 8:
            if isAtk is False:
                return 0.54
            else:
                return 0.75
        case 9:
            if isAtk is False:
                return 0.64
            else:
                return 0.82
        case 10:
            if isAtk is False:
                return 0.76
            else:
                return 0.89
        case 11:
            if isAtk is False:
                return 0.88
            else:
                return 0.96
        case 12:
            return 1


def getBalanceTypeTierData(tier, isAtk=True):
    if tier < 0:
        tier = 0
    elif tier > 12:
        tier = 12

    match tier:
        case 0:
            return 0
        case 1:
            if isAtk:
                return 0.162
            else:
                return 0
        case 2:
            if isAtk:
                return 0.162
            else:
                return 0.162
        case 3:
            if isAtk:
                return 0.243
            else:
                return 0.243
        case 4:
            if isAtk:
                return 0.382
            else:
                return 0.27
        case 5:
            if isAtk:
                return 0.41
            else:
                return 0.41
        case 6:
            if isAtk:
                return 0.466
            else:
                return 0.494
        case 7:
            if isAtk:
                return 0.55
            else:
                return 0.58
        case 8:
            if isAtk:
                return 0.64
            else:
                return 0.67
        case 9:
            if isAtk:
                return 0.73
            else:
                return 0.76
        case 10:
            if isAtk:
                return 0.82
            else:
                return 0.85
        case 11:
            if isAtk:
                return 0.91
            else:
                return 0.94
        case 12:
            return 1
