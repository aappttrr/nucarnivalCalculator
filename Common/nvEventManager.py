import enum


class EventType(enum.Enum):
    AttackDamage = '普攻-攻击'
    SkillDamage = '必杀-攻击'
    AttackHeal = '普攻-治疗'
    SkillHeal = '必杀-治疗'
    Dot = '持续伤害'
    Hot = '持续治疗'
    BloodSucking = '吸血'


class Event:
    def __init__(self, arg: EventType):
        self.eventType = arg
        self.data = {}


class EventListener:
    def __init__(self, arg):
        self.name = arg

    def receiveEvent(self, arg: Event):
        pass


class EventManager:
    def __init__(self):
        self.listeners: list[EventListener] = []

    def addListener(self, arg: EventListener):
        if arg not in self.listeners:
            self.listeners.append(arg)

    def removeListener(self, arg: EventListener):
        if arg in self.listeners:
            self.listeners.remove(arg)

    def sendEvent(self, arg: Event):
        for listener in self.listeners:
            listener.receiveEvent(arg)


eventManagerInstance = EventManager()
