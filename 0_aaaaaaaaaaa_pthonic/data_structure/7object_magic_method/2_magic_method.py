"""magic method"""
print('---------')
"""
Python的魔术方法（Magic Methods）是一组以双下划线__开头和结尾的特殊方法，它们用于实现特定的内置行为。

以下是一些常见的魔术方法，但请注意，这不是完整的列表，因为Python有几十个魔术方法，具体取决于版本和库：
实例化和初始化：
    __new__(cls[, ...]): 创建类的新实例。
    __init__(self[, ...]): 初始化新创建的实例。
算术操作：
    __add__(self, other): 自定义加法。
    __sub__(self, other): 自定义减法。
    __mul__(self, other): 自定义乘法。
    __truediv__(self, other): 自定义真除法（Python 3.x）。
    __floordiv__(self, other): 自定义地板除法。
    __mod__(self, other): 自定义取模。
    __pow__(self, other[, modulo]): 自定义幂运算。
    __lshift__(self, other): 自定义左移位。
    __rshift__(self, other): 自定义右移位。
    __and__(self, other): 自定义按位与。
    __xor__(self, other): 自定义按位异或。
    __or__(self, other): 自定义按位或。
比较操作：
    __lt__(self, other): 自定义小于。
    __le__(self, other): 自定义小于等于。
    __eq__(self, other): 自定义等于。
    __ne__(self, other): 自定义不等于。
    __gt__(self, other): 自定义大于。
    __ge__(self, other): 自定义大于等于。
一元操作符：
    __pos__(self): 自定义正号。
    __neg__(self): 自定义负号。
    __abs__(self): 自定义绝对值。
    __invert__(self): 自定义按位取反。
二进制和反射操作：
    __radd__(self, other): 反射加法。
    __rsub__(self, other): 反射减法。
    __rmul__(self, other): 反射乘法。
    __rtruediv__(self, other): 反射真除法。
    __rfloordiv__(self, other): 反射地板除法。
    __rmod__(self, other): 反射取模。
    __rpow__(self, other): 反射幂运算。
    __rlshift__(self, other): 反射左移位。
    __rrshift__(self, other): 反射右移位。
    __rand__(self, other): 反射按位与。
    __rxor__(self, other): 反射按位异或。
    __ror__(self, other): 反射按位或。
其他操作：
    __hash__(self): 自定义哈希值。
    __str__(self): 自定义转化为字符串。
    __repr__(self): 自定义转化为可读字符串。
    __bytes__(self): 自定义转化为字节串。
    __contains__(self, item): 自定义in操作符。
    __len__(self): 自定义len()函数。
    __getitem__(self, key): 自定义索引访问。
    __setitem__(self, key, value): 自定义索引赋值。
    __delitem__(self, key): 自定义删除索引项。
    __getattr__(self, name): 自定义属性访问。
    __setattr__(self, name, value): 自定义属性赋值。
    __delattr__(self, name): 自定义删除属性。
    __enter__(self): 对象进入上下文管理器。
    __exit__(self, exc_type, exc_value, traceback): 对象退出上下文管理器。
特殊用途：
    __init_subclass__(cls, **kwargs): 类初始化时调用。
    __getattr__, __getattribute__, __setattr__, __delattr__: 控制属性访问。
    __get__(self, instance, owner=None): 描述符的获取行为。
    __set__(self, instance, value): 描述符的设置行为。
    __delete__(self, instance): 描述符的删除行为。
    __dir__(self): 自定义dir()函数的结果。
    __reduce__(self): 支持pickle序列化。
    __sizeof__(self): 获取对象的内存大小。
    __subclasshook__(cls, C): 定义子类检查。
这些方法允许你定制类的行为，使其能更好地适应特定的场景。如果你需要更详细的文档或最新的魔术方法列表，建议查阅Python官方文档。
"""
print('-------------------------------魔术方法的隐式调用------------------------------')
"""
__new__(cls[, ...]) 是 Python 的魔术方法，它在创建类的新实例时被隐式调用。
    这个方法是类实例化的第一步，通常由 type() 函数触发。__new__ 负责分配内存空间并返回一个新创建的对象，这个对象通常是类的实例。
    cls 参数是创建实例的类，通常由 Python 解释器自动传递。其他的参数可以传递给 __new__，它们会传递给随后的 __init__ 方法。
    
在大多数情况下，我们不需要重写 __new__，除非我们想要控制实例的创建过程，比如实现单例模式、共享资源或者自定义对象的创建方式。
    通常，我们只需要重写 __init__ 来初始化实例的属性和状态。但请注意，如果你重写了 __new__，确保它返回一个新的实例，否则后续的 __init__ 将不会被调用。
"""


class MyClass:
    def __new__(cls, *args, **kwargs):
        # 分配内存并创建新实例
        instance = super().__new__(cls)

        # 可以在这里进行额外的初始化工作，但通常放在 __init__ 中
        # instance.some_attribute = value

        return instance

    def __init__(self):
        pass


# 创建实例时，__new__ 会被隐式调用
my_instance = MyClass()

"""
__init__(self[, ...]) 是 Python 中的另一个魔术方法，它用于初始化新创建的实例。
    这个方法在 __new__ 方法返回新对象后被调用，通常用于设置实例的属性或执行其他初始化操作。self 参数是实例本身，而其他的参数可以根据类的需要传递。
"""


class MyClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        # 其他初始化操作...


"""在这个例子中，当我们创建 MyClass 的新实例时，__init__ 会被隐式调用，允许我们设置 arg1 和 arg2 作为实例的属性"""
my_instance = MyClass('value1', 'value2')
"""在上面的代码中，my_instance 的 arg1 属性被设置为 'value1'，arg2 属性被设置为 'value2'。
    __init__ 是我们通常用于设置实例状态的地方，但不会分配新的对象，它的任务是根据传入的参数来配置新创建的对象。"""

print('-------------------------------__add__-------------------------------')

"""__add__(self, other): 自定义加法。
__add__(self, other) 是 Python 的魔术方法，用于自定义两个对象的加法操作。当使用 + 运算符连接两个对象时，Python 会尝试调用这个方法。self 参数是左操作数（即 + 符号左边的对象），other 参数是右操作数（即 + 符号右边的对象）。
例如，如果你有一个自定义的类 MyNumber，并且你想让这个类的实例支持加法操作，
你可以这样做：
"""


class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self.value + other.value)
        else:
            raise TypeError(f"Cannot add {type(other)} to MyNumber")


# 使用 + 运算符隐式调用 __add__ 方法
result = MyNumber(5) + MyNumber(7)
print(result.value)  # 输出: 12
"""在这个例子中，当你执行 MyNumber(5) + MyNumber(7) 时，Python 会调用 MyNumber 类的 __add__ 方法，将 self 设置为 MyNumber(5) 的实例，
    other 设置为 MyNumber(7) 的实例。 __add__ 方法计算两个 value 的和，并返回一个新的 MyNumber 实例。
    
注意，如果你的类需要与其他类型（如整数或浮点数）进行加法运算，你需要在 __add__ 方法中处理这些情况，例如通过类型检查和转换。
    在这个例子中，如果 other 不是 MyNumber 的实例，会抛出 TypeError。
"""
