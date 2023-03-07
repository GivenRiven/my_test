from typing import Optional
# _instance: Optional[type] = None
#
#     def __call__(self, *args, **kwargs):
#         if self._instance is None:
#             self._instance = super(MetaSingleton, self).__call__(*args, **kwargs)
#         return self._instance
#
# class BaseClass:
#     field = 5
#
# class Singleton(BaseClass, MetaSingleton):
#     pass
#
# a = Singleton()
# print(a)
# b = Singleton()
# print(a == b)


class Robot:
    def __init__(self):
        self.legs = None
        self.flying = None
        self.hands = None
        self.travrsal = []
        self.detect_system = []
    def __str__(self):
        string = ''
        if self.legs:
            string += 'рообот может ходить'
        if self.flying:
            string += 'рообот может летать'
        if self.hands:
            string += 'рообот может хватать'


        if self.travrsal:
            for i in self.travrsal:
                string += i + '\n'
        if self.detect_system:
            for i in self.detect_system:
                string += '  ' + str(i) + '\n'
        return string

class Legs:
    def __str__(self):
        return f'Крылья'
class Hands:
    def __str__(self):
        return f'Руки'

class RobotBuilder(ABC):
    @abstractmethod
    def __init__(self):
        self.product = Robot()

    @abstractmethod
    def reset(self):
        self.product = Robot()
    @abstractmethod
    def build_system(self):
        pass

class RobortFly(RobotBuilder):
    def __init__(self):
        super(RobotFly, self).__init__()
    def reset(self):
        super(RobotFly, self).reset()
    def build_system(self, *args):
        self.product.detect_system.append(Flying())
        self.product.detect_system.append(Hands())
        self.product.flying = True
        self.product.hands = True
robot_fly = RobotFly()
print(robot_fly)



