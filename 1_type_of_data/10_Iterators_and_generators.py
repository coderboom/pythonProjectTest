from collections import abc

"""
可迭代对象：实现__iter__方法的对象，都可以被for循环迭代。
迭代器：实现__iter__()和__next__方法的对象，都可以被next函数调用，直到StopIteration异常。
生成器：生成器是一种特殊的迭代器，但它并不直接实现 __iter__() 和 __next__() 方法，
    而是通过 yield 关键字在函数内部产生值。
    Python解释器会自动将这样的函数转换为生成器对象，并提供相应的 __iter__() 和 __next__() 方法。
"""
print(isinstance([1, 2, 3], abc.Iterator))  # False
print(isinstance((1, 2, 3), abc.Iterator))  # False
print(isinstance({'qwe': 'qwe'}, abc.Iterator))  # False
print(isinstance({1, 2, 3, 4, 5}, abc.Iterator))  # False
print(isinstance('abc', abc.Iterator))  # False
print(isinstance(123, abc.Iterator))  # False
print(isinstance((i for i in range(10)), abc.Iterator))  # True
"""在Python中存在类似元组推导式的语法结构，不过它并不直接生成元组，而是生成一个--生成器表达式--。
这是因为当使用圆括号 () 进行推导时，Python会将其解释为生成器表达式（generator expression），而非直接创建元组，
————————这就是没有元组生成器的原因。
"""

"""如果想得到一个元组，可以通过调用 tuple 函数将生成器表达式转换为
元组推导式的等效实现
tuples = tuple(expression for item in sequence if condition)
"""
tuples = tuple(i for i in range(10))
print(tuples)
"""列表推导式、集合推导式和字典推导式是三种简洁的表达式结构，它们用于从一个或多个可迭代对象（如列表、元组、集合等）中创建新的序列结构"""
"""列表推导式（List Comprehension）
new_list = [expression for item in iterable if condition]
"""
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # 输出：[4, 16, 36, 64, 100]

"""集合推导式（Set Comprehension）
集合推导式用于生成新的无序且不包含重复元素的集合。基本语法与列表推导式相似，只是用花括号 {} 替换方括号 []
new_set = {expression for item in iterable if condition}
"""
odd_numbers = {x for x in range(1, 11) if x % 2 != 0}
print(odd_numbers)  # 输出：{1, 3, 5, 7, 9}
"""字典推导式（Dictionary Comprehension）
字典推导式用于生成新的字典，其中每个键值对都是根据给定表达式计算得出的
new_dict = {key_expression: value_expression for item in iterable if condition}
"""
words = ["Hello", "World", "Python"]
lower_case_dict = {word.lower(): word for word in words}
print(lower_case_dict)  # 输出：{'hello': 'Hello', 'world': 'World', 'python': 'Python'}
print('------------------------')
"""要将对象转为迭代器类型，需要使用内置函数iter(object),迭代器允许通过next()方法按需逐个访问容器中的元素，直到所有原属都被访问完成"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
is_a = iter(a)
print(isinstance(is_a, abc.Iterator))  # 输出：True

"""迭代协议
iterator.__iter__(): 返回迭代器对象本身
iterator.__next__():从容器中返回下一项，当没有下一项时抛出StopIteration异常
注：一个对象只要支持上面两种方法，就是一个迭代器,对于迭代器，迭代器的元素只能‘消费一次‘。
"""


class FinNums():
    def __init__(self, num=0):
        self.num = num
        self.n = 0
        self.a = 3  # a,b时斐波那契数列的开始两项
        self.b = 5

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.num:
            self.n += 1
            self.a, self.b = self.b, self.a + self.b
            return self.a
        else:
            raise StopIteration


print(FinNums(3))
print(isinstance(FinNums(3), abc.Iterator), isinstance(FinNums(5), abc.Iterable))

fb = FinNums(10)
print(*fb, '\n', [*fb], '\n', (*fb,), "\n", {*fb})  # 对于迭代器，迭代器的元素只能‘消费一次‘。
print([*fb])  # 生成器表达式，生成器表达式可以被赋值给变量，但只能被迭代一次。 输出：[]

fbb = FinNums(10)
print(next(fbb))
print(next(fbb))
print(next(fbb))
print(next(fbb))
for i in fbb:
    print(i)  # 输出： 34 55 89 144 233; 5,8,13,21 已经迭代过一次了

"""不要对无限迭代器使用for循环和解包操作，需要用next()来迭代
迭代器并不像容器一样把所有的元素都先计算出来，它存储的是一个个元素的计算规则，在需要的时候才计算下一个元素，这样相对于容器来说节省空间
这种先记录计算规则，使用时才计算的方式称为惰性求值（lazy evaluation）或者惰性计算。
与容器相比，迭代器的宁一个特点是，它支持无限的元素，而容器则不支持。
"""
print('--------------------------------')
"""内置函数iter()用来生成迭代器，可以将字符串、列表、元组等--序列--转换为迭代器，也可以将迭代器转换为迭代器
供for循环、next()等进行迭代操作。

