from collections import namedtuple

"""
元组是用（）内，是否有逗号来区分的，

"""
a = ()  # 是一个例外，只是为了方便区分
b = (2)  # 不是一个元组
b1 = ('asdiah')  # not a tuple
c = 1, 2, 3, 4
d = tuple(range(1, 6))
e = tuple(b'adsd')
print(a, f'类型是：{type(a)}')  # <class 'tuple'>
print(b, f'类型是：{type(b)}')  # <class 'int'>
print(b1, f'类型是：{type(b1)}')  # <class 'str'>
print(c, f'类型是：{type(c)}')  # (1, 2, 3, 4) <class 'tuple'>
print(d, f'类型是：{type(d)}')  # (1, 2, 3, 4, 5) 类型是：<class 'tuple'>
print(e, f'类型是：{type(e)}')  # (97, 100, 115, 100) 类型是：<class 'tuple'>

"""元组解包
用*号将其中多个对象以列表的形式归集给指定的标识符
"""
foo, bar, baz = 1, 2, 3
a, *b = 1, 2, 3, 4, 5, 6, 8  # *号将后面的多个对象以列表的形式归集给b

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
a1, *b1, c1 = x
print(a1)
print(b1)
print(c1)

print('--------------------------')

"""
namedtuple()函数创建一个自定义的tuple类，使用方式和tuple一样，但可以自定义类名和属性名
"""
Stu = namedtuple('Student111', ['name', 'age', 'sex'])  # 创建一个Stu的类
# Stu1 = namedtuple('Stu', 'name, age, sex')
# Stu2 = namedtuple('Stu', 'name age sex') # 以上三种方式都可以
s = Stu('zhangsan', 18, '男')  # 实例化一个对象
print(s)
print(type(s), isinstance(s, tuple), issubclass(Stu, tuple))  # 类型; 是否是tuple; 是否是tuple的子类

print(s.__doc__)
s2 = namedtuple('Stu', range(3), rename=True)
print(s2.__doc__)
print('--------------------------')
print(s[0], s[2])  # 通过下标访问属性
print(s.age)  # 通过属性访问属性
print(getattr(s, 'sex'))  # 通过getattr()函数访问属性
print(s._fields)  # 获取属性名列表
print(s._asdict())  # 获取属性名和属性值的字典
print(tuple(s))  # 将对象转换为元组
s = s._replace(age=100)  # 通过_replace()方法修改属性值
print(s)
print('--------------------------')
"""zip()函数是一个内建函数，它用于将可迭代对象（如列表、元组、字符串或其他迭代器）中的元素按相同位置配对，并返回一个包含这些配对的“元组序列”。
在Python 3中，zip()函数直接返回一个可迭代的zip对象（单次迭代：只能迭代一次），而不是列表。如果需要将zip对象转换为列表形式，可以使用list()函数

zip函数在处理不同长度的可迭代对象时，其结果会以最短的可迭代对象为准，忽略多余的元素。
如果你想让zip函数在所有输入迭代器中最长的长度上运行，可以使用itertools.zip_longest()函数（在Python 2中名为izip_longest()），并提供一个填充值来处理不足的部分
"""
a, b, d = [1, 2, 3], ['1', '2', '3'], ['a', 'b', 'c']

c = zip(a, b)
print(c)
print(type(c))
f = dict(c)
print(f)

e = list(c)
print(type(e))
print(e)
print(c)
print(dict(e))

"""
a, b, d = [1, 2, 3], ['1', '2', '3'], ['a', 'b', 'c']

# c 是 zip 对象，包含了 (1, '1'), (2, '2') 和 (3, '3')
c = zip(a, b)

# 输出：<class 'zip'>
print(type(c))

# f 是由 zip 对象转换而来的字典，键是 a 列表的元素，值是 b 列表的元素
f = dict(c)
print(f)  # 输出：{1: '1', 2: '2', 3: '3'}

# 当尝试将已经迭代过的 zip 对象转换为列表时，由于zip对象是单次迭代的，因此e将为空列表
e = list(c)
print(type(e))  # 输出：<class 'list'>
print(e)        # 输出：[]

# 再次打印 c，由于zip对象在转化为列表后已经被迭代完，所以直接打印不会显示具体内容
print(c)

# 尝试将空列表 e 转化为字典，结果是一个空字典
print(dict(e))  # 输出：{}

当对zip对象进行迭代时，它会按顺序返回这些元组
注：关键在于，zip对象在第一次迭代后（如转换为字典或通过for循环遍历），其内部状态会发生变化，后续再试图将其转换为列表时，因为没有剩余的元素可以迭代，所以得到的是一个空列表。

"""
print('--------------------------')
c1 = zip(a, d)
print(type(c1))
print(dict(c1))  # zip对象转换为dict
print('--------------------------')
print(dict([(1, '1'), (2, '2'), (3, '3')]))

keys = ['a', 'b', 'c']
values = [1, 2, 3]
bbb = zip(keys, values)
dictionary = dict(bbb)  # 直接转换为字典
print(dictionary)  # 输出：{'a': 1, 'b': 2, 'c': 3}
print('--------------------------')
"""不可哈希（Unhashable）对象在Python中指的是那些不能作为字典键或者其他需要哈希功能的数据结构元素的对象。这些对象通常是可变的，因为哈希值必须在对象生命周期内保持不变，以确保哈希表的一致性。以下是Python中常见的不可哈希对象类型：
列表（list）
集合（set）
字典（dict）
由于这些类型的对象内容可以动态改变，因此它们不支持哈希操作。例如，你不能将一个列表用作字典的键，尝试这样做会引发TypeError，提示“unhashable type”。
不过，如果你确实需要将可变类型用作字典键或类似情况下的哈希键，你可以考虑将它们转换为不可变形式，如使用元组（tuple）来代替列表，或者将字典转换成frozenset的集合形式（如果适用）。
"""
print(hash('123'))
print(hash(123))
print(hash(123.0))
print(hash(range(12)))
print(hash((1, 2, 3)))
# print(hash([12, 312, 1]))  # TypeError: unhashable type: 'list'
