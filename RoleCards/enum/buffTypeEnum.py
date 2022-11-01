import enum


class BuffType(enum.Enum):
    # 特殊类型buff，
    Hot = '持续治疗'
    Dot = '持续伤害'
    BloodSucking = '吸血'
    FollowUpAttack = '追击'
    CounterAttack = '反击'
    Shield = '护盾'
    Taunt = '嘲讽'
    DisTaunt = '解除嘲讽'

    # 基础数值增加
    AtkIncrease = '攻击力增加'
    AtkIncreaseByActualValue = '以具体数值增加攻击力'
    HpIncrease = '最大生命值增加'

    # 特殊效果增加
    HotIncrease = '持续治疗增加'
    DotIncrease = '持续伤害增加'
    AttackIncrease = '普攻伤害增加'
    SkillIncrease = '必杀伤害增加'
    DamageIncrease = '造成伤害增加'
    ShieldIncrease = '造成护盾增加'
    HealIncrease = '造成回复量增加'

    BeHealIncrease = '受到回复量增加'
    BeShieldIncrease = '受到护盾效果增加'
    BeAttackIncrease = '受到普攻伤害增加'
    BeSkillIncrease = '受到必杀伤害增加'
    BeDotIncrease = '受到持续伤害增加'
    BeDamageIncrease = '受到伤害增加'

    DefenseDamageReduction = '防御减伤'