1、iter(iterable)->iterator
2、iter(callable,sentinel)->iterator
"""
"""方式1"""
mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
itm = iter(mlist)
print(next(itm))
print(next(itm))
print(next(itm))
print(next(itm))
print(next(itm))
print(next(itm))
it2 = iter(range(10, 18))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print('--------------------------------')

"""方式2：传人可调用对象和一个称为哨兵的对象，当调用可调用对象时，如果返回值等于哨兵对象，则终止迭代，引发StopIteration异常，否则继续迭代。
用for语句迭代时则会结束迭代，否则返回该值，如果哨兵是一个不可能到达的值，则迭代器会称为一个无限迭代器。
"""


def sentinel_objects():
    string = input('输入计算式进行计算，输入exit则退出:')
    return string


#
#
# for string in iter(sentinel_objects, 'exit'):
#     print('你的计算结果式：', eval(string))
#
# for string in iter(lambda: input('输入计算式进行计算，输入exit则退出:'), 'exit'):
#     print('你的计算结果式：', eval(string))


class Even:
    def __init__(self):
        self.count = 0

    def __iter__(self):  # 方法返回迭代器自身，这样当对 Even 实例进行迭代时，Python知道应该调用它的 __next__ 方法来获取下一个值。
        return self

    def __next__(self):  # 方法在每次调用时增加 count 变量的值2，并返回更新后的 count，从而产生偶数序列。
        self.count += 2
        return self.count

    __call__ = __next__  # 重载__call__方法，使Even类实例化后，可以像函数一样调用，即：even = Even()，even()


even = Even()
for i in iter(even, 10):  # 会先判断even.count是否等于10，
    # 如果不等于10，则even.count += 2，返回even.count，即2，然后for循环继续执行，直到even.count等于10，停止循环。

    print(i)

"""
每次循环迭代开始时，Python会调用迭代器的 __next__() 方法获取下一个值，并将其赋给 variable。
    有哨兵：Python会调用迭代器的 __next__() 方法获取下一个值，并与哨兵进行比较，如果相等，for 循环结束。
当迭代器没有更多的值可以返回时（即 __next__() 抛出 StopIteration 异常时），for 循环结束。
"""
# for i in iter(Even(), 21):  # 遇不到21，则一直循环下去
#     print(i)

print(isinstance(even, abc.Iterable))
print('--------------------------------')

num = iter(range(10, 18))
for _ in range(10, 19):
    print(next(num,
               '000000000000已经迭代完了00000000000000'))  # 输出：10 11 12 13 14 15 16 17 000000000000已经迭代完了00000000000000
    # next(iterator_obj, default) : 第二个参数是默认值

"""Generators
生成器是一种特殊的迭代器，可以使用yield表达式来返回值，每次调用next()方法时，生成器会返回yield表达式中的值，直到遇到下一个yield表达式。

生成器函数：定义与常规函数相同，区别在于它使用yeild语句返回值，而不是使用return来返回值
生成器表达式：与列表推导式类似，区别在于它使用()号来包裹，这也是没有元组推导式的原因(元组是不可变的)。
"""

import time


def func(n):
    for i in range(0, n):
        # yield相当于return，执行到yield i时停止，不执行arg = yield i这个赋值操作，下一次调用先执行这个赋值操作，再执行下一行代码
        arg = yield i  # 执行到yield i 时停止，不执行arg = yield i这个赋值操作，下一次调用先执行这个赋值操作，再执行下一行代码
        print('func', arg)


f = func(6)
print(f, type(f))
# while True:
#     print('main-next:', next(f))
#     time.sleep(2)
#     print('main-send:', f.send(100))  # send()函数传递的参数，先是作为yield表达式的值，再传递参数给arg。
#     time.sleep(10)

print('1----------------------1---------------------1')

"""
yeild from表达式是Python 3.3引入的一种新的语法
用法：在生成器（generator）中委托给另一个生成器或其他可迭代对象进行迭代。
    这个表达式使得生成器的编写更为简洁，并且提供了对子生成器异常处理和状态管理的支持。

