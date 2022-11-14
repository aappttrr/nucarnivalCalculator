import io


def getWelcomeContent():
    output = io.StringIO()
    writeLineString(output, '')
    writeLineString(output, 'ヽ(✿ﾟ▽ﾟ)ノ')
    writeWriteSpace(output, 8)
    writeLineString(output, '最近特别沉迷新世界所以做了个伤害计算！')
    writeWriteSpace(output, 8)
    writeLineString(output, '如果对你有帮助的话，就支持一下吧！')
    writeWriteSpace(output, 8)
    writeLineString(output, '有任何问题、Bug都可以给我留言~~')
    writeLineString(output, '')
    writeLineString(output, '')
    writeLineString(output, 'B站：纳萨尔')
    return output.getvalue()


def getHelpContent():
    output = io.StringIO()
    writeLineString(output, '当前版本：v1.0-2022-11-14')
    writeLineString(output, '有任何问题、Bug都可以给我留言~~')
    writeLineString(output, 'B站：纳萨尔')
    writeLineString(output, '')
    writeLineString(output, '设置属性：')
    writeWriteSpace(output, 8)
    writeLineString(output, '①在卡牌列表中可以设置每个卡牌的基础属性。')
    writeWriteSpace(output, 8)
    writeLineString(output,
                    '②如果勾选了“使用期望数值”，在每次计算伤害前会根据等级、星级、蜜话、潜能计算得出期望HP和ATK（会存在误差）。')
    writeWriteSpace(output, 8)
    writeLineString(output, '③星级、潜能将会影响该卡牌的技能倍率、被动是否触发，请一定要设置准确！')

    writeLineString(output, '')
    writeLineString(output, '伤害计算：')
    writeWriteSpace(output, 8)
    writeLineString(output, '①在卡牌列表中选择1-5个卡牌作为当前出战卡牌（不可重复）。')
    writeWriteSpace(output, 8)
    writeLineString(output, '②在战斗设置中设置战斗回合数（1-50），默认为13')
    writeWriteSpace(output, 8)
    writeLineString(output, '③在不设置对轴、防御的情况下会模拟自动战斗，会严格按照队伍卡牌顺序行动，自动释放必杀技。')
    writeWriteSpace(output, 8)
    writeLineString(output,
                    '④对轴功能，在战斗设置中设置释放必杀技的回合数，除设置以外的回合数将不会释放必杀技，仍会按照卡牌顺序行动，仍需要计算必杀技cd。')
    writeWriteSpace(output, 8)
    writeLineString(output,
                    '⑤防御功能，在战斗设置中可设置防御的回合数，除设置以外的回合数将会执行攻击（普通攻击/必杀技），在同一回合同时设置了防御和对轴，会优先执行防御请注意！')

    writeLineString(output, '')
    writeLineString(output, 'HP、ATK计算公式：')
    writeWriteSpace(output, 8)
    writeLineString(output, '期望数据 = 基础数据 * 蜜话加成 * 潜能加成 / 星级削减 / 等级削减（全部计算完后向上取整）')
    writeLineString(output, '')
    writeWriteSpace(output, 8)
    writeLineString(output, '基础数据：回廊中60级5星0潜能0蜜话的数据')
    writeWriteSpace(output, 8)
    writeLineString(output, '蜜话加成：分别是5%，10%，20%，30%，50%')
    writeWriteSpace(output, 8)
    writeLineString(output, '潜能加成：根据角色潜能类型有所不同，这里不全部列举，一般分为攻击型、防御型、平衡型、NR型')
    writeWriteSpace(output, 8)
    writeLineString(output, '星级削减：x星数据 = x+1星数据 / （1 + /（5+x））')
    writeWriteSpace(output, 8)
    writeLineString(output, '等级削减：x级数据 = x+1级数据/ 1.05')

    writeLineString(output, '')
    writeLineString(output, '伤害计算公式：')
    writeWriteSpace(output, 8)
    writeLineString(output, '根据技能描述选择基础攻击力/实时攻击力，每一次加成后伤害数值向下取整')
    writeLineString(output, '')
    writeWriteSpace(output, 8)
    writeLineString(output,
                    '实时攻击力 = 基础攻击力 * 攻击力加成 + 以具体数值进行加成的攻击力（例如增益提供的攻击力加成）')
    writeLineString(output, '')
    writeWriteSpace(output, 8)
    writeLineString(output, '普攻/必杀伤害 = 基础攻击力/实时攻击力 * 倍率 * 普攻/必杀加成 * 伤害加成')
    writeWriteSpace(output, 8)
    writeLineString(output, '最终普攻/必杀伤害 = 普攻/必杀伤害 * 敌方受普攻/必杀加成 * 敌方受伤害加成 * 属性压制')
    writeLineString(output, '')
    writeWriteSpace(output, 8)
    writeLineString(output, 'DOT是锁面板技能，在挂buff的那一刻就确定了DOT伤害（HOT也一样），并且DOT没有属性压制')
    writeWriteSpace(output, 8)
    writeLineString(output, 'DOT伤害 = 基础攻击力/实时攻击力 * 倍率 * 持续伤害加成 * 伤害加成')
    writeWriteSpace(output, 8)
    writeLineString(output,
                    '最终DOT伤害 = DOT伤害 * （敌方受持续伤害加成+敌方受伤害加成）【这里非常特殊是加算，不排除是bug】')
    writeLineString(output, '')
    writeWriteSpace(output, 8)
    writeLineString(output,
                    '反击和追击比较特殊，其可能会被视为普攻也可能会被视为必杀，所以如果视为普攻则会吃到普攻加成，'
                    '视为必杀则会吃到必杀加成【例如普团的追击曾经无法吃到普攻加成，后来又改成能吃到；'
                    '而花昆和布儡的反击则可以吃到必杀加成】')
    writeWriteSpace(output, 8)
    writeLineString(output, '反击/追击伤害 = 基础攻击力/实时攻击力 * 倍率 * 普攻/必杀加成 * 伤害加成')
    writeWriteSpace(output, 8)
    writeLineString(output, '最终反击/追击伤害 = 反击/追击伤害 * 敌方受普攻/必杀加成 * 敌方受伤害加成 * 属性压制')
    return output.getvalue()


def getUpdateLogContent():
    output = io.StringIO()
    getUpdateLogContent_1_0(output)
    return output.getvalue()


def getUpdateLogContent_1_0(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2022.11.13')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v1.0:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①录入所有卡牌数据')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '②确定HP、ATK计算公式')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '③确定伤害计算公式')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '④完成基本开发')


def writeString(_output: io.StringIO, content: str):
    _output.seek(0, 2)
    _output.write(content)


def writeLineString(_output: io.StringIO, content: str):
    _output.seek(0, 2)
    _output.write(content + '\n')


def writeDashString(_output: io.StringIO, count: int):
    _output.seek(0, 2)
    for i in range(count):
        _output.write('-')


def writeWriteSpace(_output: io.StringIO, count: int):
    _output.seek(0, 2)
    for i in range(count):
        _output.write(' ')
