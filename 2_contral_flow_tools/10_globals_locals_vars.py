"""globals(), locals() 和 vars() 在 Python 中都是用于访问和操作变量命名空间的函数。以下是它们的详细解释：
globals()
    globals() 函数返回一个全局作用域的字典的引用，其中包含了当前模块中所有全局变量（包括内置函数、模块级别的变量以及导入的模块）及其对应的值。
    在模块级别调用 globals() 时，它会返回该模块全局命名空间的所有内容。
    在函数内部调用 globals()，虽然仍然返回的是全局命名空间，但在函数内部对返回字典的修改可能会影响全局变量（除非在严格模式下运行，Python 3.7+），
    但最佳实践是尽量避免直接修改 globals() 返回的结果。
    -----可以更新当前作用域的全局变量-----

locals()
    locals() 函数返回当前局部作用域的字典，即包含当前函数或方法内定义的所有变量及其值。
    在函数内部调用 locals() 将返回包含当前函数内所有局部变量的字典。
    如果在全局作用域中调用 locals()，其结果与 globals() 是相同的，因为在全局作用域下没有局部变量的概念。
    注意：尽管 locals() 返回的是一个字典，但这个字典并不是真正的本地作用域引用，而是对当前作用域的一个副本。
    因此，对返回的字典进行修改---不会影响----实际的本地作用域中的变量。

vars()
    vars() 函数的行为取决于传入参数：
    若不带参数调用，其行为与 locals() 相同，返回当前作用域的局部变量字典。
    若传入一个对象作为参数，它会尝试获取并返回该对象的 __dict__ 属性，这通常用于获取一个类或实例的属性字典。
    对于用户自定义类型，如果支持特殊方法 __slots__ 而非普通的 __dict__，则 vars() 的行为可能会有所不同。
    ——————-可以更新当前作用域的局部变量——————————

总结来说，在处理变量作用域时，globals() 和 locals() 主要用于检查或调试代码中变量的状态，而 vars() 则提供了一种通用的方式
    来查看任何具有属性的对象的内部状态。不过，在实际编程中，直接修改这些函数返回的字典并不是推荐的做法，因为这样容易引发难以预料的副作用。
"""

print(globals())
print(locals())
print(vars())

"""
调试和分析代码：
    在编写或调试代码时，开发者可以使用这些函数来查看当前作用域中的变量及其值。这对于理解程序运行时的上下文状态非常有用。
    例如，在调试器中或通过交互式 shell（如 IPython），程序员可以快速查看全局变量或局部变量。
动态修改变量：
    尽管不推荐直接修改 globals() 或 locals() 返回的字典，但在某些特殊情况下，它们可能用于动态地创建或修改全局或局部变量。
    这在编写元编程、框架或工具脚本时偶尔会被用到，但需要注意的是这样做可能会降低代码的可读性和可维护性。
获取对象属性字典：
    使用 vars(obj) 可以获取一个对象的所有属性（对于有 __dict__ 属性的对象）。这个功能在需要遍历对象所有属性，
    或者需要将对象的属性转换为字典结构以便于处理时很有用。
实现内部机制：
    在底层编程或者实现自己的抽象语法树解析、编译器等工具时，会直接操作命名空间，这时 globals() 和 locals() 
    会成为构建或操纵执行环境的重要手段。
学习Python特性与原理：
    这些函数有助于了解 Python 中的作用域规则和名称查找机制，是学习 Python 内部工作原理的重要辅助工具。
    尽管这些函数提供了对作用域的灵活访问，但在实际开发中应谨慎使用，避免导致不可预见的行为和副作用。
    通常，更好的做法是遵循面向对象编程的原则以及明确的数据流控制，而不是依赖于动态修改全局或局部变量。
"""

Globals = 100

globals_list = [1, 2, 3]

print(globals())  # 返回的是一个字典

globals()['Globals'] = 9999999  # change value of Globals

print(globals())
print(Globals)
globals()['abcd'] = '12345'
print(globals())
print('------------------')
print(vars())
print('------------------')


def func():
    bar = 1111
    print(locals())
    print(globals())


func()
print('------------------')


class Foo():
    bar111 = 10
    gg = globals()
    ll = locals()
    vv = vars()  # 不带参数时与locals() 一样

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(locals())  # {'self': <__main__.Foo object at 0x120060a10>, 'a': 1, 'b': 2}
        print(globals())

    def add(self):
        return self.a + self.b


f = Foo(1, 2)
print(f.add())
print('------------------')
print('gg:', f.gg)
print('ff:', f.ll)
print('vv:', f.vv)
print(vars(f))
print('11111111111111111')
print(vars(Foo))
