"""Property 装饰器"""
"""
我们把在代码运行期间动态增加函数或方法功能的方式，叫“装饰器”（Decorator）。
面向对象的设计强调封装， 把对象内聚的状态私有化，仅供类的内部进行操作。
被封装的属性通常是通过类的 getter 和 setter 方法来实现的。
在 Python 中，普遍认为直接访问属性进行读写比创建单独的 getter 和 setter 方法更有意义。
"""


class Square:
    def __init__(self):
        self.side = None

    def get_side(self):
        return self.side

    def set_side(self, side):
        assert side > 0, '边长不能为负数'
        self.side = side

    def get_area(self):
        return self.get_side() * self.get_side()


"""上面是传统方法，下面是使用装饰器方法"""


class Square1:
    def __init__(self):
        self._side = 0

    @property
    def side(self):
        return self._side

    """
    # @side.getter
    # def side(self):
    #     return self._side
    
    在Python中，一旦你已经使用@property装饰器定义了一个属性，如@value，那么默认就会有一个getter方法。
    这意味着你不需要再单独使用@value.getter来定义getter方法。
    当你这样做的时候，Python会忽略这个装饰器，因为getter方法已经被@property定义了
    """

    @side.setter
    def side(self, side):
        assert self._side >= 0, '边长不能为负数'
        self._side = side

    @side.deleter
    def side(self):
        self._side = 0

    @property
    def area(self):
        return self._side * self._side


suqare = Square1()
print(suqare.side)
suqare.side = 10
print(suqare.side, suqare.area)
del suqare.side
print(suqare.side, suqare.area)

print('----------------------详解------------------------')
"""
@property装饰器是用来创建一个只读属性的方法，它可以让我们以属性的方式访问一个方法，而不需要使用括号。
    这样做的好处是增加了代码的可读性，同时也提供了对属性访问的控制

1. @property是一个内置的类装饰器，
    它允许我们将一个方法变成对象的一个属性调用。这个方法通常用于获取（getter）一个对象的状态，而不需要直接暴露内部的变量。
"""


class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


my = MyClass(12)
print(my.value)
""" 
在这个例子中，value是一个@property装饰器的方法，当我们像访问属性一样调用my_obj.value时，实际上是在执行MyClass实例的value方法。

2. 添加setter方法
如果想要给@property属性添加设置值（setter）的功能，我们可以定义一个额外的方法并使用@<property_name>.setter装饰器：     
"""


class MyClass1:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, int):  # 检查类型
            raise ValueError("Value must be an integer.")
        self._value = new_value


"""
3. 删除器方法（deleter）
除了getter和setter，还可以定义删除器方法（deleter），使用@<property_name>.deleter装饰器，但这种情况相对较少见：
"""


class MyClass2:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @value.deleter
    def value(self):
        del self._value


"""
4. 应用场景
数据验证：在设置属性值时，可以进行数据校验或类型检查。
访问控制：隐藏内部实现细节，防止外部直接修改对象状态。
缓存：可以缓存计算结果，避免重复计算。

5. 优势
提供了封装，使得代码更易于理解和维护。
控制属性的访问权限，防止意外修改。
可以在不改变API的情况下添加新的行为。
通过使用@property，我们可以确保在访问或修改属性时执行额外的逻辑，这在处理复杂对象或需要控制数据流的应用程序中非常有用。
"""
