"""在Python中，self 是一个指向对象实例本身的引用。当你在一个类的内部定义方法时，通常需要将 self 作为第一个参数。
    这个约定是Python面向对象编程中的标准做法"""


class MyClass:
    __CLASS = 'abcdefg'
    # 私有变量只能在类内部使用，不能在类外部访问或直接访问，但可以使用，对象名._类名__私有属性名来访问私有属性，
    # 当然，要尊所私有属性不能在类外部访问或这届调用的约定
    score = 100

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")


# 创建类的一个实例
instance = MyClass("Alice")
# 调用实例的方法
instance.say_hello()  # 输出: Hello, my name is Alice.

print(dir(MyClass))
# print(MyClass.__CLASS) # 无法访问类的私有变量
print(MyClass._MyClass__CLASS)  # 可以访问类的私有变量；输出: abcdefg
print(MyClass.score)
print(instance.__dict__)  # 查看类的属性，是一个字典
print(instance.__doc__)  # 类的文档字符串
print(instance.__class__)  # 类名
print(instance.__module__)  # 类定义所在的模块

"""在 __init__ 方法中，self 引用了正在初始化的新创建的对象实例，并且通过 self.name = name 给实例添加了一个属性。
    在 say_hello 方法中，self 同样引用了调用该方法的对象实例，因此它可以访问并修改实例的属性（如上面示例中的 name）。
    简而言之，self 的作用在于允许方法内部能够直接操作和访问类的实例变量。尽管名为 self，但程序员也可以选择其他任何名称，
    只要在方法定义中保持一致即可，但是为了代码可读性和一致性，通常推荐使用 self 这个约定俗成的名称。

self 
self代表类的实例，而非类；self 就是 对象/实例 属性集合,可以看成是一个字典，self只存储属性，没有动作。
self 看似是整个对象，实际上清楚地描述了类就是产生对象的过程，描述了 self 就是得到了 对象，所以 self 内的键值可以直接使用。
正如自然界中一个有效的对象，必须包括：1、描述对象的属性；2、对象的方法。所以 self是必须的，也是对象中重要的特性。
"""
print('22222222222222222222222222222222222222222222222222222222222222222222222222')
"""python 中一些特殊的实例变量：

私有变量(private),只有内部可以访问，外部不能访问，私有变量是在名称前以两个下划线开头，如：__name，其实私有变量也不是完全不能被外部访问。
在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
"""
print('-----------------------------')
"""对象的属性：
对象属性是指与特定对象实例关联的变量。每个对象实例都有自己独立的一份属性值。
在Python中，当你创建一个类的实例时，通过__init__方法或其他方式给实例添加的属性就是对象属性。
对象属性通常存储在实例内部，可通过self关键字来引用。
例如，在以下代码中，name 和 age 是Person类实例的对象属性：
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 25)
# 这里的 "Alice" 和 25 是 p1 这个对象实例的属性

类的属性：
类属性则是属于整个类级别的变量，而不是任何一个特定的类实例。
所有该类的实例都共享这个类属性，且修改类属性会影响到所有实例。
类属性通常定义在类的内部，但不在任何方法内，也不需要通过self引用。
使用@classmethod或@staticmethod装饰器定义的方法也可以访问和修改类属性。
例如，在以下代码中，species 是Animal类的一个类属性：

class Animal:
    species = "Mammal"  # 这是一个类属性

    def __init__(self, name):
        self.name = name

a1 = Animal("Dog")
a2 = Animal("Cat")

print(Animal.species)  # 输出 "Mammal"
print(a1.species)       # 同样输出 "Mammal"
print(a2.species)       # 同样输出 "Mammal"

# 更改类属性会影响所有实例
Animal.species = "Vertebrate"
print(a1.species)  # 现在输出 "Vertebrate"

"""
print('-----------------------------')

