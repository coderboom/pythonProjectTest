"""类属性的public vs private"""

"""Python并没有像其他的编程语言如Java/C#等一样有类的公有属性和私有属性的约束访问的概念。
我们只能遵循PEP-8的规范在代码的Style上做出约束。
    这就要求我们在对Python进行类的设计的时候，要考虑到加_前缀作为所以有变量的提示，__作为保护属性的提示，让Python的开发人员在这种约定下进行合作。
    看到非公有的方法或属性就不要去访问和互动。这样才能保证Python代码的高可维护性。

另外，也从子类继承父类的角度上分析了如何使用这些特性。
当然，类的设计是很考量设计者的思想和经验的，要遵循面向对象的设计思想来设计类才能够让设计出来的类更具可读性、可扩展性与可维护性。
"""


class A:
    def __init__(self, g=2.0):
        self._a = 1.5
        self.__g = g

    def get_g(self):
        return self.__g

    def get_a(self):
        return self._a

    def get_ag(self):
        return self.get_a() * self.get_g()


a = A()
print(a.get_g())
print(a.get_a())
print(a.get_ag())
print('--------------')
# print(a._a) # 不推荐这样访问，但是能访问到private属性
# print(a.__g) # 对双下划线的属性不推荐这样访问，用这种方法也访问不到
print(a.__dict__)  # {'_a': 1.5, '_A__g': 2.0}
print(a._A__g)  # 2.0  对于双下划线属性，不推荐访问，但可以这样访问到
print('--------------')


class B(A):
    def __init__(self, g=32):
        super().__init__()
        self.__g = g

    def calc(self):
        return self.__g

    def calc_from_parent(self):
        return self.get_g()


b = B()
print(b.calc())  # 32 继承类A的__g 属性，但有重新赋值，所以这里是覆盖类__g的值
print(b.calc_from_parent())  # 2.0

"""A 类有两个属性：_a 和 __g。_a 是单下划线属性，虽然不是严格私有的，但通常表示不希望外部直接访问。__g 是双下划线属性，Python 会对其进行名称修饰，使其在类的实例字典中以 _A__g 的形式存在，从而限制外部直接访问。
B 类在 __init__ 方法中通过 super().__init__(g=32) 调用 A 类的构造方法，传入了一个新的 g 值 32。A 类的构造方法会将这个值赋给 self.__g。
然后，B 类的 __init__ 方法中，又直接设置了 self.__g = g，这里的 g 是 32。这就覆盖了 A 类中 __g 的值，因为 self.__g 在 B 类中重新定义了。
B 类的 calc 方法返回 self.__g，这是 B 类中定义的新 __g 值，也就是 32。
calc_from_parent 方法调用 self.get_g()，这会返回 A 类中 get_g 方法的结果。由于 A 类的 get_g 方法返回的是 self.__g（即 A 类实例字典中的 _A__g），这个值在 A 类的构造方法中被初始化为 2.0。

所以，当你创建 B 类的实例 b 并调用 calc 方法时，它返回的是 B 类中的 __g 值 32。而 calc_from_parent 方法调用 get_g 返回的是 A 类中的 __g 值 2.0。因此，B 类并没有继承 A 类的 __g，而是覆盖了它。
"""


class B1(A):
    def __init__(self, g=32):
        super().__init__()
        self.__g = g

    def calc(self):
        return self.__g

    def get_g(self):
        return self.__g

    def calc_from_parent(self):
        return self.get_g()


b = B1()
print(b.calc())  # 32
print(b.calc_from_parent())  # 32  覆盖类A类的get_g()方法，返回的是B1的 __g 属性

"""
重点：继承中，子类尽量不要去更改父类的一些受保护的属性（private和受保护属性）
"""


class B1(A):
    def __init__(self, g=32):
        super().__init__(g)

    def calc(self):
        return self.get_g()  # 通过接口访问属性，不要直接访问


b = B1()
print(b.calc())  # 32
print(b.__dict__)  # {'_a': 1.5, '_A__g': 32}
