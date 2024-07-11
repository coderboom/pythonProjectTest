"""
可调用对象：可调用对象是指那些可以像函数一样被调用的对象，即它们实现了调用协议（__call__方法）。调用一个对象通常意味着执行与该对象相关的特定操作
"""
"""Python 允许您创建行为类似于函数的对象。
    此功能的众多应用之一是创建更健壮的装饰器。
    当试图执行对象时，我们使用__call__ 魔术方法l来模拟正常函数。此外，提供给对象的参数将被移交给 __call__ 方法。
    
__call__方法是双刃剑，用好了让你的代码丝般顺滑，让人容易理解，容易维护；
    但用的不好的话，会导致羞涩难懂的尴尬。它作为后续装饰器decorator的铺垫起到了重要的作用。
    
callable(object)
如果参数 object 是可调用的就返回 True，否则返回 False。 
    如果返回 True，调用仍可能失败，但如果返回 False，则调用 object 将肯定不会成功。 
    请注意类是可调用的（调用类将返回一个新的实例）；如果实例所属的类有 __call__() 则它就是可调用的,没有就不是可调用的。
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, weight):
        self.weight = weight
        print(self.name, self.age, self.weight)
        return self


person = Person('joy', 29)
print(callable(person))
"""
未实现__call__：返回 False

实现__call__：返回 True
"""
its_me = person(100)
print(its_me.name, its_me.age, its_me.weight)
"""输出：
joy 29 100
joy 29 100
"""
light_me = its_me(12)
print(light_me.name, light_me.age, light_me.weight)
"""输出：
joy 29 12
joy 29 12
"""
abcpe = person(100)(90)(2)
print(abcpe.name, abcpe.age, abcpe.weight)
"""输出：
joy 29 100
joy 29 90
joy 29 2
joy 29 2
"""
print('--------------------------------------')
from collections import defaultdict
