"""
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
/ 之前是仅限位置形参
/和*之间是 位置或关键字 形参 。
*之后是关键字形参
"""
import functools

print((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

"""
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
    
variadic(可变参数 *args) 参数用于采集传递给函数的所有剩余参数，因此，它们通常在形参列表的末尾。
*args 形参后的任何形式参数只能是仅限关键字参数，即只能用作关键字参数，不能用作位置参数
"""
print('----------------------------')
"""
# 解包实参列表

函数调用要求独立的位置参数，但实参在列表或元组里时，要执行相反的操作。例如，内置的 range() 函数要求独立的 start 和 stop 实参。
如果这些参数不是独立的，则要在调用函数时，用 * 操作符把实参从列表或元组解包出来
"""
args = [1, 10, 2]
print(list(range(*args)))


def f1(a, b, c, *d):  #
    print(a, c, b, d)  # 1 3 2 (4, 234, 67, 563, 52, 32, 42, 4)


args1 = [1, 2, 3, 4, 234, 67, 563, 52, 32, 42, 4]
f1(*args1)  # 多余的参数将被 *d 收集，以元组的方式存储未分配的变量。 # 1 3 2 (4, 234, 67, 563, 52, 32, 42, 4)
"""1、使用星号 * 对 args1 列表进行解包。这意味着，在函数调用时，列表中的元素会被依次取出并分别赋值给对应的函数参数。
第一个元素 1 被赋值给 a
第二个元素 2 被赋值给 b
第三个元素 3 被赋值给 c
剩余的所有元素 [4, 234, 67, 563, 52, 32, 42, 4] 被打包成一个元组，并赋值给 d
"""


def f2(a, b, *c, d):  #
    print(a, b, c, d)


f2(*args1, d=3)

"""python 类型注解
是Python 3.5版本及更高版本引入的一种功能，它允许在代码中为变量、函数参数和返回值声明预期的数据类型。
    类型注解的目的不是强制执行类型检查（Python仍然是动态类型语言），而是作为一种静态类型提示机制，
    帮助开发者编写更易于理解和维护的代码，并且能够与各种静态类型检查工具（如mypy）以及IDE集成，提供更强的自动补全、错误提示和代码分析能力
"""
"""变量类型注解"""
# age: int = 10
# name: str = 'zhangsan'

"""函数类型注解
可以注解形参的类型，以及函数的返回值类型。
"""


def greet(name: str, city: str = '北极') -> tuple:
    return name, city


from typing import List


def process_user(users: List[dict]) -> None:
    for users in users:
        print(users['name'])


"""可调用对象
Python中，可调用对象是指那些能够使用调用运算符()进行调用并执行特定操作的对象。当对一个对象进行调用时，
    Python会查找该对象上是否定义了特殊方法__call__()，如果存在这个方法，则认为该对象是可调用的。
以下是Python中常见的几种可调用对象类型：

用户自定义函数：
    使用 def 关键字定义的函数。
    使用 lambda 表达式创建的匿名函数。
内置函数：
    由C语言实现并内置于Python解释器中的函数，例如 len(), sum(), print() 等。
方法：
    类实例上的函数，即绑定到类实例的函数，它们可以通过实例进行调用。
类：
    当你通过()调用一个类时，Python会创建并返回一个新的实例（通过调用类的__new__()方法和随后的__init__()方法）。
    
实现了__call__()方法的类实例：
    如果一个类定义了__call__()方法，则其实例也可以成为可调用对象。当对该实例进行调用时，就会执行__call__()方法内的代码。
生成器函数：
    通过包含yield语句的函数可以生成生成器对象，这些生成器也是可调用的，并且每次调用都会返回下一个值。
其他可调用对象：
    在某些情况下，还有其他类型的对象可能被设计为可调用的，只要它们定义了适当的__call__()方法，如一些第三方库或框架中封装的操作等。
"""


def say_hello(name):
    return f"Hello, {name}!"


# 调用该函数
print(say_hello("Alice"))  # 输出：Hello, Alice!

greet = lambda name: f"Hello, {name}!"
# 调用lambda函数
print(greet("Bob"))  # 输出：Hello, Bob!


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}."


p = Person("Charlie")
# 调用方法
print(p.introduce())  # 输出：My name is Charlie.


class CallableObject:
    def __init__(self, value):
        self.value = value

    def __call__(self, multiplier=1):
        return self.value * multiplier


obj = CallableObject(5)
# 调用实例
print(obj())  # 输出：5
print(obj(2))  # 输出：10


class Counter:
    count = 0

    def __new__(cls):
        cls.count += 1
        return cls

    @classmethod
    def get_count(cls):
        return cls.count


# 类被当作可调用来创建新实例
counter_instance = Counter()
print(counter_instance.get_count())  # 输出：1


def simple_generator():
    for i in range(3):
        yield i


gen = simple_generator()
# 调用生成器
for num in gen:
    print(num)  # 分别输出：0, 1, 2

"""高阶函数
是指那些可以接收一个或多个函数作为参数，并且可能返回一个新的函数作为结果的函数。
    这类函数增强了程序的抽象能力和代码复用性，是函数式编程的重要特性之一。
    
高阶函数的两个主要特点如下：
1、接受函数作为参数：高阶函数能够将其他函数作为输入，这意味着它可以操作或者利用这些被传递进来的函数的能力来完成更复杂的逻辑。
    例如，内置的sorted()函数就可以接收一个key参数，该参数是一个函数，用于定义排序时使用的依据
"""


def square(x):
    return x * x


numbers = [1, 2, 3, 4]
sorted_numbers = sorted(numbers, key=square)  # 使用square函数作为key参数
print('------------------')
"""返回函数作为结果：
高阶函数也可以生成并返回新的函数对象，这个新函数可能是通过某种方式对传入函数进行封装、组合或修改得到的。
比如定义一个函数，它根据用户提供的运算符创建一个新的计算函数。"""


def operation_factory(func):
    def calculate(a, b):
        return func(a, b)

    return calculate


add = operation_factory(lambda a, b: a + b)  #
print(add(3, 5))  # 调用add(3, 5)，就相当于调用calculate(3, 5)


def operation1_factory(func):
    def wrapper(a, b):
        return func(a, b)

    return wrapper


reduce = operation1_factory(lambda x, y: x - y)  # reduce =wrapper，
print(reduce(10, 5))  # 调用reduce(10,5) ,就相当于调用wrapper(10,5)

"""常见的Python内置高阶函数包括但不限于：map(), filter(), reduce()（在functools模块中），
    以及装饰器（虽然它们不是直接调用返回函数，但装饰器本质上也是一种高阶函数应用）
"""
print('-----------')

"""装饰器
装饰器（Decorator）是一种特殊类型的函数或类，它允许我们在不修改原函数源代码的基础上，向现有函数添加新的功能。
装饰器本质上是一个接收函数作为输入，并返回新函数的高阶函数。这个新函数通常会包装原始函数，在调用原始函数前后执行额外的操作
"""


def my_decorator(func):
    def wrapper(*args, **kwargs):
        # 在调用原始函数前执行的操作
        print("Before function call")

        result = func(*args, **kwargs)  # 调用原始函数，如果原始函数有返回值，先用result保存返回值，再返回result

        # 在调用原始函数后执行的操作
        print("After function call")
        return result

    return wrapper


# 最关键的一步处理————————当解释器遇到 @my_decorator 符号时，它实际上会在--编译阶段--执行如下语句
#    example_function = my_decorator(example_function)
#    这样，便意味着原始定义的 example_function 函数，作为参数被传递给装饰器函数 my_decorator，
#    然后 my_decorator 返回一个新的包装函数（即 wrapper 函数）并将其赋值给 example_function。
# 因此，原始的 example_function 函数在经过装饰器处理后，其功能被替换为装饰器内部定义的 wrapper 函数。
# 当调用 example_function() 时，实际上是执行了 wrapper() 函数，并且这个新函数在调用原始函数的前后分别执行了额外的操作，如打印日志信息
@my_decorator
def example_function():
    print("This is the original function.")


example_function()

print('9999999999')

"""带参数的装饰器"""


def logged(prefix=""):
    # 定义装饰器函数logged，它接受一个可选参数prefix，默认为空字符串
    # 这个装饰器的主要作用是在被装饰的函数执行前后打印一条包含函数名以及传入前缀的日志信息
    def decorator(func):
        # 在logged内部定义一个名为decorator的闭包函数，它接收一个需要被装饰的函数作为参数func。
        def wrapper(*args, **kwargs):
            # decorator函数内部又定义了名为wrapper的函数，它是实际用于替换原函数的新函数。
            # wrapper在调用原函数前后分别打印日志，并返回原函数的执行结果。

            print(f"{prefix} - Entering {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{prefix} - Exiting {func.__name__}")
            return result  # wrapper函数返回原始函数的执行结果

        return wrapper  # decorator 函数最后返回 wrapper 函数，这样当使用 logged 装饰其他函数时，实际上是用 wrapper 函数替换了原来的函数

    return decorator


"""
核心思想是：最外层的函数logged()接受参数prefix，并将他们作用在内部装饰器函数上面。
          内层的函数decorate()接受一个函数func作为参数，然后在函数上面放置一个包装器。
          ————这里的关键点是，包装器是可以使用传递给logged()的参数的。
然后返回一个闭包函数decorator，这个闭包函数接收一个函数作为参数func，然后返回一个新函数wrapper。
"""


# 使用无参数的装饰器
@logged()  # 解释器遇到@logged()时，做了如下隐匿操作， add = logged()(add)，
# 即add被替换成了 logged()函数返回的decorator函数返回的wrapper函数，调用add()其实就是在调用wrapper()函数
def add(a, b):
    # Python解释器会将 add 函数作为参数传递给 logged 装饰器函数。
    # 由于 logged 函数返回一个新的内部函数（即闭包 decorator 返回的 wrapper 函数），因此 add 函数会被这个新函数替换。
    return a + b


# 使用带有参数的装饰器
@logged(prefix="DEBUG:")
# 解释器遇到@logged(prefix="DEBUG:")时，做了如下隐匿操作，subtract = logged(prefix="DEBUG:")(subtract)，
# 即subtract函数被替换成了 logged()函数返回的decorator函数返回的wrapper函数
def subtract(a, b):
    return a - b


print(add(3, 5))  # 输出：DEBUG: - Entering add, DEBUG: - Exiting add, 8
print(subtract(10, 5))  # 输出：DEBUG: - Entering subtract, DEBUG: - Exiting subtract, 5

"""
在装饰器 logged 的设计中，选择不在 decorator(func) 函数内部直接设置 prefix="DEBUG:" 的原因是
    装饰器通常需要具有灵活性，以便能够在不同场景下以不同的方式装饰函数。
    通过将前缀作为参数传递给装饰器，可以在使用装饰器时指定不同的前缀值，
    这样可以实现一个装饰器应用于多个函数且具有不同日志前缀的需求。
"""
print('-------------------------------------')


# 创建一个带参数的装饰器
def logged_decorator(name='debug', message='debug message'):
    def decorator1(func):
        def wrapper(*args, **kwargs):
            print('start func:', func.__name__, name, message)
            result = func(*args, **kwargs)
            print('end func:', func.__name__, name, message)
            return result

        return wrapper

    return decorator1


@logged_decorator()
def pppp(list_bbb):
    for i in list_bbb:
        print(i)


# 创建一个不带参数的装饰器
def decorator1(func):
    def wrapper(*args, **kwargs):
        print('start func:', func.__name__)
        result = func(*args, **kwargs)
        print('end func:', func.__name__)
        return result

    return wrapper


@decorator1
def pppp2(list: list):
    return list[0] + list[1]


print(pppp2([1, 2]))
"""匿名函数"""

add1 = lambda x, y: x + y
add2 = (lambda x, y: x + y)(1, 2)  # lambda表达式后面还可以加参数，但必须有等号，等号后面是函数体，函数体内部可以直接调用前面的参数
add3 = lambda x, y=10: x + y  # 可以给lambda函数指定默认值

a = lambda x, y: x if x > y else y
b = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
c = [1, 2, 3, 9, 4, 5, 6, 7]
c1 = map(lambda x: x ** 2, c)
print(type(c1), '\n', list(c1), '\n', [*c1])

c2 = filter(lambda x: x % 2 == 0, c)
print(type(c2), '\n', list(c2), '\n', [*c2])

from functools import reduce

c3 = reduce(lambda x, y: x * y, c)  # 累积迭代方法reduce()函数，接收两个参数，一个是函数，一个是序列
print(type(c3), c3)

n = lambda x, y=iter('asaishasbdaidbus'): next(y)  # n
print(n(None))  #

"""assert 断言
assert 是一个用于断言或验证程序中某个条件是否满足的语句。它的主要目的是在开发阶段作为一种调试辅助工具，
确保代码运行时的某些关键假设始终为真。当断言失败（即表达式求值结果为 False）时，会立即抛出 AssertionError 异常。

assert expression[, message]
expression：这是一个布尔表达式，表示需要被检查的条件。如果这个表达式的值为 True，则程序继续执行；如果为 False，则触发异常。
message（可选）：如果提供了第二个参数，那么它会被作为 AssertionError 异常的消息内容，在异常抛出时显示出来。
"""


def divide(x, y):
    assert y != 0, "Divider cannot be zero!"
    return x / y


result = divide(10, 2)  # 正常情况，y不为0，不会触发异常
print(result)

try:
    result = divide(10, 0)
except AssertionError as e:
    print(e)  # 当y为0时，触发异常，输出"Divider cannot be zero!"
"""使用时机与目的：
在函数内部，可以用来验证输入参数的有效性，例如参数非空、类型正确等。
验证程序中的中间状态或计算结果符合预期，尤其是在复杂的逻辑分支中，有助于快速定位潜在错误。
测试代码中，断言常常用于确认单元测试的结果与预期一致。
需要注意的是，尽管断言对于调试和确保程序逻辑正确性非常有用，但在生产环境中，
默认情况下Python会忽略所有的 assert 语句（通过 -O 或 -OO 标志启用优化时）。
因此，不应依赖 assert 来执行关键的错误处理或业务逻辑控制。
"""

"""常用内置函数"""
print('-------------------------------------')
"""zip()
将两个或两个以上的可迭代对象按照位置一一组合起来，它返回一个zip对象。是一个元组迭代器，只能消费一次
"""
z = zip()
print(type(z), '\n', list(z))
z = zip([1, 2, 3, 4])
print(type(z), '\n', list(z))  # [(1,), (2,), (3,), (4,)]

z = zip([1, 2, 3], [4, 5, 6, 7])
print(type(z), '\n', list(z))  # [(1, 4), (2, 5), (3, 6)]
z = zip([1, 2, 3, 8], [4, 5, 6])
print(type(z), '\n', list(z))  # [(1, 4), (2, 5), (3, 6)]
z = zip([1, 2, 3, 8], [4, 5, 6, 7])
print(type(z), '\n', list(z))  # [(1, 4), (2, 5), (3, 6), (8, 7)]

"""将多个序列按照位置组合在一起，以便将他们进行迭代和转化为字典"""
name = ['a', 'b', 'c', 'd']
age = [10, 20, 30, 40]
print([*zip(name, age)])  # [('a', 10), ('b', 20), ('c', 30), ('d', 40)]

dict_if = dict(zip(name, age))
print(type(dict_if), '\n', dict_if)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40}

