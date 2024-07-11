"""
 Python的super super()的使用
"""
print('------------------------继承-----------------------')
"""
在Python中，当一个类继承另一个类时，它会自动继承以下内容：
    属性（Attributes）：包括类变量（静态变量）和实例变量。类变量是所有实例共享的，而实例变量则是每个实例独有的。
    
    方法（Methods）：包括实例方法、类方法（使用@classmethod装饰器定义）和静态方法（使用@staticmethod装饰器定义）。
        实例方法可以访问实例变量和调用其他实例方法，类方法可以访问类变量和调用其他类方法或静态方法。
        
    构造方法（Initializer/__init__方法）：虽然直接继承父类的__init__方法，但通常需要显式调用父类的构造方法来初始化父类的属性。
        如果不显式调用，父类的__init__将不会被执行，除非使用super()。
        
    特殊方法（Special Methods，如__str__, __repr__, __add__等）：这些方法提供了类的内部操作和表示，如打印字符串表示、相加操作等。
    
    文档字符串（Docstrings）：类和方法的文档字符串不会被直接继承，但可以通过父类的引用查看。
    
    私有成员（Private Members，如以双下划线__开头的成员）：虽然按照约定，私有成员不应被子类直接访问，但Python中没有绝对的私有，
        子类可以通过特定方式访问到这些成员，尽管这样做通常被认为是不好的设计。
        
    异常处理（Exception Handling）：如果父类的方法中包含了异常处理逻辑，子类在调用这些方法时也会间接继承这种异常处理机制。
    
    元类（Metaclasses）：如果父类定义了自己的元类，子类也会继承这个元类，除非子类明确指定了不同的元类。
    
继承的核心目的是复用代码和实现代码的结构化，允许子类在其基础上添加新的功能或覆盖（Override）现有功能，而不必从头开始编写所有代码。
"""
print('------------------------super()-----------------------')
"""
Python 可能不是纯粹的面向对象语言；但是，它拥有使用面向对象设计模式构建软件和应用程序的基础。
    实现这一点的方法之一是使用 super() 方法支持继承。
    与所有语言一样，此方法允许您从派生类本身访问超类的实体。 
——————————————————super() 方法返回对父类实例的引用，您可以使用它来调用基类的方法。————————————————————————
        先在父类里面做基本的功能实现。再用子类去扩展父类的一些功能
    
super()的例子里面引申出了面向对象分析与设计的开闭原则，设计易于维护的容易扩展的类离不开这些原则的渗透和super（）工具提供的便利。
"""
print('---------------------------------------------------')
"""
在Python中，super() 是一个特殊类，它用于调用父类（超类）的方法，特别是在多继承的场景下。
super() 主要用于解决以下问题：
    调用父类方法：当子类覆盖了父类的方法，但又需要在子类中调用父类的实现时，super() 提供了一种优雅的方式。
    处理多继承：在使用多继承时，super() 可以帮助解决方法解析顺序（Method Resolution Order, MRO）问题，按照定义的顺序调用父类的方法。
    避免硬编码父类名：使用 super() 调用方法，避免了直接引用父类名称，增加了代码的可读性和可维护性，因为如果父类名称改变，只需要在一个地方修改。

下面是一个简单的例子来说明 super() 的用法：
"""

print('---------------------------------pythonic 讲解--------------------------------------')


class AA:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"A - {self.name}")


class BB(AA):
    def __init__(self, name):
        super().__init__(name)

    def show(self):
        # super().show()
        print(f"B - * * {self.name}")


bb = BB('Test')
bb.show()
print('--------------------------------------------------------------------')
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
log.addHandler(ch)


class Person:
    def __getattribute__(self, item):
        """
        __getattribute__方法无论是否存在属性都会被调用，如果想访问没有被定义的属性的时候，
        首先或触发__getattribute__的方法，内建的实现发现属性是不存在的话，才会触发__getattr__的方法去执行
        """
        log.debug(f'getting attribute [{item}]')
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        log.debug(f'setting attribute [{key}] to {value}')
        super().__setattr__(key, value)


