import datetime

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
        self.currentDate: datetime.date = None
        self.tb = 0
        self.bb = 0
        self.sb = 0
        self.xyk = False
        self.dyk = False
        self.coin = False
        self.holyWater = False
        self.battleCost = 30
        self.battlePoint = 100

    def calTotalEnergy(self, days):
        dailyEnergy = self.getDailyEnergy()
        totalEnergy = dailyEnergy * days
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

    def calTotalPoint(self, days):
        totalEnergy = self.calTotalEnergy(days)
        battleCount = roundDown(totalEnergy / self.battleCost)
        dailyBattleCount = roundCeiling(battleCount / days)
        totalPoint = battleCount * self.battlePoint + self.currentPoint
        data = {'totalPoint': totalPoint, 'battleCount': dailyBattleCount}
        return data

    def calNeedEnergy(self, days):
        totalEnergy = self.calTotalEnergy(days)

        needPoint = self.targetPoint - self.currentPoint
        battleCount = roundCeiling(needPoint / self.battlePoint)
        dailyBattleCount = roundCeiling(battleCount / days)
        needEnergy = battleCount * self.battleCost
        gemEnergy = 0
        gem = 0
        if needEnergy > totalEnergy:
            gemEnergy = needEnergy - totalEnergy
        if gemEnergy > 0:
            gem = gemEnergy * 5 / 3
        data = {'energy': gemEnergy, 'gem': gem, 'battleCount': dailyBattleCount}
        return data

    def cal(self):
        days = self.getDays()
        if days <= 0:
            return False
        print('活动持续{}天'.format(days))
        if self.currentDate > 0:
            print('目前有{}积分'.format(self.currentPoint))

        dailyEnergy = self.getDailyEnergy()
        needPoint = self.targetPoint - self.currentPoint
        totalEnergy = dailyEnergy * days
        totalEnergy += self.tb * 10
        totalEnergy += self.bb * 30
        totalEnergy += self.sb * 100
        print('日常可用于刷取活动的体力为：{}')
        print('额外有微型日月精华{}个，初级日月精华{}个，上级日月精华{}个'.format(self.tb, self.bb, self.sb))
        print('总共可使用的体力为：{}'.format(totalEnergy))
        print('')

        battleCount1 = roundDown(totalEnergy / self.battleCost)
        dailyBattleCount1 = roundCeiling(battleCount1 / days)
        totalPoint = battleCount1 * self.battlePoint + self.currentPoint

        print('不额外获取体力的情况，按照可用体力，一共能刷积分：{}'.format(totalPoint))
        print('每天需要刷{}次，如果每天刷次数小于10可能会无法完成日常任务（日常任务提供30体力）'.format(dailyBattleCount1))

        battleCount2 = roundCeiling(needPoint / self.battlePoint)
        dailyBattleCount2 = roundCeiling(battleCount2 / days)
        needEnergy = battleCount2 * self.battleCost
        gemEnergy = 0
        gem = 0
        if needEnergy > totalEnergy:
            gemEnergy = needEnergy - totalEnergy
        if gemEnergy > 0:
            gem = gemEnergy * 5 / 3

        print('如果需要刷到目标积分{}，则需要额外使用{}体力，共需要{}晶灵石兑换体力'.
              format(self.targetPoint, gemEnergy, gem))
        print('每天需要刷{}次，如果每天刷次数小于10可能会无法完成日常任务（日常任务提供30体力）'.format(dailyBattleCount2))

    def getDailyEnergy(self):
        dailyEnergy = 12 * 24
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
            if self.currentDate is not None and self.currentDate < self.endDate:
                days = (self.endDate - self.currentDate).days
            else:
                if self.startDate < self.endDate:
                    days = (self.endDate - self.startDate).days
        except:
            days = 0
        return days
