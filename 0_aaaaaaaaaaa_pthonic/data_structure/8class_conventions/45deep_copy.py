print('deep copy')
"""
Python对象的深层复制deep copy与浅层复制shallow copy有着一定的区别，它会复制对象的结构树中的所有节点为新的实例而不是共享实例。
    对于有些需要不共享的场合是很有用的。
    
当然，也不是什么都需要重新生成实例，对于原生类型的值，如整型int、字符串等，是可以通过引用的方式指向同一值的位置达到节省内存资源和高效访问的目的。
    这需要我们对deep copy中的memo的使用有一定的了解。
    当然，这memo可以是隐含的方式使用，除非你想控制deep copy的规则或者想窥视copy中产生的中间字典表达的内涵，否则的话最好不要去触碰它，避免产生副作用。
    
Python的copy模块公开了copy.deepcopy() API 以创建对象的克隆。
"""
import copy

list1 = [1, 2, 3, 4, 5, [11, 22, 33, 54]]
list2 = copy.deepcopy(list1)
print(id(list1), id(list2))  # 4385269312 4385273472
print(id(list1[-1]), id(list2[-1]))  # 4339852160 4385273536
print(id(list1[-1][1]), id(list2[-1][1]))  # 4337596176 4337596176

print(id(list1[0]), id(list1[1]), id(list1[2]))  # 4310840432 4310840464 4310840496
print(id(list2[0]), id(list2[1]), id(list2[2]))  # 4310840432 4310840464 4310840496
"""为什么值是一样的，见cpython的常用数字缓存

Python为了提高效率，对小整数(-5至256)进行了缓存，这意味着在这个范围内的每个整数都只存在一个实例，多次赋值给不同的变量实际上都是引用同一个对象。
    这一特性自动提供了这些数字的缓存效果，无需额外编程。
    
    小整数缓存
原理：Python解释器启动时，会预先创建一个小整数池，通常包含从-5到256的整数（这个范围可能会根据Python版本有所不同）。
    当你创建这个范围内的整数时，Python直接从池中返回已存在的对象引用，而不是每次都创建新的对象
  a = 250
  b = 250
  print(a is b)  # 输出True，表明a和b指向同一对象
  
大整数及其他类型的缓存
对于大整数或其他非整数类型的数字（如浮点数），Python默认并没有类似的内置缓存机制。
    如果你的应用场景中需要缓存这些数值以提高性能，可以自定义一个缓存机制，例如使用functools.lru_cache装饰器来缓存函数的计算结果，
    当涉及到大量重复计算时非常有用。

"""
"""自定义缓存示例
假设你有一个复杂的计算过程来生成某些数字，可以这样做："""
from functools import lru_cache

# @lru_cache(maxsize=None)
# def complex_calculation(x):
#     # 这里是你的复杂计算逻辑
#     return x * x + some_other_operations()
#
#
# # 使用缓存的计算
# result1 = complex_calculation(10)
# result2 = complex_calculation(10)  # 第二次调用将直接从缓存中获取结果
"""在这个例子中，lru_cache装饰器为complex_calculation函数的结果提供了缓存，避免了重复计算。
总的来说，Python的小整数缓存是自动进行的，而对于其他数字类型或需要优化特定计算场景时，可以通过自定义缓存策略来实现。
"""

print('deepcopy的 类的形式')


class A:
    def __repr__(self):
        return f"A - {id(self)}"


class B:
    def __init__(self, a: A):
        self.a = a
        self.b = self
        self.c = 1

    def __repr__(self):
        return f"B - {id(self)}"


a1 = A()
b1 = B(a1)

memo = {}  # 备忘录
b2 = copy.deepcopy(b1, memo)
print(memo)
# {4604228304: B - 4602321104,
# 4603408960: {'a': A - 4602321168, 'b': B - 4602321104, 'c': 1},
# 4604228240: A - 4602321168,
# 4336672640: [A - 4604228240, {'a': A - 4604228240, 'b': B - 4604228304, 'c': 1}, B - 4604228304]}

print(id(a1), id(b1), id(b2), id(b2.a), id(b2.b), id(b2.c), id(b2.b.b), id(b2.b.b.b.b.a))
# 4604228240 4604228304 4602321104 4602321168 4602321104 4334417008 4602321104 4602321168
"""id(b2.a) he  id(b2.b.b.b.b.a)) 结果一样，见deepcopy()函数方式避免了的问题"""