以下是 yield from 表达式的几个关键特性：
1、--委托迭代--： 当在生成器函数内部使用 yield from iterable 时，该生成器会暂停自身的执行，
        并开始逐个产出 iterable 中的元素，直到 iterable 被完全遍历或抛出 StopIteration 异常为止。
        在此过程中，调用方从外部获取到的是 iterable 的直接产出值，而不是通过生成器间接产出。
    迭代完成之后，再执行 yield from 表达式之后的语句。
"""

"""基本用法"""


def gen_range(x):
    yield from range(1, x, 2)
    yield from range(2, x + 1, 2)


a = [*gen_range(10)]
print(a)  # [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]


def sub_generator():
    for i in range(5):
        print('sub_generator', i)
        yield i
        print('sub_generator', i)
        print('-----------------')


def main_generator():
    print('11111')
    yield from sub_generator()  # main_generator是一个生成器，yield from sub_generator() 是将迭代委托给sub_generator()进行。
    print('00000')


for item in main_generator():  # item 是 sub_generator 的直接产出返回值，不是main_generator 间接产出
    print(item)

print(iter(main_generator()), type(iter(main_generator())))

"""
print('00000') 这一行会执行是因为 yield from 在子生成器 sub_generator() 结束（即抛出 StopIteration 异常）后继续执行 main_generator() 函数的剩余部分。

当调用 for item in main_generator(): 时，迭代开始：
1、首先，main_generator 开始执行并打印 '11111'。
2、接着，yield from sub_generator() 使得 main_generator 委托给 sub_generator 进行迭代。每次循环通过 for item in main_generator()时，
    main_generator() 都会从 sub_generator 获取一个值 ，并将值给到item。
3、当 sub_generator 完成其内部的 for i in range(5): 循环并抛出 StopIteration 异常时，——yield from—— 知道子生成器已结束，并恢复到 main_generator() 的执行流。
4、因此，在 sub_generator 完成之后，main_generator 继续执行下一行代码，也就是打印 '00000'。
注意：由于 yield from 的异常处理特性，即使在遍历 sub_generator 期间发生异常，只要该异常未被捕获，也会导致 main_generator 恢复执行并到达 print('00000') 这一行

11111
sub_generator 0
0
sub_generator 0
-----------------
sub_generator 1
1
sub_generator 1
-----------------
sub_generator 2
2
sub_generator 2
-----------------
sub_generator 3
3
sub_generator 3
-----------------
sub_generator 4
4
sub_generator 4
-----------------
00000
"""

"""
2、异常传播
    如果在委派期间，-----被委托的生成器抛出了异常，那么这个异常会被--立即--传递给调用者，并且不会被当前生成器捕获------。
    同样地，如果调用者向当前生成器发送了一个异常（例如通过 throw() 方法），该异常会被透明地传递给被委托的生成器。
3、返回值处理
    当子生成器因 return 语句而终止并抛出带有值的 StopIteration 异常时，
    这个值会被作为 yield from 表达式的整体结果返回给调用者
"""


def sub_generator():
    for i in range(5):
        yield i
    return 'done'


def main_generator():
    result = yield from sub_generator()
    print(f"Sub-generator returned: {result}")


gen = main_generator()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # 4

# ... 迭代过程 ...
try:
    next(gen)  # Sub-generator returned: done
    # i=4，第6次迭代时, sub_generator() 没有更多的元素可供迭代,所以触发 StopIteration 异常
    # 同时sub_generator() 携带的返回值 'done' 将被传递给 main_generator() 中的 result 变量
except StopIteration as e:
    print('异常StopIterator', e.value)  # 异常StopIterator None

# gen1 = main_generator()
# for _ in range(6):
#     try:
#         print(next(gen1))
#     except StopIteration as e:
#         print(e.value)

"""
4、效率提升
    使用 yield from 可以避免手动维护内部迭代的状态和嵌套的 for 循环，简化了生成器代码，同时提升了性能，
    因为 Python 内部可以更高效地处理迭代转移。
总结来说，yield from 提供了一种将一个生成器的控制流无缝连接到另一个生成器或者任何其他可迭代对象的方式，
    让生成器的实现更加直观、灵活并且高效
"""

"""生成器表达式
与列表推导式类似，区别在于它使用()号来包裹，这也是没有元组推导式的原因(元组是不可变的)
"""
ge = (i for i in range(50) if i % 2 == 0)
print(ge, type(ge))  # <generator object <genexpr> at 0x1148ae400> <class 'generator'>
while True:
    try:
        print(next(ge))
    except StopIteration as e:
        print(e.value)
        break
print(i for i in range(50) if i % 2 == 0)  # <generator object <genexpr> at 0x11ec96f60>
print(sum([i for i in range(50) if i % 2 == 0]))  # 600

"""send()
send() 方法是Python生成器（generator）提供的一个特殊方法，它允许向生成器发送值并在生成器内部处理这些值。
    在生成器的生命周期中，send() 与 yield 表达式配合使用，使得生成器能够接收外部传入的数据并继续执行。

