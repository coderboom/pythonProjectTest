import sys

import date_structure.yeild_test as yeild_test
from date_structure.yeild_test import func as yeild_test_func
import time

# f = yeild_test.func(6)
# while True:
#     print('main-next:', next(f))
#     time.sleep(2)
#     print('main-send:', f.send(100))  # send()函数传递的参数，先是作为yield表达式的值，再传递参数给arg。
#     time.sleep(10)
'''
dir() 函数
用于返回模块的属性名列表(属性名会排序)。
属性名列表包含变量、函数、类、其它导入的模块、模块级的变量和常量

如果不提供参数调用 dir(), 它将列出当前作用域内的变量、方法和定义的类型。# 即模块的命名空间中有定义的
当传入一个模块名时，它会返回该模块内定义的所有名称列表。
当传入一个类或对象实例时，它会返回类或对象中定义的所有方法和属性名称列表

'''

print(sys.path)
print(dir(yeild_test))  # dir()函数返回一个包含模块中所有方法的列表。
print(dir())
print(dir(sys))
print(dir(sys.path))
print(sys.builtin_module_names)

"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
*objects：可变数量的位置参数，表示要打印的内容，可以是任意类型的数据，如字符串、数字、列表、字典等。多个对象之间会按照指定的分隔符进行连接。
sep=' '：可选参数，用于设置多个对象之间的分隔符，默认为空格。例如，print(1, 2, 3, sep=',')会输出1,2,3。
end='\n'：可选参数，设置输出结束后追加的内容，默认为换行符\n。比如，print("Hello", end='')会在“Hello”后面不换行。
file=sys.stdout：可选参数，指定输出的目标流，默认为标准输出（屏幕）。你可以将其替换为一个打开的文件对象，以将内容输出到该文件。
flush=False：可选布尔参数，如果设置为True，则强制立即将缓冲区的内容输出到目标流，而不是等待缓冲区满或者特定时机再输出
"""
