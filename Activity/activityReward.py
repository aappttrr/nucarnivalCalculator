from Props.propTypeEnum import PropType


class ActivityReward:
    def __init__(self, _pt: PropType, _num: int, _p: int):
        self.propType: PropType = _pt
        self.number: int = _num
        self.point: int = _p
