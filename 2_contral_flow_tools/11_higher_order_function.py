"""常用高阶函数"""
from typing import Union

"""map()
map()函数是一个内置的高阶函数，它应用于一个或多个可迭代对象（如列表、元组、字符串等），并将每个可迭代对象中的元素传递给指定的函数进行处理。
    map()函数会返回一个新的--迭代器--，其中包含了对原始可迭代对象中所有元素应用该函数后的结果

map(function, iterable1, iterable2, ...)
    function: 这是一个接受一个或多个参数的函数，并且对于传入的每个元素都会调用这个函数。
    iterable1, iterable2, ...: 一个或多个可迭代对象。map()函数将按顺序从这些可迭代对象中取出相应位置的元素作为参数传给function。 
"""


def func(x):
    return x + 1


m = map(func, [1, 2, 3, 4, 5])
print(list(m), '\n', [*m])

mm = map(lambda x, y: x ** 2 + y ** 3, [1, 2, 3, 4, 5], (6, 7, 8, 9))
print(list(mm))


def add_coordinates(x, y):
    return (x, y, x + y)


numbers_x = [1, 2, 3]
numbers_y = [4, 5, 6]

coordinates_with_sum = map(add_coordinates, numbers_x, numbers_y)

# 打印结果
for coord in coordinates_with_sum:
    print(coord)

"""当我们调用 map(add_coordinates, numbers_x, numbers_y) 时，
    map() 函数将 numbers_x 和 numbers_y 中对应的元素（例如 numbers_x[0] 与 numbers_y[0]，numbers_x[1] 与 numbers_y[1] 等）打包成元组，
    并将这些元组作为参数传递给 add_coordinates 函数。
    map() 返回的新迭代器 coordinates_with_sum 包含了每次调用 add_coordinates 函数得到的结果。
在循环遍历 coordinates_with_sum 并打印结果时，可以看到每个元素是一个包含坐标及其和的元组。

"""
print('---------------------------')

"""filter()
filter()函数是一个内置的高阶函数，它用于对序列（如列表、元组、字符串等）或其他可迭代对象中的元素进行过滤操作，只保留那些使给定函数返回值为True的元素
    filter()返回的是迭代器，所以它并不会一次性生成所有结果并占用额外内存，而是按需计算，这在处理大量数据时更为高效
    
filter(function, iterable)
function: 这是一个接受单一参数并返回布尔值的函数，它将被应用于iterable中的每个元素上。如果函数返回True，则该元素会被包含在结果中。
iterable: 这是一个可迭代的对象，filter()函数会遍历这个对象，并对其中的每一个元素应用function。
"""
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# even_numbers 现在是 [2, 4, 6]


"""reduce() 
它应用于一个可迭代对象（如列表、元组或其他序列类型），通过连续地将前两个元素应用给定的二元操作函数来减少这个序列到单个值。
    reduce() 函数在 Python 2 中是内置函数，在 Python 3 中被移到了 functools 模块中。
    
reduce()只返回最后的结果，若要看到中间结果，可以使用accumulate()函数
"""
from functools import reduce


def my_function(accumulator, current_value):
    # 定义你的累积计算逻辑，返回新的累积值
    return accumulator + current_value  # 这是一个加法示例


sequence = [1, 2, 3, 4, 5]

# 使用reduce计算序列中所有数字的累加和
result = reduce(my_function, sequence)

print(result)  # 输出: 15
"""my_function 接受两个参数：当前累积值（accumulator）和序列中的下一个元素（current_value）。
    reduce() 函数首先将 sequence[0] 和 sequence[1] 传递给 my_function，得到的结果再与 sequence[2] 结合，
    如此反复直到处理完序列的所有元素。最终结果就是整个序列经过某种累积运算后得到的一个单一值。
如果提供了第三个可选参数 initial，那么它会被用作第一个 accumulator 的初始值
"""

from itertools import accumulate

sequence = [1, 2, 3, 4, 5]
result = [*accumulate(sequence, my_function)]
# 指定累积计算的初始值当 initial 被提供时，该值将作为第一个累积结果，并与序列中的第一个元素进行运算
result1 = [*accumulate(sequence, my_function, initial=0)]

