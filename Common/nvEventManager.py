import enum


class EventType(enum.Enum):
    attack = '普攻'
    attackDamage = '普攻-攻击'
    attackFollowUp = '普攻-追击'
    attackHeal = '普攻-治疗'
    skill = '必杀'
    skillDamage = '必杀-攻击'
    skillFollowUp = '必杀-追击'
    skillHeal = '必杀-治疗'
    dot = '持续伤害'
    hot = '持续治疗'
    bloodSucking = '吸血'
    counter = '反击'
    shield = '护盾'
    defense = '防御'


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
