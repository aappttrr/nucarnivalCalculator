import io


def getWelcomeContent():
    output = io.StringIO()
    writeLineString(output, '')
    writeLineString(output, 'ヽ(✿ﾟ▽ﾟ)ノ')
    writeWriteSpace(output, 8)
    writeLineString(output, '最近特别沉迷新世界狂欢所以做了个计算工具！')
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
    writeLineString(output, '当前版本：v2.14-2024-1-7')
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
    writeLineString(output, '伤害模拟：')
    writeWriteSpace(output, 8)
    writeLineString(output, '①在卡牌列表中选择1-5个卡牌作为当前出战卡牌（不可重复）。')
    writeWriteSpace(output, 8)
    writeLineString(output, '②在战斗设置中设置战斗回合数（1-50），默认为13。默认怪物是群攻，所以夏布的反击是能吃满的。')
    writeWriteSpace(output, 8)
    writeLineString(output, '③在不设置对轴、防御、行动顺序的情况下会模拟自动战斗，按照队伍卡牌顺序行动，自动释放必杀技。')
    writeWriteSpace(output, 8)
    writeLineString(output,
                    '④对轴功能，在战斗设置中设置释放必杀技的回合数，除设置以外的回合数将不会释放必杀技，仍会按照卡牌顺序行动，仍需要计算必杀技cd。')
    writeWriteSpace(output, 8)
    writeLineString(output,
                    '⑤防御功能，在战斗设置中可设置防御的回合数，除设置以外的回合数将会执行攻击（普通攻击/必杀技），在同一回合同时设置了防御和对轴，会优先执行防御请注意！')
    writeWriteSpace(output, 8)
    writeLineString(output,
                    '⑥模拟结果：角色完整名称[实时攻击力] 普攻/必杀/防御；中括号内的实时攻击力是计算伤害时使用的实时攻击力。')
    writeWriteSpace(output, 31)
    writeLineString(output,
                    '而行动后实时攻击力，指的是计算完伤害后的实时攻击力（例如辅助行动后实时攻击力能吃到自己的增益），普攻时以攻击力造成150%治疗，就是用该实时攻击力计算。')
    writeWriteSpace(output, 31)
    writeLineString(output,
                    '我方所有角色行动后的实时攻击力，用于参考部分副本，敌方可能会攻击实时攻击力最高的角色。')
    writeWriteSpace(output, 8)
    writeLineString(output,
                    '⑦治疗量：吸血在模拟结果中显示在攻击的角色上，但在总治疗量统计的时候吸血会算在提供buff的角色上（例如奶狐）。')
    writeWriteSpace(output, 8)
    writeLineString(output,
                    '⑧攻击时：当普攻/必杀时，伤害为0，那么就不算【被攻击时】。因此火狐、奶、除瓜狼以外的辅助都无法触发地方【被攻击时】类型的buff。'
                    '反击也不算，所以不会反复触发反击（我方反击不会触发敌方反击，反过来也一样）。')
    writeWriteSpace(output, 8)
    writeLineString(output,
                    '⑨行动顺序功能，在行动顺序中可设置任意回合的角色行动顺序，除设置以外的回合、角色将会按原顺序行动。')

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
    writeLineString(output, '最终普攻/必杀伤害 = 普攻/必杀伤害 * （敌方受普攻/必杀加成 + 定位易伤） * 敌方受伤害加成 * 属性压制 '
                            '* 敌方受特定角色伤害加成（未验证是否为单独乘区）')
    writeLineString(output, '')
    writeWriteSpace(output, 8)
    writeLineString(output, 'DOT是锁面板技能，在挂buff的那一刻就确定了DOT伤害（HOT也一样），并且DOT没有属性压制')
    writeWriteSpace(output, 8)
    writeLineString(output, 'DOT伤害 = 基础攻击力/实时攻击力 * 倍率 * 持续伤害加成')
    writeWriteSpace(output, 8)
    writeLineString(output,
                    '最终DOT伤害 = DOT伤害 * （敌方受持续伤害加成+敌方受伤害加成）【这里非常特殊是加算，不排除是bug】'
                    '* 敌方受特定角色伤害加成（未验证是否为单独乘区）')
    writeLineString(output, '')
    writeWriteSpace(output, 8)
    writeLineString(output,
                    '反击和追击比较特殊，其可能会被视为普攻也可能会被视为必杀，所以如果视为普攻则会吃到普攻加成，'
                    '视为必杀则会吃到必杀加成【例如普团的追击曾经无法吃到普攻加成，后来又改成能吃到；'
                    '而花昆和布儡的反击则可以吃到必杀加成】')
    writeWriteSpace(output, 8)
    writeLineString(output, '反击/追击伤害 = 基础攻击力/实时攻击力 * 倍率 * 普攻/必杀加成 * 伤害加成')
    writeWriteSpace(output, 8)
    writeLineString(output, '最终反击/追击伤害 = 反击/追击伤害 * 敌方受普攻/必杀加成 * 敌方受伤害加成 * 属性压制 '
                            '* 敌方受特定角色伤害加成（未验证是否为单独乘区）')
    writeLineString(output, '')
    writeWriteSpace(output, 8)
    writeLineString(output, '吸血量 = 伤害 * 吸血倍率 * 受回复量加成')
    writeWriteSpace(output, 8)
    writeLineString(output, '治疗量 = 基础攻击力/实时攻击力 * 倍率 * 普攻/必杀加成 * 造成回复量加成')
    writeWriteSpace(output, 8)
    writeLineString(output, '最终治疗量 = 治疗量 * 受回复量加成')
    writeWriteSpace(output, 8)
    writeLineString(output, 'Hot量 = 基础攻击力/实时攻击力 * 倍率 * 造成回复量加成 * 持续治疗量加成')
    writeWriteSpace(output, 8)
    writeLineString(output, '最终Hot量 = Hot * 受回复量加成 * 受持续治疗量加成【夏八】')
    writeLineString(output, '')
    writeWriteSpace(output, 8)
    writeLineString(output, '护盾 = 最大HP * 倍率 * 普攻/必杀加成 * (造成护盾加成 + 护盾效果加成)')
    writeWriteSpace(output, 8)
    writeLineString(output, '最终护盾 = 护盾 * 受护盾效果加成【夏八】')
    return output.getvalue()


