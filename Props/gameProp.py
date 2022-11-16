from Props.propTypeEnum import PropType


class GameProp:
    def __init__(self, _propType: PropType, _number):
        self.propType: PropType = _propType
        self.number = _number


