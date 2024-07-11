"""你定义一个你知道你会在某个时候 print() 的类时，默认的 Python 表示可能不是很有帮助。您可以定义自定义 __str__方法来控制不同组件的打印方式，以获得更好的清晰度和可读性。

__str__ 方法实现允许我们以人类可读的方式显示类，__repr__ 方法可用于获取类的机器可读格式。

Python 类中__repr__ 的事实上的实现没有重要用途。该方法应该具有构造对象所需的一切。
    对象和 __repr__ 输出应该是可区分的对象。这在日志记录用例中很有帮助；例如，列表对象的组成部分使用 __repr__ 而不是 __str__ 表示形式显示。
"""
print('-------')


class Person:
    def __init__(self, name, interests: [str]):
        self.name = name
        self.interests = interests

    def __str__(self):  # 为用户读取准备的
        return F"{self.name} like {'，'.join(self.interests)}"

    def __repr__(self):  # 为机器和开发人员准备的
        return F"Person(name={self.name} ,interests={self.interests})"

    def __eq__(self, other):
        return self.name == other.name and self.interests == other.interests


person = Person('9BUND', ['basketball', 'football'])
# 不实现__str__ 和 __repr__,打印的是对象的地址
print(person)  # <__main__.Person object at 0x100c8e0d0>
print(str(person))  # <__main__.Person object at 0x100c8e0d0>
print(repr(person))  # <__main__.Person object at 0x100c8e0d0>
print('-----------------')

"""
在Python中，__str__和__repr__都是特殊方法（也称为魔术方法），它们用于自定义对象的字符串表示。这两个方法在处理对象转换为字符串时起着关键作用：
__str__():
    这个方法返回一个适合人类阅读的字符串表示，通常应该是用户友好的，如果可能的话，它应该提供足够的信息来理解对象的含义。
    当使用str()函数、print()函数或者直接输出对象时，Python会自动调用__str__()方法。
    如果没有定义__str__()，Python会尝试调用__repr__()作为备选方案。
"""
# 只实现 __str__
print(person)  # 9BUND like basketball，football
print(str(person))  # 9BUND like basketball，football
print(repr(person))  # <__main__.Person object at 0x10ba05f10>
print('-----------------')

"""
__repr__():
    __repr__()返回一个对象的“官方”或“代表”字符串表示，通常更倾向于程序员的视角，旨在清楚地表明对象是什么，而不是仅仅显示它的值。
    它的目的是当对象出现在交互式解释器或调试器中时，能提供一种明确识别对象的方式。
    如果没有定义__repr__()，Python会返回一个默认的表示，通常是类名加上内存地址。
"""
print(person)  # Person(name=9BUND ,interests=['basketball', 'football'])
print(str(person))  # Person(name=9BUND ,interests=['basketball', 'football'])
print(repr(person))  # Person(name=9BUND ,interests=['basketball', 'football'])
print('-----------------')

# 两个魔术方法同时存在
print(person)  # 9BUND like basketball，football
print(str(person))  # 9BUND like basketball，football
print(repr(person))  # Person(name=9BUND ,interests=['basketball', 'football'])

othrt_person = eval(repr(person))  # eval()函数接收一个字符串参数，并将这个字符串当作有效的 Python 表达式执行，然后返回表达式的值。
print(person == othrt_person)  # True

import datetime

datetime.datetime.now()
