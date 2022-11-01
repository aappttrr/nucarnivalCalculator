import enum


class ConditionType(enum.Enum):
    WhenAttack = '普攻时'
    WhenSkill = '必杀时'
    WhenDamage = '造成伤害时'

    WhenBeAttacked = '被普攻时'
    WhenBeSkilled = '被必杀时'
    WhenBeDamaged = '受到伤害时'

    WhenHpMoreThan = '当Hp大于xx时'