person = Person()
person.name = 'Setinb'
print(person.name)


class Base:
    def __init__(self):
        print("Base init")


class Derived(Base):
    def __init__(self):
        super().__init__()  # 使用super调用父类的__init__
        print("Derived init")


d = Derived()

"""在这个例子中，Derived 类继承自 Base 类。
    在 Derived 类的构造函数 __init__ 中，我们使用 super().__init__() 来调用 Base 类的构造函数。
    当我们实例化 Derived 类时，首先调用的是 Base 类的 __init__，然后是 Derived 类的 __init__。
    
super() 的调用语法通常是 super(current_class, current_instance), 
    但在 Python 3 中，当在类的方法中使用 super() 时，可以省略参数，因为编译器能自动推断出当前类和实例。
    
注意：
————super() 返回的是一个代理对象，它代表了父类的一个临时实例————————，可以调用父类的方法。
    super() 遵循 MRO（方法解析顺序），这是根据 C3 线性化算法确定的，保证了方法调用的顺序。
    使用 super() 是一种推荐的实践，因为它遵循了Python的“鸭子类型”和“合作原则”，使得代码更加灵活和易于维护

MRO 详解：
MRO（Method Resolution Order，方法解析顺序）是Python中用于解决多继承时方法调用冲突的策略。
    在多继承的类层次结构中，当一个类从多个父类继承并试图调用一个方法时，Python需要确定应该调用哪个父类的方法。MRO决定了这个查找顺序。
    
C3线性化是Python中实现MRO的主要算法，它保证了在多继承时方法调用的线性顺序。
C3线性化的基本规则是：
    每个类都在列表中出现一次。
    如果类B在类A的继承列表中，那么B必须在A之前。
    列表必须是线性的，不能有环。
    Python的__mro__属性可以显示类的方法解析顺序
    
C3线性化算法的基本目标是生成一个线性的顺序，使得每个类只出现一次，
并且满足以下条件：
    自包含性：生成的顺序必须包含所有直接和间接基类。
    子类在前，父类在后：在MRO中，子类总是出现在其父类之前。
    深度优先：在选择两个基类时，总是优先考虑在MRO中较深的路径。
    左到右一致性：如果两个基类在MRO中没有直接的父子关系，那么在它们的继承列表中，先出现的基类应该排在前面。
C3算法通过合并各个基类的MRO，形成一个新的MRO，使得满足上述条件。
    Python中的每个类都有一个__mro__属性，它是一个元组，表示了按照C3线性化计算出的方法解析顺序。

"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):  # D 继承自 B 和 C，B 和 C 都继承自 A
    pass


print(
    D.__mro__)  # 输出: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

"""在这个例子中，D 的 MRO 是 [D, B, C, A, object]，这意味着如果在 D 类中寻找方法，Python会按照这个顺序查找。
super() 函数利用了MRO，当调用 super().some_method() 时，Python会沿着MRO列表找到下一个类的 some_method() 实现。
    这种方式避免了显式地指定父类名称，有助于减少代码耦合，同时遵循了“鸭子类型”和“合作原则”。
    在多继承中，super() 确保了方法调用的一致性和预期行为，使得代码更易于理解和维护。
    
"""

print('-------------------------------多继承-------------------------------------')


class A1:
    pass


class B1(A1):
    pass


class C1(B1):
    pass


class C2(A1):
    pass


class D1(C1, C2):
    pass


D1()
print(D1.__mro__)
"""
(<class '__main__.D1'>, <class '__main__.C1'>, <class '__main__.B1'>, <class '__main__.C2'>, <class '__main__.A1'>, <class 'object'>)
"""
 
"""
总结：
super()，是一个特殊的类，在多继承中，当调用父类的方法时，super()是一个代理对象，即父类的临时对象，可以调用父类的方法。
如何确定super()是哪一个父类的临时对象，根据MRO，MRO是使用的C3线性算法。
"""