for key, value in dict_if.items():
    print(key, value)

lity = [123, 5, 231, 26, 5]
lucy = [38, 237, 45123, 65]
amy = [129993, 45123, 165, 2523]

z = zip(name, age, lucy, amy, lity)
print(list(z), '\n', list(
    z))  # [('a', 10, 38, 129993, 123), ('b', 20, 237, 45123, 5), ('c', 30, 45123, 165, 231), ('d', 40, 65, 2523, 26)]
"""zip(),是按照最短计算法，所以，如果列表长度不一致，就会截取最短的列表
如果想计算法是按照最长计算法，可以使用itertools.zip_longest()函数"""
lity = [123, 5, 231, 26, 5, 2131, 5, 1, 34, 2, 1, 23, 134, 1, 21, 231, 23, 12]
lucy = [38, 237, 45123, 65]
amy = [129993, 45123, 165, 2523]

import itertools

z = itertools.zip_longest(lity, lucy, amy, fillvalue=999999999)  # fillvalue: 填充值,默认None
print(list(z), '\n', list(z))
print('------------------------------------')
"""enumerate()
将计数器添加到可迭代对象，每个元素连同计数器（或者称为索引）组成元组，并返回枚举对象。
"""
names = ['a', 'b', 'c', 'd']
enu_names = enumerate(names)  # 返回一个枚举对象,对应的索引和值以元组的形式成对存在,可以使用list()转换为列表
print(type(enu_names), '\n', list(enu_names))  # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

