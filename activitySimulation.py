import datetime

from Activity.activityReward import ActivityReward
from Common.ncRound import roundCeiling
from Nucarnival.activityRewardHelper import ActivityRewardHelper
from Props.propTypeEnum import PropType


def simulation(_helper, days, rewardData, title):
    totalEnergy = _helper.calTotalEnergy(days)
    data = _helper.calNeedEnergy(days, totalEnergy)
    energy = data['energy']
    energy -= rewardData['energy']
    gem = 0
    if energy > 0:
        gem = roundCeiling(energy * 5 / 3)
        gem -= rewardData['gem']
    if energy < 0:
        energy = 0
    if gem < 0:
        gem = 0
    print(title + '，扣除活动奖励的体力和晶灵石，仍需要体力{}，即{}晶灵石'.format(str(energy), str(gem)))


if __name__ == '__main__':
    _helper = ActivityRewardHelper()
    _helper.coin = True
    _helper.holyWater = True

    _helper.startDate = datetime.date(2022, 11, 24)
    _helper.endDate = datetime.date(2022, 12, 15)
    days = _helper.getDays()

    # _helper.activityRewards.append(ActivityReward(PropType.spiritGem, 500, 10000))
    _helper.battlePoint = 100
    _helper.battleCost = 30

    _helper.targetPoint = 36000
    rewardData = _helper.calRewards(_helper.targetPoint)

    print('活动共{}天，刷到{}积分，总共可以获得{}体力，{}晶灵石'
          .format(days, _helper.targetPoint, rewardData['energy'], rewardData['gem']))
    # 无氪
    _helper.xyk = False
    _helper.dyk = False
    simulation(_helper, days, rewardData, '无氪')

    # 小月卡
    _helper.xyk = True
    _helper.dyk = False
    simulation(_helper, days, rewardData, '小月卡')

    # 小月卡+大月卡
    _helper.xyk = True
    _helper.dyk = True
    simulation(_helper, days, rewardData, '小月卡+大月卡')
