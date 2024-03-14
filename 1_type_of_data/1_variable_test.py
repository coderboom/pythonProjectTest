import keyword

"""
变量一旦建立你可以放任何东西，它都能接受，不需要事先申明我将要放什么

由 字母、汉字（包括表情符，但尽量别用）下划线 和 数字 组成
大小写敏感（就是大小写不一样）
不能以数字开头
不能与关键字重名

"""

print(keyword.kwlist,)

"""
标准的数据类型中，有些是可变的，有些是不可以变的，不可变就意味差你不能对它进行操作，只能读取。

不可变数据：Number（数字）、String（字符串）、Tuple（元组）；
可变数据：List（列表）、Dictionary（字典）、Set（集合）。

"""
a = '23123'
print(type(a))
print(isinstance(a, str))  # isinstance(a,b) 判断a是否是b类型

"""
对象的类型:

类型 type
空类型 NoneType
数字 numeric
    整型 int
        布尔 bool
    浮点 float
    复数 complex
容器 collections
    序列 sequence
        可变序列 abc.MutableSequence
            列表 list
        字节数组 bytearray
    不可变序列 ImmutableSequence
        元组 tuple
        字符串 string
        等差数列 range
        字节串 bytes
        内存视图 memoryview
    集合 set
        可变集合 set
        不可变集合 frozenset
    映射 mapping
        字典 dict
上下文管理器 context manager
类型注解的类型 type annotation
其他内置类型
    迭代器 iterator
        生成器 generator
    模块 module
    类与类实例 class/instances
    函数 function
    方法 method
    代码 code
    省略符 Ellipsis
    未实现 NotImplemented
    栈帧 frame
    扩展类型 (内置库)
    高效数组 array.array
    枚举 enum.Enum
    有理数 fractions.Fraction
    指定精度浮点数 decimal.Decimal
    时间 datetime.datetime
    命名元组 collections.namedtuple
    双向队列 collections.deque
    有序字典 collections.OrderedDict
    映射链 collections.ChainMap
    计数器 collections.Counter
    默认字典 collections.defaultdict
"""
print('22222')
"""
鸭子类型（Duck Typing）是一种在编程中使用的概念，它强调一个对象的类型是由其行为而不是其类别或明确的接口定义来确定的。
换句话说，如果一个对象的行为类似于鸭子，那么它就可以被视为鸭子。在Python中，由于其动态类型和灵活性，鸭子类型经常出现。

可迭代对象 Iterable
可调用对象 callable
list-like
dict-lick
array-like
可等待对象

"""