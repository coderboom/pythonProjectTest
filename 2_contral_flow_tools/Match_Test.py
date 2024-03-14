from math import pi

import time

TOTAL = 0
for i in range(100):
    TOTAL += i
print(TOTAL)
#
# list_num = [i for i in range(101)]
# for num in list_num:  # unm代表叠戴对象里面的元素
#     print(num)
"""
for 循环 主要用于遍历
任何序列（如列表、元组、字符串）
可迭代对象（包括字典、集合、文件对象等）
"""
# for variable in iterable:
#     # 这里是循环体内的语句块
#     statement(s)
"""
variable：在每次循环迭代时，变量会被赋予iterable中的下一个值。
iterable：是一个可迭代的对象，可以是列表、元组、字符串、range对象，或者是实现了迭代协议的自定义对象等。
"""
names = ('tome', 'asdih', 'oeroqwu')
ages = [12, 34, 87]
sorces = {123, 431, 987}

"""Zip()函数，将两个序列对齐为对应的建值
zip() 函数在 Python 中用于将多个可迭代对象（如列表、元组、字典视图等）的元素打包成一个个元组，并返回一个 zip 对象（在 Python 3 中，如果不转换为列表或类似容器，它会作为迭代器使用）。
这个功能可以看作是将不同序列“对齐”并压缩成一个新的结构。
然而，集合（set）是一种无序且不包含重复元素的数据结构。直接与 zip() 结合使用的场景可能并不常见，
因为集合本身不能被直接用作 zip() 的参数，因为集合中的元素没有顺序。
但你可以通过先将集合转换为可迭代的有序数据结构（如列表），然后将其与其他可迭代对象一起传递给 zip()：

"""
a = zip(names, ages)  # zip()函数，将两个序列对齐为对应的建值
b = zip(names, sorces)  # zip()函数，将两个序列对齐为对应的建值
print(a)
print(b)
print(list(a))
print(tuple(a))
print(dict(a))
print(list(b))
print(tuple(b))
print(dict(b))

print('-----------------------------------')
list_num = ['sdad', 'asdiueb', 'vriebbsd', 'vidhqwey', 'siuhdwbei']
for index, value in enumerate(list_num):
    # print(f'index:{index},value:{value}') # f字符串
    print('index:{index}, value:{value}'.format(index=index, value=value))

list_num.insert(2, str(124121))
print(list_num)

# list_num.append(123123123)
list_num.sort(reverse=True)  # 无法对数字和字符串进行排序
print(list_num)
