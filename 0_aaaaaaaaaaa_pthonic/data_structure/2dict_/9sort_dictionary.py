"""排序字典"""
from collections import OrderedDict

d = {'a': 900, 'f': 9231, 'c': 43, 'b': 888}
print(d)
print(d.items())  # dict_items([('a', 900), ('f', 9231), ('c', 43), ('b', 888)])

"""默认是按键排序"""
sorted_d_items = sorted(d.items())  # [('a', 900), ('b', 888), ('c', 43), ('f', 9231)]
print(sorted_d_items)

sorted_d_items1 = sorted(d.items(), key=lambda x: x[1])
print(sorted_d_items1)
sorted_d_items1 = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(sorted_d_items1)
print('---------------------------------------------------')
"""Python标准库提供了 collections.OrderedDict 类，它可以保持插入顺序或者按照您提供的顺序进行存储。
    如果您希望按照特定顺序初始化一个有序字典，
可以使用如下方式：
"""

dictionary = d = {'a': 900, 'f': 9231, 'c': 43, 'b': 888}
sorted_keys = sorted(dictionary.keys())  # 获取排序后的键列表
print(sorted_keys)

ordered_dict = OrderedDict((k, dictionary[k]) for k in sorted_keys)  # 创建有序字典，键按照排序后的顺序

print('---------------------------------------------------')
import operator

"""
operator 模块提供了对标准算术、比较、位移以及其他类型的操作符的函数形式封装，
使得在需要直接调用操作符功能的场景（如列表推导、函数式编程、排序或自定义数据结构的实现等）下，可以以函数调用的方式使用这些操作符。
    这不仅提高了代码的可读性和简洁性，而且由于operator模块是用C语言实现的，其运行效率通常优于等效的Python代码

operator.itemgetter(index)：返回一个可调用对象，用于从序列（如列表、元组）中获取指定索引处的项。
    例如，getter = itemgetter(0); getter(tuple) 相当于 tuple[0]
"""
sorted_d_operator = sorted(d.items(), key=operator.itemgetter(1))
print(sorted_d_operator)

cc = [('asd', 123293712937, 1412312), ('qwe', 23, 1412312), ('oiqe', 1523, 917376),
      ('akdsn', 428, 74874),
      ('vdugd', 327487, 6108)]

# 使用 itemgetter 创建两个排序键：第一个键对应元组的第三个元素，第二个键对应元组的第二个元素
sorted_key = operator.itemgetter(2, 1)
# 使用sorted()函数 对cc列表进行排序，key=sorted_key
sorted_cc = sorted(cc, key=sorted_key)
print(sorted_cc)

"""对第三个元素生序排序，对第二个元素降序排序"""
# 使用 lambda 函数创建一个复合排序键：第一个键对应元组的第三个元素（升序），第二个键对应元组的第二个元素（降序）
sort_keys = lambda x: (x[2], -x[1])

# 使用 sorted 函数对 cc 列表进行排序，传入 sort_keys 作为 key 参数
sorted_cc = sorted(cc, key=sort_keys)

print(sorted_cc)
