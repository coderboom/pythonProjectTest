"""
namespace
namespace   是从名称到对象的映射。
内置命名空间、模块命名空间、函数命名空间、类命名空间

一个命名空间的 作用域 是Python代码中的一段文本区域，它定义了其中的名称。
    即命名空间隐式的存在于一段代码中，而作用域则存在于这段文本区域内。

作用域
最内层作用域：包含局部名称，并首先在其中进行搜索。
外层闭包函数的作用域，包含“非局部、非全局”的名称，从最内层的哪个作用域开始，逐层向外搜索。
倒数第二层作用域，包含当前模块的全局名称
最外层（最后搜索）的作用域，是内置名称的命名空间

"""

print('11111')


def outer_func():
    y = 30  # 外层作用域变量

    def inner_func():
        nonlocal y  # 声明 y 是外层作用域变量
        y = 40  # 修改外层作用域变量 y 的值

    inner_func()
    return y


result = outer_func()
print(result)  # 输出：40


def outer_func1():
    y = 30  # 外层作用域变量

    def inner_func(x):
        y = x + 20
        # y = 40  # 修改外层作用域变量 y 的值
        return y

    print(inner_func(y))
    return y


result1 = outer_func1()
print(result1)  # 输出：40
"""
global 语句用于表明特定变量在全局作用域里，并应在全局作用域中重新绑定；
nonlocal 语句表明特定变量在外层作用域中，并应在外层作用域中重新绑定
"""


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