print(result)
print(result1)
print('----------------------')

"""partial()
functools.partial() 函数是 Python 内置 functools 模块中的一个实用工具，用于创建偏函数（也称为部分应用函数）。
    它允许你预设某个函数的部分参数，并返回一个新的可调用对象，该对象在被调用时只需要提供剩余的参数。
    这在很多情况下非常有用，比如当你想要重用同一函数但其中某些参数经常保持不变时。
"""
from functools import partial


def original_function(a, b, c):
    return a + b + c


# 创建一个预先设置了 'c' 参数为 5 的偏函数
fixed_c_partial = partial(original_function, c=5)
# 现在只需传入 'a' 和 'b' 参数即可调用这个偏函数
result_c = fixed_c_partial(2, 3)
print(result_c)  # 输出: 10

"""固定多个参数： 你可以同时固定多个参数，新的偏函数将根据你提供的参数顺序从左到右依次固定"""
fixed_ab_partial = partial(original_function, 10, 20)  # 固定了 'a' 和 'b'
result2 = fixed_ab_partial(30)  # 这相当于调用 original_function(10, 20, 30)
"""
默认参数保留： 如果原始函数有默认参数，partial() 可以正确地处理这些参数，允许你在创建偏函数时覆盖或保留它们。

命名参数： 当原始函数使用关键字参数时，partial() 也可以通过名称来固定这些参数。
"""


def func(d, e=10, f=20):
    return d * (e + f)


named_partial = partial(func, f=30)  # 固定 'f' 参数为 30
result3 = named_partial(4, e=5)  # 这相当于调用 func(4, e=5, f=30)
"""行为和元信息： 返回的偏函数拥有与原函数相同的名字、文档字符串以及注解（如果存在）。
    它是一个可调用对象，可以像普通函数一样传递给其他需要函数作为参数的函数或方法。
总之，functools.partial() 是一种强大的函数式编程工具，能够帮助我们简化代码，提高灵活性，并且在许多场合下能提升代码的可读性和可维护性。
"""

print('--------------------------')
"""@cache
@cache 是一个装饰器（decorator），通常用于为函数或方法添加缓存功能。当一个函数被 @cache 装饰后，
    它的结果将会被存储起来，并且在后续调用时，如果传入相同的参数，会直接从缓存中返回之前计算的结果，而不是重新执行函数逻辑。
    这样可以显著提高程序性能，特别是在处理耗时较长但结果不常变的纯函数场景。
在 Python 标准库 functools 中，有一个名为 lru_cache 的装饰器，它可以实现类似的缓存功能。
    不过，@cache 并非标准库中的内置装饰器，而是需要根据具体上下文来确定其具体实现。
    例如，在某些第三方库（如 Django、Flask 等）或自定义代码库中，开发者可能会提供一个名为 @cache 的装饰器来实现缓存功能。
"""
from functools import lru_cache


# 定义一个基于 lru_cache 实现的 @cache 装饰器
def cache(func):
    """1 首先定义了一个名为 cache 的装饰器函数，它接受一个参数 func，即待装饰的原始函数。"""
    cached_func = lru_cache(maxsize=None)(func)  # 使用无限制大小的 LRU 缓存
    """2 在装饰器内部，我们使用 functools.lru_cache(maxsize=None) 来创建一个新的具有缓存功能的版本的 func。
    lru_cache 是 Least Recently Used Cache 的缩写，即最近最少使用缓存策略。
    maxsize=None 表示缓存大小没有限制，所有结果都将被缓存。"""
    return cached_func  # 3 """装饰器返回这个带有缓存功能的新函数 cached_func"""


@cache  # 4  下来，我们使用 @cache 装饰器语法来装饰函数 expensive_computation。
# 这相当于在编译阶段将 expensive_computation 作为参数传递给 cache 函数，
# 并将返回值（即带缓存功能的新函数）替换原来的 expensive_computation 定义
def expensive_computation(a, b):
    # 这是一个模拟耗时计算的函数
    print("Computing...")
    return a * b ** 2


# 第一次调用会进行实际计算并缓存结果
result11 = expensive_computation(3, 4)
print(result11)