def getUpdateLogContent():
    output = io.StringIO()
    getUpdateLogContent_2_14(output)
    output = io.StringIO()
    getUpdateLogContent_2_13(output)
    writeLineString(output, '')
    getUpdateLogContent_2_12(output)
    writeLineString(output, '')
    getUpdateLogContent_2_11(output)
    writeLineString(output, '')
    getUpdateLogContent_2_10(output)
    writeLineString(output, '')
    getUpdateLogContent_2_9(output)
    writeLineString(output, '')
    getUpdateLogContent_2_8(output)
    writeLineString(output, '')
    getUpdateLogContent_2_7(output)
    writeLineString(output, '')
    getUpdateLogContent_2_6(output)
    writeLineString(output, '')
    getUpdateLogContent_2_5(output)
    writeLineString(output, '')
    getUpdateLogContent_2_4(output)
    writeLineString(output, '')
    getUpdateLogContent_2_3(output)
    writeLineString(output, '')
    getUpdateLogContent_2_2(output)
    writeLineString(output, '')
    getUpdateLogContent_2_1(output)
    writeLineString(output, '')
    getUpdateLogContent_2_0(output)
    writeLineString(output, '')
    getUpdateLogContent_1_2(output)
    writeLineString(output, '')
    getUpdateLogContent_1_1(output)
    writeLineString(output, '')
    getUpdateLogContent_1_0(output)
    return output.getvalue()


def getUpdateLogContent_2_14(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2024.1.7')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v2.14:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①增加勇闯新世界，伊得的新卡')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '②增加定位易伤buff')


def getUpdateLogContent_2_13(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2023.12.14')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v2.13:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①增加晶霜回声，艾德蒙特、可尔、昆西的新卡')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '②修复吸血执行的顺序')


def getUpdateLogContent_2_12(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2023.11.2')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v2.12:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①增加血之秘钥，奥利文、啖天的新卡')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '②修复水啖3星被动加成不对的问题（原来一层8%，实际是一层9%）')


def getUpdateLogContent_2_11(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2023.10.7')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v2.11:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①修复部分BUG')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '②增加锖色国度，布儡、敛、玖夜的新卡')


def getUpdateLogContent_2_10(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2023.9.13')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v2.10:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①修复治疗量算法，影响所有可治疗的角色')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '②修复烟狼被动持续回合数不对的问题')


def getUpdateLogContent_2_9(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2023.9.9')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v2.9:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①更新烟岚秘境，八云可尔新卡')


def getUpdateLogContent_2_8(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2023.8.24')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v2.8:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①更新墨菲、艾斯特SSR新卡')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '②修复多段攻击，不再多次触发')


def getUpdateLogContent_2_7(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2023.7.8')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v2.7:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①更新啖天、玖夜、副团夏活新卡')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '②暗团buff修改，多段攻击会进行多次触发，如暗奥、夏啖、火布的多段攻击'
                             '，还有普团、暗昆、早八、圣啖的追击，有多少次追击算多少次')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '③现在普攻没有伤害也可以触发追击了')