"""
继承
类的继承会“继承”所有的属性和方法，无论它们是否被声明为私有（以双下划线 __ 开头）。然而，私有属性和方法虽然可以被继承，但并不推荐直接在子类中访问或修改。
Python中的私有属性（如 __private_attr）并不是真正意义上的私有，而是采用了名称修饰（name mangling），即在类内部将其名字更改为 _ClassName__private_attr 的形式。
这一机制使得外部代码很难直接访问这些属性，从而起到一种封装的作用，防止意外篡改。
对于子类来说，由于它也是父类的一部分，因此子类的方法仍然可以通过这种修饰后的名称来访问父类的私有属性，但这被认为是违反了私有属性的设计初衷。
通常情况下，设计良好的类结构应该通过公共接口（如公共方法）与父类进行交互，而不是依赖于私有成员的直接访问。

def __private_attr(self,*args,**kwargs):  私有方法（不被继承）
注：可以通过对象名._类名__私有方法名来访问私有属性
"""


class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print('员工：{},员工编号：{}'.format(self.name, self.id))


class FullEmployee(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def monthly_salary(self):
        print('正式员工：{},员工编号：{}，月薪：{}'.format(self.name, self.id, self.salary))


class DailyEmployee(Employee):
    def __init__(self, name, id, day, d_salary):
        super().__init__(name, id)
        self.day = day
        self.salary = d_salary

    def monthly_salary(self):
        print('日结员工：{},员工编号：{}，月薪：{}'.format(self.name, self.id, self.day * self.salary))


fe = FullEmployee('张三', 1002, 10000)
de = DailyEmployee('李四', 10003, 12, 150)

print(fe)
print(de)
fe.print_info()
de.print_info()
fe.monthly_salary()
de.monthly_salary()
print(DailyEmployee.mro())  # 查看类的继承顺序(继承链)
"""---为什么调用父类的实例化函数可以实例自己
当你在一个子类的__init__方法中调用父类的实例化函数（如super().__init__(...)），实际上是在初始化子类对象的同时也初始化了父类的部分。
    这是因为子类继承了父类的所有属性和方法，而一个完整的子类实例应当包含从父类继承来的所有状态。

在上面两个继承中，当创建 FullEmployee 类的一个实例时，首先会通过 super().__init__(name, id) 调用 Employee 类的 __init__ 方法来初始化 name 和 id 属性，
然后再初始化子类特有的 salary 属性。
————这样就确保了一个 FullEmployee 对象既包含了作为员工的基本信息，又添加了正式员工独有的月薪信息，从而构建了一个完整的子类实例。

实际上，类并不直接继承实例属性。在面向对象编程（OOP）中，子类会继承父类的类属性和方法，而不是实例属性。
    这是因为类定义的是一个蓝图或模板，用于创建具有相同属性和行为的对象实例。
当子类通过 super().__init__(...) 调用父类的构造函数时，实际上是执行了父类构造函数内的逻辑来初始化子类实例的部分状态。
    这样，子类实例就获得了与父类相同的实例属性，但这并不是“继承”实例属性的概念，而是基于父类构造函数为每个新创建的子类实例提供了初始值。

"""
print('------------------------')
"""重点：super() 函数在子类继承父类实例属性中的作用是帮助子类完成对父类属性的初始化，
    并维护了继承层次结构中的方法调用顺序，使得子类能够充分利用父类的构造过程来设置共有的或默认的属性。
"""
print('------------------------')
"""super()函数
super([type[, object-or-type]])

当不带参数时，super() 会返回一个代理对象，它会根据当前类的 MRO（Method Resolution Order，方法解析顺序）查找下一个类，并委托给该类的方法。
    如果提供了类型参数（如 super(Child, self)），self 是子类实例，那么它会找到 self 类型对应的父类（即 Child 的直接父类）并获取其方法。
MRO（方法解析顺序）：
    在多重继承中，Python 使用 C3 线性化算法来决定方法和属性的查找顺序，这个顺序就是 MRO。当使用 super() 时，它会按照 MRO 列表中的顺序寻找下一个类。
    每个类都有一个隐含的 __mro__ 属性，它是一个元组，表示了类及其所有父类的查找顺序。
用途：
调用父类方法：在子类重写父类方法时，若想先执行父类方法再进行额外操作，可以使用 super() 来调用父类方法，例如：
"""

"""类方法classmethod

定义： 类方法通过 @classmethod 装饰器进行标记。
    其定义通常包含一个特殊的第一个参数 cls，而不是常见的实例方法中的 self。
    cls 参数表示调用该方法时所对应的类对象
"""


class Employee:
    employees_count = 0

    @classmethod
    def create_employee(cls, name, id):
        cls.employees_count += 1
        # 在这里，cls 是 Employee 类的一个引用
        return cls(name, id)  # 这行代码创建了一个 Employee 类的新实例---返回一个实例

    def __init__(self, name, id):
        self.name = name
        self.id = id


# 创建员工并增加员工计数
new_employee = Employee.create_employee('张三', 1001)  # 可以通过类方法创建实例对象
print(Employee.employees_count)  # 输出：1
"""create_employee 是一个类方法，它可以访问和修改类级别的变量 employees_count，并且不需要任何已存在的实例就能工作。
"""
print(new_employee.name, '\n', new_employee.id)

"""静态方法 staticmethod()
    静态方法（staticmethod）是一种特殊的方法类型，它不与类或类的实例绑定，其定义和调用方式与普通函数非常相似。
    通过 @staticmethod 装饰器来标记一个方法为静态方法。

1、定义
    静态方法不需要任何特殊的第一个参数，不像类方法那样有 cls 或者实例方法中的 self    
"""


class MyClass:
    @staticmethod
    def static_method(arg1, arg2):
        # 这里没有 self 或 cls 参数
        # 只处理传入的参数，并根据这些参数执行相关逻辑
        pass


"""
调用方式：
    静态方法同样可以通过类名直接调用：MyClass.static_method(value1, value2)
    同样也可以通过类的实例来调用：instance = MyClass(); instance.static_method(value1, value2)
    不论如何调用，---静态方法内部都无法访问到类属性或实例属性---，因为它们并不知道哪个类或实例正在调用它。
用途：
    静态方法主要适用于那些仅仅依赖于传入参数而无需访问类或实例状态的方法。
    它们作为类的一部分组织代码，但其实质上是---独立于类存在的纯函数---，通常用于实现一些工具性或者辅助性的功能，这些功能与类的具体实例无关。
    由于静态方法不会自动接收类或实例的引用，所以它们不能用来操作类或实例的属性
"""

"""特殊方法
这些方法在类定义中提供了对Python内置操作符和其他语言结构的自定义支持，允许开发者改变对象的行为。
特殊方法（魔术方法）与内置函数的对应关系如下：
__init__(self, ...):
对应于创建对象时自动调用的过程，而非直接对应的内置函数。

__str__(self):
对应于内置函数 str(), 当调用 str() 函数或者在交互式环境中打印对象时使用。

__repr__(self):
对应于内置函数 repr(), 用于生成一个代表该对象的字符串，通常用于调试和开发环境。当对象被直接输出到解释器或使用 print(repr(obj)) 时调用。

__add__(self, other):
对应于加法运算符 +，如：a + b。

__len__(self):
对应于内置函数 len(), 如：len(obj)。

__call__(self, *args, **kwargs):
允许实例像函数一样被调用，无直接对应的内置函数，但可以理解为对象能“响应”圆括号 ()。

其他例子：
__getitem__(self, key) 对应于索引操作，如：obj[key]。
__setitem__(self, key, value) 对应于赋值操作，如：obj[key] = value。
__delitem__(self, key) 对应于删除操作，如：del obj[key]。
__iter__(self) 和 __next__(self) 定义了迭代器协议，使类能够通过 for item in obj: 进行迭代。
__eq__(self, other) 定义了等于运算符 == 的行为。
这些特殊方法使得开发者能够在自定义类中重载或定制Python中的基本操作符和内置函数的行为

"""
print('------------------------')
"""__new__() 和 __init__()

__new__(cls, [...])：
    这是一个类方法（即使没有被显式声明为@classmethod），它会在实例创建阶段首先被调用。
    主要任务是负责创建一个新的实例，并返回这个实例。它是类级别的方法，因为它处理的是类到实例的转换过程。
    在这里，cls 参数代表当前要实例化的类，而其他参数则用于传递给实例化过程中所需的任何额外信息。
    如果需要控制实例的创建过程（例如单例模式、自定义实例类型等），通常会重写 __new__() 方法。
    __new__() 的默认实现通常会调用超类的 __new__() 方法来创建实例，然后返回这个新创建的对象。
__init__(self, [...])：
    这是一个实例方法，在 __new__() 创建并返回一个实例之后被调用。
    它的主要任务是对新创建的实例进行初始化，设置初始状态或属性。
    self 参数就是由 __new__() 刚刚创建并返回的那个实例。
    在这里可以执行一些针对实例数据成员的初始化操作，如设置默认值、绑定事件处理函数、建立与其他对象的关系等。
    不管是否重写了 __new__() 方法，只要成功创建了实例，__init__() 方法都会被调用。
总结一下，__new__() 负责生成实例本身，而 __init__() 负责对生成的实例进行初始化。
    如果只想控制实例的创建过程而不改变其初始化行为，只需重写 __new__()；
    如果只是想定制实例的初始状态，则只需重写 __init__()。
    在某些情况下，可能需要同时重写这两个方法以满足特定的需求。
"""


class Point:
    total_instance = 0
    MAX_INSTANCE = 2

    def __new__(cls, *args, **kwargs):
        if cls.total_instance >= cls.MAX_INSTANCE:
            print('实例数量超过限制')
            return None
        cls.total_instance += 1
        # return super().__new__(cls)
        return object.__new__(cls)

    # super().__new__(cls) 和 object.__new__(cls) 都用于创建新实例，但在多继承或类层次结构较复杂的情况下，它们之间存在一定的区别：
    # super().__new__(cls, *args, **kwargs)：
    #     这个方式会调用当前类的MRO（Method Resolution Order，方法解析顺序）中的下一个类的 __new__() 方法。
    #     如果 Point 类是从其他基类继承而来的，并且这些基类也重写了 __new__()，那么 super().__new__() 将会沿着MRO链找到最近的一个具有 __new__() 方法的父类并调用它。
    #     使用 super() 可以确保即使在复杂的继承结构下也能正确地执行类方法的调用顺序。
    # object.__new__(cls)：
    #     直接调用 object 类的 __new__() 方法来创建实例。
    #     不考虑任何可能存在的中间父类，无论 Point 是否有其他父类以及这些父类是否重写了 __new__() 方法，这里都会直接调用最底层的基类 object 的 __new__() 方法来创建对象。
    #     在没有涉及多重继承或者所有父类都没有自定义 __new__() 方法的情况下，super().__new__() 与 object.__new__() 的效果是相同的，它们都将创建一个空的实例对象。
    # 在这个具体的上下文中，因为 Point 类并没有显式指定继承自其他类，所以 Python 默认将其视为继承自 object。
    #     因此，在这个例子中，两种写法在功能上是一致的，都会调用 object 的 __new__() 方法创建一个新的实例。
    #     然而在更复杂的类继承结构中，选择使用 super() 通常更为通用和灵活。

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_total_instance(cls):
        print('当前实例数量：', '\n', cls.total_instance)


a = Point(1, 2)
a.get_total_instance(Point)
Point.get_total_instance(Point)
print('----------------')
b = Point(3, 4)
b.get_total_instance(Point)
Point.get_total_instance(Point)
print('----------------')
c = Point(5, 6)
# c.get_total_instance(Point)
Point.get_total_instance(Point)

"""多继承
Method Resolution Order (MRO) 是 Python 中用于确定类的方法查找顺序的机制。在多继承的情况下，
    当一个类有多个父类，并且这些父类中可能存在同名方法时，Python 需要一种规则来决定应该调用哪个父类的方法。MRO 就是用来解决这个问题的一种线性顺序。
Python 的 MRO 确保了以下两个原则：
    单调性（Monotonicity）：如果 A 是 B 的子类，那么在任何类 C 的 MRO 中，A 都会出现在 B 之前。
    本地优先级（C3 Linearization）：对于类 X 继承自 A, B, ...等多个父类的情况，如果 A 和 B 同时定义了一个方法，
    并且 X 没有重写这个方法，那么在寻找该方法时，X 的实例会先调用距离 X 更近的那个父类的方法（即在继承树上更靠近 X 的父类）。
    Python 2.x 使用经典类时，默认采用深度优先搜索（DFS）的方式进行方法解析，这可能会导致不一致的行为和难以预料的结果。
    从 Python 2.3 开始引入了新式类（也称类型对象或面向对象编程中的类），并使用 C3 线性化算法来确保 MRO 符合上述原则，以实现直观、一致和可预测的方法查找顺序。
    在 Python 中，可以通过查看类的 __mro__ 属性来获取其 MRO 序列。例如，假设有一个类定义如下：

下面的例子打印出：
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

这意味着当在 C 类中查找一个方法时，Python 会按照 C -> A -> B -> object 的顺序依次查找。
    如果某个方法在 A 中找到，则不会继续查找 B 或 object 中的同名方法
"""


class A:
    pass


class B:
    pass


class C(A, B):
    pass


print(C.__mro__)
print('----------------')

"""object()
在Python中，object() 是一个特殊构造函数，用于创建一个空的、最基础的对象实例。object 类是所有类的基类，
    在Python 3.x版本中，无论是否明确继承，所有自定义类都隐式地继承自 object 类。
基础概念：
    object 类本身包含了Python中所有对象的基本操作和属性。
    它定义了一些特殊方法（如 __new__, __init__, __del__, __str__, __repr__, 等等），这些方法构成了Python面向对象编程的基础。
使用 object() 函数：
"""
instance = object()
"""上述代码会创建一个 object 类的实例。这个实例没有任何附加的属性或方法，它是最纯粹的对象形式。
内置方法：
创建的 object 实例默认具有以下一些方法：
    __str__: 当调用 str(instance) 或者在交互式环境中打印实例时返回一个表示该对象的字符串。
    __repr__: 当调用 repr(instance) 或在交互式环境中直接输入实例名时返回一个代表该对象的可读字符串，通常用于调试和复制对象。
    __hash__: 提供对象的哈希值，使其可用于字典或其他需要哈希功能的数据结构中。
    其他魔术方法涉及对象生命周期管理（如初始化、清理）、比较、类型转换等。
继承与多态：
    所有自定义类都会继承 object 类的方法，如果在子类中没有重写这些方法，则调用时将执行 object 类中的相应实现。
    这种设计确保了语言的一致性，并且允许程序员通过覆盖基类方法来实现多态行为。
示例：
"""


class MyClass:
    pass


my_instance = MyClass()  # 即使 MyClass 没有显示继承 object，它也隐式继承了 object 的所有特性
print(isinstance(my_instance, object))  # 输出: True

"""python 中任何对象的都有可能指向内存中的同一个对象，但object()的实例除外。"""
x = object()
b = object()
print(x == b, '\n', x is b)  # 输出: False False
# 基于以上特征，可以利用object对象代替缺失值做哨兵
mydict = {'a': None}
if mydict.get('a', None) is None:
    print('a is not defined')
else:
    print('a is defined')

MISSING = object()
if mydict.get('a', MISSING) is MISSING:
    print('a is not defined')
else:
    print('a is defined')

"""type()
1 type() 函数在 Python 中的主要用法是用于获取变量或表达式的类型。它可以接受一个参数，并返回该参数的类型（即类或类型对象）
2 创建新类型（元类使用）： type() 可以作为元类（metaclass）来动态地创建新的类。
    它需要三个参数：类名、基类列表和类字典（包含类的方法和属性）。
"""
SimpleClass = type('SimpleClass', (object,), {'method': lambda self: 'Called method'})
instance = SimpleClass()
print(instance.method())  # 输出: Called method
print(type(SimpleClass))  # 输出: <class 'type'>

"""
hasatter(obj,name): 检测是否指定的对象属性
getatter(object,name[,default])：获取对象属性
setatter(obj,name,value): 设置对象属性
delatter(obj,name): 删除对象属性

以上函数可以操作实例的属性和方法，也能操作类的属性。
"""
print('-------------------')
"""
partialmethod() 函数是 Python 中的 functools 模块提供的一个工具，类似于 functools.partial()，但专门用于方法。
    它允许你预先固定部分方法参数，并创建一个新的可调用对象。
基本用法
"""
from functools import partialmethod


class MyClass:
    def my_method(self, arg1, arg2=None):
        print(f"arg1: {arg1}, arg2: {arg2}")

    def test_method(self, arg1, arg2, arg3='every day'):
        print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")


# 部分参数预设
MyClass.fixed_method = partialmethod(MyClass.my_method, arg1="fixed_value")

# 创建实例并调用预设方法
obj = MyClass()
obj.fixed_method(arg2="variable_value")  # 输出: arg1: fixed_value, arg2: variable_value

MyClass.test_method_arg2 = partialmethod(MyClass.test_method, arg2='variable_value')
test_obj = MyClass()
test_obj.test_method_arg2(123)
"""partialmethod() 返回的对象保持了原方法的绑定特性（即在类或实例上调用时会自动将 self 或者 cls 作为第一个参数传入）。
可以用于减少重复代码或者创建具有默认值的方法变体，提高代码的灵活性和重用性。
"""

"""@property装饰器
@property 装饰器用于将一个方法转换为属性调用的形式，提供对对象私有属性的间接访问。
    通过这种方式，可以控制对对象属性的读取（getter）和写入（setter）、删除（deleter），甚至添加验证逻辑等操作
"""


class Person:
    def __init__(self, name):
        self._name = name

    @property  # 实质是getter 方法，通过 @property 装饰器转换为属性
    def name(self):
        return self._name.title()  # 返回姓名，并进行了首字母大写的格式化处理

    @name.setter  # setter 方法，与 @property 结合使用，定义如何设置属性值
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('Name must be a string.')
        self._name = value.title()

    @name.deleter  # deleter 方法，与 @property 结合使用，定义如何删除属性
    def name(self):
        print('Name deleted.')
        self._name = None


p = Person('john')
print(p.name)  # 输出: John
p.name = 'bob'
print(p.name)  # 输出: Bob
# p.name = 123  # ValueError: Name must be a string.

"""我们创建了一个 Person 类，其中有一个名为 _name 的私有属性。
    我们通过 @property 装饰器创建了一个公有属性 name，它实际上是一个getter方法。
    同时，我们还定义了对应的setter和deleter方法，这样用户在访问或修改_name属性时，
    就可以受到我们设定的规则约束和执行特定的操作
"""
print('-------------------')

"""@cached_property 缓存属性
@cached_property 是一个装饰器，用于将类的方法转换为只计算一次的属性。
    首次访问该属性时，它会调用被装饰的方法来计算属性值，并将结果缓存到实例中，
    后续对该属性的访问直接返回缓存的值，从而避免了重复计算带来的性能开销
在Python中，@cached_property 可以是第三方库提供的装饰器（如 Django 中的 django.utils.functional.cached_property），
    也可以是自定义实现的装饰器
"""
from functools import cached_property


class cached_property1:  # 自定义装饰器（属性装饰器）
    def __init__(self, func):
        self.func = func
        self.__doc__ = func.__doc__  # 同时，为了保持文档字符串和方法名的一致性，从原函数获取并存储了 __doc__ 和 __name__ 属性。
        self.name = func.__name__

    def __get__(self, instance,
                owner):  # 当通过类或其实例访问属性时，Python会调用描述符的 __get__ 方法，并传入对应的实例和该实例所属的类作为 instance 和 owner 参数。
        if instance is None:
            return self
        else:
            value = instance.__dict__.get(self.name, None)
            if value is None:
                value = self.func(instance)
                instance.__dict__[self.name] = value
            return value


"""这段代码实现了一个名为 cached_property 的类装饰器，它用于将一个实例方法转换为只计算一次的属性。这个装饰器适用于那些计算代价较高但结果不随时间改变的属性方法。
cached_property 类的工作原理如下：
初始化（init）：
当使用 @cached_property 装饰器时，会创建一个 cached_property 类的实例，并将被装饰的方法作为 func 参数传递。
同时，为了保持文档字符串和方法名的一致性，从原函数获取并存储了 __doc__ 和 __name__ 属性。
descriptor协议的 get 方法：
    通过定义 __get__ 方法，该类遵循了Python的描述符协议（descriptor protocol），使得当访问装饰后的实例属性时，会调用此方法。
        这里的“实例”是指 cached_property 装饰器修饰的类（例如上面示例中的 MyClass）的实例。
            具体来说，当创建了 MyClass 的一个对象（如 obj = MyClass()），并尝试访问其经过 @cached_property 装饰的方法（如 obj.expensive_computation）时，
            Python解释器会触发 cached_property 类中定义的 __get__ 方法。
            这是因为通过实现描述符协议，特别是定义了 __get__ 方法，Python将自动处理对装饰后属性的访问，并根据 __get__ 方法来获取和/或计算该属性的值。
            在这个例子中，每次访问 expensive_computation 属性时都会检查是否已经缓存了结果，如果没有，则执行耗时的计算操作并将结果缓存起来。
            
    如果访问属性时没有提供实例（即 instance is None，通常发生在类级别而非实例级别），则直接返回 self，这有助于在类上调用时保持一致的行为。
    若提供了实例，则首先尝试从实例的 __dict__ 中获取已缓存的结果。
    若未找到已缓存的结果（即 value is None），则执行原始函数（这里为 expensive_computation），并将计算得到的结果保存到实例的 __dict__ 中。
    最后，无论结果是否已经存在缓存中，都返回对应的值。
使用示例：
    在 MyClass 中，expensive_computation 方法被 cached_property 装饰器修饰，因此每次访问该属性时，都会根据上述逻辑决定是否重新计算或从缓存中获取结果。
    第一次访问 obj.expensive_computation 时，由于缓存中无值，会触发 "Computing..." 输出并计算结果，然后将结果缓存至 obj.__dict__ 中。
    第二次及后续访问时，由于已经有缓存的结果，因此不再重新计算，而是直接从缓存中取出结果返回。
"""


# 使用示例
class MyClass:
    @cached_property1  # 当使用 @cached_property 装饰器时，会创建一个 cached_property 类的实例，并将被装饰的方法作为 func 参数传递。
    def expensive_computation(self):
        # 这里执行耗时的计算操作
        print("Computing...")
        return 42  # 计算得到的结果


obj = MyClass()
print(obj.__dict__)
print(obj.expensive_computation)  # 第一次访问，触发计算并缓存结果
print(obj.__dict__)
print(obj.expensive_computation)  # 第二次及以后访问，直接从缓存获取结果
print(obj.__dict__)

"""Python 描述符协议是面向对象编程中的一种机制，它允许定义类属性的行为，尤其是当这些属性被获取、设置或删除时。
    描述符是一个实现了以下至少一个特殊方法的类：
__get__(self, instance, owner)
self：
    这是指向当前描述符对象自身的引用，在这个例子中就是 cached_property 类的一个实例
instance：
    如果 __get__ 是在一个实例属性上调用，则 instance 参数将传入该属性所属的对象实例。
    如果 __get__ 是直接在类上被调用（例如 MyClass.expensive_computation），则 instance 参数将是 None。
owner：
    这个参数代表的是拥有此属性的类，即 __get__ 方法被调用时属性所在的类的引用。在上述示例中，
    当访问 obj.expensive_computation 时，owner 将是 MyClass 类本身。   
    
当描述符关联的属性通过实例或类访问时调用。
instance 是拥有该属性的实例，如果通过类直接访问，则为 None。
owner 是包含描述符的类。
    
__set__(self, instance, value)
    当尝试给描述符关联的属性赋值时调用。
    它负责设置存储在 instance 上的实际值。
__delete__(self, instance)
    当尝试删除描述符关联的属性时调用。
    实现这个方法以控制删除属性的行为。
    描述符通常用于实现数据验证、计算属性、代理（proxies）或其他高级属性行为，例如 Python 中的 property 类型就是一个内置的描述符例子。
    通过遵循描述符协议，开发者可以自定义对类属性的操作，从而增强了属性封装和抽象能力。
"""