# 5 第二次调用相同的参数将从缓存中获取结果，不会再次计算
result22 = expensive_computation(3, 4)
print(result22)
"""@cache 装饰器通过 functools.lru_cache() 来实现一个无限制大小的最近最少使用（LRU）缓存策略。
    对于 expensive_computation 函数来说，每次调用时都会检查是否已经为特定输入计算过结果，从而避免重复计算。
"""
print('-----------------------')
"""@singledispatch
@singledispatch 是 Python 中用于实现多态（polymorphism）的一种装饰器，它来自 functools 模块。
    这个装饰器允许你定义一个函数作为“主”函数，并为不同类型的输入参数提供不同的实现版本。
"""
from functools import singledispatch


@singledispatch
def my_function(arg):
    # 这是默认处理函数，当没有找到特定类型处理器时调用
    print(f"Default handler for {type(arg)}: arg = {arg}")


# 为特定类型注册处理函数
@my_function.register(int)
def _(arg: int):
    print("Handling an integer:", arg)


@my_function.register(str)
def _(arg: str):
    print("Handling a string:", arg)


# 调用函数
my_function(10)  # 输出：Handling an integer: 10
my_function("Hello")  # 输出：Handling a string: Hello
my_function([1, 2, 3])  # 输出：Default handler for <class 'list'>: arg = [1, 2, 3]
"""在这个例子中，my_function 是一个多态函数，通过 @my_function.register() 方法我们分别为整数和字符串类型注册了专门的处理函数。
    当传入的参数类型匹配到已注册类型时，将调用对应的处理函数；如果未找到匹配的处理函数，则会调用默认处理函数。"""

# @singledispatch
# def join_test(arg1, arg2):
#     print("Default handler for", type(arg1), type(arg2), arg1, arg2)
#     result111 = [arg1, arg2]
#     return result111
#
#
# @join_test.register(int)
# def _(arg1: int, arg2: int) -> int:
#     print("Default handler for", type(arg1), type(arg2), arg1 + arg2)
#     return arg1 + arg2
#
#
# @join_test.register(str)
# def _(arg1: str, arg2: str) -> str:
#     print("Default handler for", type(arg1), type(arg2), arg1 + arg2)
#     return arg1 + arg2
#
#
# @join_test.register(int, str)
# def _(arg1: int, arg2: str) -> str:
#     print("Default handler for", type(arg1), type(arg2), str(arg1) + arg2)
#     return str(arg1) + arg2
#
#
# @join_test.register(str, int)
# def _(arg1: str, arg2: int) -> str:
#     print("Default handler for", type(arg1), type(arg2), arg1 + str(arg2))
#     return arg1 + str(arg2)


"""
类型注册顺序：singledispatch 是基于第一个参数（arg1）的类型进行分发的，而不是考虑两个参数的类型组合。
    因此，为 (int, str) 和 (str, int) 分别注册处理器在这里是不必要的，因为它们都只会匹配到第一个参数为 int 或 str 的处理器。

重载行为：由于单一调度只关注第一个参数，所以对于像 join_test(1, 'None') 这样的调用，
    它会根据 int 类型调用相应的处理器，而不是考虑到第二个参数 str 类型并调用一个特定于 (int, str) 的处理器。
    这里的行为实际上与预期不符，因为已经分别定义了对 (int, str) 和 (str, int) 的处理方式。"""


@singledispatch
def join_test(arg1, arg2):
    print("Default handler for", type(arg1), type(arg2), arg1, arg2)
    result111 = [arg1, arg2]
    return result111


@join_test.register(int)
def _(arg1: int, arg2) -> Union[int, str]:
    if isinstance(arg2, int):
        print("两个数k字的和是:", arg1 + arg2)
        return arg1 + arg2
    else:
        print("string 表示:", str(arg1) + arg2)
        return str(arg1) + arg2


@join_test.register(str)
def _(arg1: str, arg2) -> str:
    print("Handling strings:", arg1 + str(arg2))
    return arg1 + str(arg2)


# 测试调用
print(join_test(1, 2))
print(join_test('adadada', 'qwer'))
print(join_test('hello---', 2))
print(join_test(1, 'None'))
