import datetime
import io

from Activity.activityReward import ActivityReward
from Common.ncRound import roundCeiling, roundDown
from Props.propTypeEnum import PropType


class ActivityRewardHelper:
    def __init__(self):
        self.activityRewards: list[ActivityReward] = []
        self.currentPoint: int = 0
        self.targetPoint: int = 0
        self.startDate: datetime.date = None
        self.endDate: datetime.date = None
        self.tb = 0
        self.bb = 0
        self.sb = 0
        self.dailyMission = False
        self.weeklyMission = False
        self.xyk = False
        self.dyk = False
        self.coin = False
        self.holyWater = False
        self.battleCost = 10
        self.battlePoint = 30
        self.output = io.StringIO()

    def calTotalEnergy(self, days):
        dailyEnergy = self.getDailyEnergy()
        totalEnergy = dailyEnergy * days
        if self.weeklyMission:
            number = days / 7
            number = roundDown(number)
            totalEnergy += number * 200
        totalEnergy += self.tb * 10
        totalEnergy += self.bb * 30
        totalEnergy += self.sb * 100
        return totalEnergy

    def calRewards(self, _point):
        rewardEnergy = 0
        rewardSpiritGem = 0
        for reward in self.activityRewards:
            if reward.point > _point:
                continue
            if reward.propType == PropType.tinyBoost:
                rewardEnergy += reward.number * 10
            elif reward.propType == PropType.basicBoost:
                rewardEnergy += reward.number * 30
            elif reward.propType == PropType.strongBoost:
                rewardEnergy += reward.number * 100
            elif reward.propType == PropType.spiritGem:
                rewardSpiritGem += reward.number
        data = {'energy': rewardEnergy, 'gem': rewardSpiritGem}
        return data

    def calTotalPoint(self, days, totalEnergy):
        battleCount = roundDown(totalEnergy / self.battleCost)
        dailyBattleCount = roundCeiling(battleCount / days)
        totalPoint = battleCount * self.battlePoint + self.currentPoint
        data = {'totalPoint': totalPoint, 'battleCount': dailyBattleCount}
        return data

    def calNeedEnergy(self, days, totalEnergy):
        needPoint = self.targetPoint - self.currentPoint
        battleCount = roundCeiling(needPoint / self.battlePoint)
        dailyBattleCount = roundCeiling(battleCount / days)
        needEnergy = battleCount * self.battleCost
        gemEnergy = 0
        gem = 0
        if needEnergy > totalEnergy:
            gemEnergy = needEnergy - totalEnergy
        if gemEnergy > 0:
            gem = gemEnergy / 120
            gem = roundCeiling(gem)
            gem = gem * 200
        data = {'energy': gemEnergy, 'gem': gem, 'battleCount': dailyBattleCount}
        return data

    def simulation(self):
        self.output.close()
        self.output = io.StringIO()
        days = self.getDays()
        self.recordMsg('活动持续{}天'.format(days))
        self.recordMsg('已有积分：{}'.format(self.currentPoint))
        self.recordMsg('目标刷取积分：{}'.format(self.targetPoint))
        self.recordMsg('活动副本体力：{}'.format(self.battleCost))
        self.recordMsg('一次活动副本积分：{}'.format(self.battlePoint))
        self.recordMsg('')
        totalEnergy = self.calTotalEnergy(days)
        self.recordMsg('总共可以获取体力：{}'.format(totalEnergy))

        try:
            data = self.calTotalPoint(days, totalEnergy)
            self.recordMsg('如果不碎钻，平均一天可刷{}次活动副本，总积分：{}'.
                           format(data['battleCount'], data['totalPoint']))
            self.recordMsg('')
            data2 = self.calNeedEnergy(days, totalEnergy)
            self.recordMsg('如果刷取到目标积分{}，平均一天需要刷{}次活动副本，除原有体力外仍需{}体力，即{}晶灵石'.
                           format(self.targetPoint, data2['battleCount'], data2['energy'], data2['gem']))
        except:
            print('模拟失败')


    def recordMsg(self, msg: str):
        self.output.seek(0, 2)
        self.output.write(msg + '\n')

    def getDailyEnergy(self):
        dailyEnergy = 12 * 24
        if self.dailyMission:
            dailyEnergy += 30
        if self.xyk:
            dailyEnergy += 60
        if self.dyk:
            dailyEnergy += 100
        if self.coin:
            dailyEnergy -= 50
        if self.holyWater:
            dailyEnergy -= 50
        return dailyEnergy

    def getDays(self):
        days = 0
        if self.startDate is None or self.endDate is None:
            return days
        try:
            days = (self.endDate - self.startDate).days
        except:
            days = 0
        if days < 0:
            days = 0
        return days