以下是 send() 方法的详细说明：
基本用法： 在生成器函数内部，通常会有一个或多个 yield 表达式，当生成器第一次被调用时，会从函数的第一行开始执行，
    直到遇到第一个 yield 表达式并暂停在那里。这时，你可以通过调用 send(value) 方法来恢复生成器的执行，
    并将 value 作为 yield 表达式的值然后赋值给接收变量n（比如 n = yeild i 注：n 只在使用send(value) 方法时才会有值，其他情况下，n 为None）。
"""


def simple_generator():
    i = 1
    value = yield i  # 第一次执行到这里会暂停，并返回0给调用者
    print(f"Received value: {value}")
    i += 10
    yield value + 1


"""第一次调用 next(gen11) 时，生成器开始执行直到遇到第一个 yield i 表达式。此时，它会返回 i 的值（即 1），并暂停执行。
当你调用 gen11.send(42) 时，生成器从上次暂停的地方继续执行，将 42 赋给 value 变量，并打印 "Received value: 42"。然后它执行到 yield value + 1 并暂停，返回 value + 1 的结果，即 43。
再次调用 next(gen11) 时，生成器试图继续执行，但在这个例子中，生成器函数已无更多的 yield 语句可以执行。因此，在尝试继续迭代时，由于没有更多的值可供生成，生成器抛出 StopIteration 异常，这是生成器结束其生命周期的标准方式。
"""
gen11 = simple_generator()
print(next(gen11))  # 输出：0
print(gen11.send(42))  # 输出：Received value: 42  ‘\n’43
# print(next(gen11))  # 没有可迭代的对象，抛出异常 StopIteration

"""注意，首次调用 send() 之前，需要先调用一次 next(gen) 或 gen.send(None) 来启动生成器并到达第一个 yield 语句。
返回值： 当调用 send(value) 方法时，------生成器会接收到 value 参数，并将其赋值给 yield 表达式的左侧变量。------
    然后生成器会继续执行到下一个 yield 表达式或者结束，此时 send() 方法会返回当前 yield 表达式的右侧值。
    
异常处理： send() 方法还可以用于在生成器内部抛出和捕获异常。如果传递给 send() 的是一个非None类型的异常对象，
    那么这个异常将在生成器内部的 yield 表达式处被引发。
"""

# def exception_handling_generator():
#     try:
#         value = yield
#         # ...
#     except ValueError as e:
#         print("Caught an exception:", e)


# gen = exception_handling_generator()
# gen.send(None)
# gen.throw(ValueError("A test exception"))

"""总结起来，send() 方法为生成器提供了一种灵活的方式进行通信，使得生成器可以在迭代过程中动态地接收和处理数据。
    同时，它也增强了生成器的控制流功能，使其能更好地与其他代码协同工作
"""

print('-----------------------')


def gent():
    i = 0
    while True:
        n = yield i
        i = i + (n or 2)


g = gent()
print(next(g))
print(next(g))
print(next(g))
g.send(10)
print(next(g))
print(next(g))
g.send(100)
print(next(g))
print('-------------------------2-----------------')
"""all(),any()
all(Iterable): 传入的可迭代对象的所有元素均为True（或：可迭代对象为空）时返回True，否则返回False。
any(Iterable): 转入的可迭代对象中，存在一个元素为True时返回True，否则返回False。
对字典来说：所有键都为False或者字典为空时，any()将返回False，否则返回True。 对字典来说，是以键作为判断依据（检测目标）。
"""
abc = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(all(abc))
print(all([0, False]))  # False
print(any([0, False]))  # False
print(all(()))  # True 空元组
print(all('asdhaisuh'))  # True
d = {0: False, 1: True, 2: False, 3: False, 4: False, 5: False}
print(all(d))  # False
print(any(d))  # True
a = [False, None, 0, 0.0, 0 + 0j, '', [], (), {}]
print(all(a))  # False
print(any(a))  # False
print(all(" "))  # True 空格字符串是True
print(not any([False, False]))  # True
print(not any([False, True]))  # False
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(all([i > 2 for i in b]))  # False
print(any([i > 2 for i in b]))  # True

"""作用与生成器表达式相同，只是生成器表达式是惰性求值的，而all()和any()是立即求值的。"""
print((i > 2 for i in b))  # <generator object <genexpr> at 0x116a33030>
print(all(i > 2 for i in b))  # False
print(all((i > 2 for i in b)))  # False

"""sorted()---不是原地操作
作用：按照特定顺序（升序或者降序）对给定的可迭代对象的元素进行排序，将其作为列表返回
sorted(iterable, key=None, reverse=False)

