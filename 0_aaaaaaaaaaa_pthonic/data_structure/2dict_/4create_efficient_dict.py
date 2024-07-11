cars_config = {'volvo': 'c1c', 'asdoj': 'ojsd12'}
print(cars_config.get('volvo1', 'ccccaaaaa'))
print(cars_config.get('asdad'))  # 不提供默认值返回的是： None
"""
使用字典的get方法，可以设置默认返回参数，不用在去判断是否有这这个键，在大部分场景下能使代码更整洁

传统方法根据键取值，若键不存在，会抛出异常
         ——————在具体使用场景需要两者衡量一下
"""

print('-------------------------------defaultdict-----------------------------------')
"""defaultdict 是 Python 标准库 collections 模块中提供的一个非常实用的数据结构，它是 dict 类的一个子类，继承了 dict 的所有功能，
并在此基础上增加了一个特性：
    当尝试访问一个不存在的键时，defaultdict 不会抛出 KeyError 异常，而是自动为其创建一个默认值。
    这种特性使得 defaultdict 在处理需要预先填充或动态添加默认值的场景时尤为便捷。

以下是对 defaultdict 的详细解析：
"""
from collections import defaultdict

# 创建一个 defaultdict，默认值类型为 int，初始值为 0
dd = defaultdict(int)

# 添加或更新键值对，与普通字典无异
dd['apple'] = 3
dd['banana'] = 5

# 访问已存在的键
print(dd['apple'])  # 输出: 3

# 访问不存在的键，此时会自动创建一个默认值（这里是 0）
print(dd['orange'])  # 输出: 0

# 默认值已经存在于字典中，可以正常进行操作
dd['orange'] += 2
print(dd['orange'])  # 输出: 2

"""
构造参数：默认工厂函数
    defaultdict 的初始化需要传入一个可调用对象作为其唯一的参数，这个可调用对象被称为默认工厂函数。
        当访问一个不存在的键时，defaultdict 会调用这个工厂函数来生成新的默认值。
    
    常见的工厂函数包括：
    内置类型（如 int, list, set, str 等）：直接传入类型本身，会创建该类型的默认实例（如 int() 生成 0，list() 生成空列表等）。
    自定义函数：可以是任何可调用对象，如一个无参函数或一个 lambda 表达式，用于生成特定类型的默认值或复杂数据结构。
"""
# 使用 list 作为默认工厂函数
words_dd = defaultdict(list)
words_dd['fruit'].append('apple')  # 自动创建并添加元素
print(words_dd)  # 输出: {'fruit': ['apple']}

# 使用 lambda 表达式生成默认值为长度为 2 的 tuple
tuples_dd = defaultdict(lambda: (0, 0))
# tuples_dd['pair1'][0] = 10  # 自动创建并修改元素
# print(tuples_dd)  # 输出: {'pair1': (10, 0)}

"""
与普通字典的区别
    与普通字典相比，defaultdict 的主要区别在于处理未出现键的方式：
    普通字典 (dict)：尝试访问不存在的键时，会抛出 KeyError 异常。
    defaultdict：尝试访问不存在的键时，会调用默认工厂函数生成一个默认值，并将其与该键关联，然后返回该值。
    
应用场景
    defaultdict 常用于以下几种情况：
    统计：快速累加计数、构建频率表等，无需先检查键是否存在。
"""
word_counts = defaultdict(int)
text = [12, 3, 12, 1, 2, 31, 231, 23, 4, 23, 4, 21, 31, 23, 12, 31, 231, 5,
        4, 2, 3, 1, 1, 34, 45, 12, 32, 6, 6, 23, 31, 23, 3231, 1, 322, 423]
for word in text:
    word_counts[word] += 1
print(word_counts)

"""初始化集合型数据结构：确保每个键对应的值都是一个新的列表、集合等，避免反复检查和初始化。"""
user_preferences = defaultdict(list)
user_preferences['Alice'].append('coffee')
user_preferences['Bob'].extend(['tea', 'chocolate'])

"""填充缺失数据：在处理数据时，自动为缺失的键提供有意义的默认值。"""
grades = defaultdict(lambda: 'N/A')
grades.update({'Alice': 'A', 'Bob': 'B'})
print(grades['Charlie'])  # 输出: 'N/A'

"""
不要混淆默认值与已插入的键值：虽然访问不存在的键会返回默认值，但这个键确实已经被添加到了字典中。
    后续对该键的操作会影响实际存储的值，而不是重新生成默认值。
    
默认工厂函数应避免有副作用：由于工厂函数可能被多次调用，如果它有副作用（如改变全局状态、产生不可预期的输出等），可能会导致意外的行为。

序列化与pickle兼容性：defaultdict 可以像普通字典一样被序列化（如使用 json.dumps() 或 pickle.dump()）。
    但在反序列化时，恢复的对象将是普通字典，丢失了 defaultdict 的特殊行为。若需保持 defaultdict 类型，可能需要在反序列化后手动转换。
    
总结来说，defaultdict 是一个增强版的字典，它通过提供一个默认工厂函数，
    简化了处理未知键时的逻辑，避免了频繁的 if key in dictionary 判断或捕获 KeyError 异常。
    这使得代码更加简洁、高效，并且适用于多种需要自动填充默认值的场景。
"""


def create_factory(value):
    return lambda: value


d = defaultdict(create_factory('xxxxx'))
d.update(name='jeff', action='eat')
print(d)
print(f'{d["name"]} s ,{d["action"]} is {d["undows"]}')
