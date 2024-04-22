from abc import abstractmethod, ABC


class Player(ABC):
    def __init__(self, name, role):
        self.name = name
        self.role = role

    """
     @abstractmethod 是来自 abc（Abstract Base Classes，抽象基类）模块的一个装饰器，用于标记一个方法为抽象方法。
    在面向对象编程中，抽象方法是一种仅在基类中声明但不提供具体实现的方法，要求继承该基类的子类必须提供其实现。这
    样做有助于定义类的公共接口，并强制子类遵循特定的设计契约。
    """

    @abstractmethod
    def action(self):
        """球员的动作"""

    def __str__(self):
        return f"name={self.name},role={self.role}"


class Forward(Player):

    def action(self):
        print(f"{self.name},带球突破，过后卫凌空抽射！")


class MiddleField(Player):
    def action(self):
        print(f"{self.name},中场球员，长传！")


class DefenseField(Player):
    def action(self):
        print(f"{self.name},后卫，阻止对方前锋进攻！")


class GoalKeeper(Player):
    def action(self):
        print(f"{self.name},我是守门员，我能守住对方的抽射 ！")