print([*enumerate(names, start=1)])  # start: 开始计数的数字,默认为0
print([*enumerate(names, start=10)])  # 从索引为10开始计数

print('-----------------------------------------')
"""eval() 执行一个以字符串表示的表达式，返回表达式的值
eval()非常强大，也非常危险，使用是需要格外小心，因为可以执行任何python代码
"""
print(eval('1+2*3'))
print(eval('[*"12312312313"]'))
print(eval('[i for i in range(10)]'))

"""exec() AND compile()
ecxe() :可执行存储在字符串或文件中的python语句，相比evel()，可以执行更复杂的python代码，其返回值永远是None，除非打印返回值。
    是python留给用户传入代码字符串的一个借口。
    
compile()：将python代码编译成字节码，返回一个code对象，可以使用eval()、exec()等函数执行。
"""
exec('a=1\nb=2\nprint(a+b)')  # 输出：3

code_string = 'a=5\nb=6\nsum=a+b\nprint("sum=",sum)'
code_object = compile(code_string, 'sumstring', 'exec')
"""
code_string:
    这是一个包含Python源代码的字符串。在您的例子中，它定义了变量 a 和 b，计算它们的和，并将结果存储在 sum 中，然后打印出 "sum=" 后跟求和的结果
    
filename (在您的例子中为 'sumstring'):
    这个参数代表源代码所在的文件名，通常是一个字符串。虽然在这里并没有实际的文件，但在错误报告或其他需要引用源代码位置的情况下，它会被用作信息来源。这个参数在调试时特别有用，因为它可以帮助追踪代码来自哪个文件（即使实际代码是在字符串中）。
    
mode (在您的例子中为 'exec'):
    指定编译模式，有三种可能的模式：
        'exec': 编译整个程序或一个模块，这是最常见的模式，用于执行一系列语句。
        'eval': 编译单个表达式，返回其计算结果。
        'single': 编译单行交互式的语句，例如在REPL（Read-Eval-Print Loop）环境中使用的语句。
        
compile(code_string, 'sumstring', 'exec') 的作用是将给定的代码字符串编译成可以在当前环境下执行的字节码对象。这个字节码对象可以稍后通过 exec() 函数执行。
"""

exec(code_object)
eval(code_object)