iterable：必需参数，指定需要排序的可迭代对象。
key：可选参数，指定一个（--函数--）或（--可调用对象--），该函数或对象将应用于 iterable 中每个元素上以获取比较值。例如，如果要根据字符串长度排序，可以使用 key=len
"""


def take_second(elem):
    return elem[1]


random1 = [(1, 3), (2, 2), (3, 1), (12, 98), (12, 98), (43, 1), (12, 3)]
sorted_list = sorted(random1, key=take_second)
sorted_list1 = sorted(random1, key=take_second, reverse=True)
print(sorted_list)
print(sorted_list1)
sorted_list3 = sorted(random1, key=lambda x: x[1], reverse=True)

# 对列表进行升序排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # 输出：[1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

# 对元组进行降序排序，注意元组本身不可变，但可以通过sorted()得到一个新的排序后的列表
tup = (9, 2, 7, 1, 5)
sorted_tup = sorted(tup, reverse=True)
print(sorted_tup)  # 输出：[9, 7, 5, 2, 1]

# 根据元素的某个属性排序
students = [{'name': 'Alice', 'grade': 85}, {'name': 'Bob', 'grade': 92}, {'name': 'Charlie', 'grade': 78}]
sorted_students_by_grade = sorted(students, key=lambda x: x['grade'], reverse=True)
print(sorted_students_by_grade)

"""reversed() 函数和 list.reverse() 方法：
reversed() 是一个内置函数，它可以返回给定序列的迭代器，并不直接生成新列表（不是一个原地操作）。常用于反向遍历序列，
或者配合其他构造函数（如 list()）生成反转后的列表。
要查看返回的这个迭代器的内容，需要迭代输出或者将其转化为列表

list.reverse() 是列表对象的方法，只能用于对列表进行原地反转。
示例：
"""

original_list = [1, 2, 3, 4, 5]
reversed_iterator = reversed(original_list)
print(list(reversed_iterator))  # 输出：[5, 4, 3, 2, 1]

"""迭代器（Iterator）和生成器（Generator）是两种不同的机制，它们都允许我们遍历数据集合而无需一次性加载所有数据到内存。但是，它们的内容并不能像查看列表或元组那样直接打印出来，因为它们设计为惰性计算和按需提供值
1、通过遍历迭代器或生成器，可以逐个访问迭代器中的元素，但是，迭代器只能访问一次。
2、如果确实需要查看生成器或迭代器所有的内容作为列表，可以将它们转换为列表。
"""
# 创建一个迭代器
it = iter([1, 2, 3])

# 逐个打印迭代器中的内容
try:
    while True:
        print(next(it))
except StopIteration:
    pass


# 定义一个生成器函数
def gen_numbers(n):
    for i in range(n):
        yield i * i


# 创建一个生成器对象并打印内容
gen = gen_numbers(5)
for number in gen:
    print(number)

iterator_content = list(iter([1, 2, 3]))
generator_content = list(gen_numbers(5))
print(iterator_content)
print(generator_content)

"""星号（*）解包操作可以用于迭代器和生成器的元素，将它们收集到一个可迭代对象（如列表、元组或集合）中。这种操作通常用于将多个值合并成单个序列。
对于迭代器或生成器，当其返回的是包含多个值的序列时，你可以使用星号解包来一次性获取所有剩余的值并放入一个新的容器中：
"""


# 示例：生成器函数
def my_generator():
    yield 1
    yield 'a'
    yield 2
    yield 'b'


# 创建生成器
gen = my_generator()

# 使用星号(*)解包将剩余的生成器内容放入一个列表
remaining_values = list(*gen)

# 输出：[1, 'a', 2, 'b']
print(remaining_values)
"""然而，在实际应用中，由于生成器是惰性计算的，你可能无法直接对整个生成器进行星号解包，除非你知道生成器会生成固定数量的元素。
更常见的情况是在for循环中逐个处理生成器的值，或者结合itertools.islice()等工具来限制要解包的数量。
如果你确实需要将生成器的所有元素一次性收集到一个列表中，推荐直接使用列表推导式或list()函数：
"""
all_values = list(my_generator())