def getUpdateLogContent_2_6(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2023.6.11')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v2.6:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①更新蜜话调整后数据')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '②增加【虚实雨季】限定，伞敛、伞昆')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '③修正角色排序')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '④伞昆、普奥被动回血改为吃“必杀加成”')


def getUpdateLogContent_2_5(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2023.5.10')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v2.5:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①修复dot伤害计算公式，经验证，dot伤害不吃“伤害加成”')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '②增加早八、晚奥两张新卡')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '③由于不可设置敌方属性，血量限制条件buff不好查看是否触发，因此所有血量限制条件均不判断，默认触发')


def getUpdateLogContent_2_4(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2023.4.22')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v2.4:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①修复春日迷乱（艾德蒙特）攻击倍率错误问题，原125%，现修正为100%')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '②修复治疗量错误问题，原无法吃到普攻/必杀提升，现修正为可吃到普攻/必杀提升，具体请看计算公式，影响火团')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '③提升默认敌方攻击力，原过低的攻击力，导致盾昆和盾八防御状态受伤害位0无法触发反击')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '④优化索敌方法，追击将单独判断索敌，原圣啖追击增加后，会导致群攻角色进行多次追击（目前软件尚未能配置'
                             '多名敌方，所以不会影响旧角色）')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '⑤优化护盾、治疗统计，现在把对每个角色单独的护盾、治疗和总护盾、治疗列出')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '⑥增加行动顺序设置')


def getUpdateLogContent_2_3(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2023.2.26')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v2.3:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①新增春林狂欢宴限定卡：午夜醺然（玖夜）、春日迷乱（艾德蒙特）')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '②修复普奥3星后必杀治疗量不对的问题')


def getUpdateLogContent_2_2(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2023.1.19')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v2.2:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①新增银羽奇迹限定卡：夜雾银星（伊得）')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '②更正护盾计算公式')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '③冬昆和普啖的治疗、护盾能够吃普攻和必杀加成')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '④优化了Excel导出')


def getUpdateLogContent_2_1(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2023.1.8')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v2.1:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①新增圣夜微光限定卡：祝祷者的霜夜心愿（奥利文）、权衡者的雪藏初心（啖天）、守望者的冬季馈礼（昆西）')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '②修复了一些BUG')


def getUpdateLogContent_2_0(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2022.12.9')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v2.0:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①优化伤害记录处理逻辑')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '②增加实时攻击力数值用于参考')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '③增加盾量、治疗量用于参考')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '④增加活动计算，可以得出到目标积分需要碎钻多少，以及不碎钻的情况下能刷取多少积分')


def getUpdateLogContent_1_2(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2022.11.26')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v1.2:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①增加【专属指导】- 艾德蒙特')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '②增加【守护甜心】- 布儡')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '③优化【被攻击】判定，在一次普攻/必杀中只触发一次，伤害为0时不触发（例如辅助、奶妈）')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '④增加【受某角色伤害提升】buff，设置为独立乘区')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '⑤增加输出占比结果')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '⑥修复N卡可以定义蜜话的问题')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '⑦增加伤害模拟卡牌左移右移的功能')


def getUpdateLogContent_1_1(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2022.11.17')
    writeDashString(_output, 36)
    writeLineString(_output, '')
    writeLineString(_output, 'v1.1:')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '①修复了一些Bug')
    writeWriteSpace(_output, 8)
    writeLineString(_output, '②优化伤害模拟导出Excel的内容')


def getUpdateLogContent_1_0(_output: io.StringIO):
    writeDashString(_output, 36)
    writeString(_output, '2022.11.14')
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
    writeWriteSpace(_output, 8)
    writeLineString(_output, '⑤完成基本功能测试')


def getActivityHelpContent():
    output = io.StringIO()
    writeLineString(output, '请输入开始时间和结束时间、活动副本体力和对应积分、勾选所需选项，并点击计算')
    writeLineString(output, '')
    writeLineString(output, '日常、周常任务请自行留意是否可完成')
    writeLineString(output, '')
    writeLineString(output, '每天回复12*24=288体力（5分钟1点体力）')
    writeLineString(output, '')
    writeLineString(output, '日常任务可获取初级日月精华（30体力）x1')
    writeLineString(output, '周常任务可获取上级日月精华（100体力）x2，如果勾选了周常任务，且任务持续时间>7，则会算上2x100体力')
    writeLineString(output, '')
    writeLineString(output, '小月卡每天初级日月精华（30体力）x2')
    writeLineString(output, '大月卡每天上级日月精华（100体力）x1')
    writeLineString(output, '')
    writeLineString(output, '每日金币副本和每日经验副本各耗费50体力')
    writeLineString(output, '')
    writeLineString(output, '碎钻以200钻购买120体力为一组整体，假设需要购买140体力，则是400钻')
    return output.getvalue()


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
