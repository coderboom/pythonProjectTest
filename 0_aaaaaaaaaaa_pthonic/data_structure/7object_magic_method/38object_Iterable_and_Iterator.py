"""可迭代对象及其创建"""
print('----------------------------------------')
"""Python 中的对象属性本质上是公共的，并且不支持任何访问说明符来使它们成为私有或受保护的。您不能阻止任何调用对象访问基础对象上的任何属性。
Python 没有严格执行访问说明符，但它是一种社区驱动的语言，有几个约定可以弥补它。当你用双下划线开始一个属性时，你表明它对于对象的范围是私有的。

一些常用的 Python 对象，如列表、集合、字典或元组，不仅有助于存储数据，而且还提供了对它们存储的值进行迭代的构造。
    Python 使开发人员能够使用自定义逻辑创建他或她自己的迭代。这又是使用“魔术方法”的地方。
Python 中的迭代协议是如何工作的呢？当您执行“for element in elements”之类的循环时，
解释器会验证以下内容：
    * 对象是否具有__iter__ 或 __next__迭代器方法。
    * 被迭代的序列对象是否具有 __getitem__或 __len__方法。

序列可以被迭代，并且前面的机制可以启用这种行为。当需要迭代时，解释器将调用对象的 iter() 方法。
    该函数反过来将调用 __iter__ 方法，如果存在，该方法将运行。

迭代开始时，Python 会调用调用 __iter__的 iter() 函数。
    我们已将其配置为返回 self，这意味着结果再次是可迭代的，因此控制权转移到 __next__函数。 
    __next__方法将决定或容纳逻辑来决定哪些是需要返回的后续元素。当我们没有值时，它会引发一个StopIteration异常。
"""
print('-------------------可迭代对象的创建和迭代---------------------')
"""
使用for 迭代可迭代对象时，首先：
1、检察对象是否具有__iter__或__next__迭代器方法
2、被迭代的序列对象是否具有__getitem__或者__len__ 魔术方法
"""


class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.previous = 0
        self.current = 1
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._count > self.n:
            raise StopIteration
        self._count += 1
        return_value = self.previous
        self.previous, self.current = self.current, self.previous + self.current
        return return_value


for num in Fibonacci(4):
    # for循环开始，它会调用Fibonacci(4)实例的__iter__方法，由于__iter__返回self，所以迭代器仍然是Fibonacci(4)实例。
    # 在每次循环迭代开始时，Python内部会隐式地调用迭代器的__next__方法。对于Fibonacci实例，这意味着执行Fibonacci(4).__next__()。
    print(num)
"""
1、for num in Fibonacci(4): 这行代码开始一个for循环，其中num将被用来存储在迭代过程中获取的每一个值。
    Fibonacci(4)创建了一个Fibonacci类的新实例，传入的参数4表示我们希望生成斐波那契数列的前4个数字。
2、Fibonacci(4)：
    Fibonacci 类的构造函数 __init__ 被调用，self.n 被设置为 4。
    self.previous 和 self.current 分别初始化为 0 和 1，这是斐波那契数列的前两个数。
    self._count 初始化为 0，用于追踪生成的斐波那契数的数量。
3、for循环的迭代过程：
    Fibonacci 实例被用作迭代器，因为它的 __iter__ 方法返回了自身。
    __next__ 方法被调用，开始迭代过程。
    第一次迭代：
    self._count 为 0，小于 4，所以不抛出 StopIteration 异常。
    self.previous（当前值为 0）被返回给 num 并打印出来。
    self.previous 和 self.current 更新，self.previous 变为 1，self.current 变为 1（0 + 1）。
    第二次迭代：
    self._count 为 1，仍小于 4，继续迭代。
    self.previous（当前值为 1）被返回给 num 并打印出来。
    self.previous 和 self.current 更新，self.previous 变为 1，self.current 变为 2（1 + 1）。
    第三次迭代：
    同理，self.previous（当前值为 1）被返回给 num 并打印出来。
    self.previous 和 self.current 更新，self.previous 变为 2，self.current 变为 3（1 + 2）。
    第四次迭代：
    self._count 为 3，仍小于 4，继续迭代。
    self.previous（当前值为 2）被返回给 num 并打印出来。
    self.previous 和 self.current 更新，self.previous 变为 3，self.current 变为 5（2 + 3）。
    第五次迭代：
    self._count 为 4，等于 4，因此抛出 StopIteration 异常，for循环结束。
所以，输出将是斐波那契数列的前4个数字：0, 1, 1, 2。
"""

print('-----------------------')
"""
问：for 循环首先会调用__iter__得到迭代器，再调用迭代器__next__进行迭代，那为什么一个list可以for循环很多次呢，迭代器不是一次性的吗？

答：在for循环执行的时候，被执行体成为Iteratable，而迭代器通过next()调用一直到raise StopIteration错误。
而对于list，它实现了__len__和__getitem__的魔术方法，可以取得长度和通过索引获取对应的项，
    所以再执行for循环的时候，通过iter()函数对list生成一个iterator，
    譬如，list = 【'a', 'b', 'c', 'd', 'e', f'】, 
    如果for循环的话，内部的机制会通过iter函数生成对应的iterator是iter(【‘a', 'b’, 'c', 'd', 'e', 'f'】)，
    然后循环获取next(list_iterator)直到raise StopIteration来结束循环。
"""
