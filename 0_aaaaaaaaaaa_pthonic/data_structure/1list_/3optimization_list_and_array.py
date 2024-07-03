"""
列表和数组的优化
1、使用列表推导有什么特别之处
2、使用列表推导而不是map（）和filter（）
3、使用负索引进行快速反向访问
4、确定可迭代性的all和any的使用
5、使用*运算符操作剩余序列
6、使用array.array获取基本类型数组
7、带str的不可变unicode字符数组
8、带有bytearray的单字节可变序列
9、使用字节作为不可变的单字节序列
"""
import itertools
import numpy as np

print('----------------------使用列表推导有什么特别之处-----------------------')
"""列表推导式（List Comprehension）是一种简洁且强大的Python特性，用于生成新的列表。当列表推导式中包含多个 for 循环和 if 条件语句时，
    它允许您在单行代码中实现对多个嵌套循环以及条件判断的组合操作，以生成满足特定条件的新列表元素。

理解这类复杂列表推导式的要点如下：
**1. 嵌套结构：多个 for 循环在列表推导式中按照从左到右的顺序依次嵌套。最左边的循环外部，最右边的循环内部。每个循环负责遍历一个相应的可迭代对象。
"""
outer_list = [1, 2, 3]
inner_list = ['a', 'b', 'cd']

result = [(i, j) for i in outer_list for j in inner_list]
print(result)
"""
**2. 条件过滤：if 条件语句出现在所有 for 循环之后，用于筛选满足条件的元素。只有当条件为 True 时，当前循环变量组合对应的元素才会被添加到新列表中。
"""
result1 = [(i, j) for i in outer_list for j in inner_list if i * len(j) > 2]
print(result1)
"""
**3. 执行顺序：列表推导式的执行逻辑遵循从左到右、从外到内的顺序：
    先执行最左边的 for 循环，依次取其可迭代对象的每一个元素。
    对于外部循环的每一个元素，执行内部的 for 循环，遍历其可迭代对象的所有元素。
    在内部循环中，对当前内外循环变量的组合应用 if 条件判断。如果条件为 True，则根据列表推导式的表达式生成一个新的元素，并将其添加到结果列表中；
        否则跳过该组合，继续处理下一个内部循环的元素。
    完成内部循环后，继续处理外部循环的下一个元素，重复上述过程，直至所有外部循环元素遍历完毕。
    
**4. 嵌套层次：理论上，列表推导式可以包含任意数量的嵌套 for 循环，形成多层嵌套结构。
    每增加一层循环，就相当于增加一个维度的遍历。
    同时，可以有多个 if 条件语句，它们之间可以是逻辑与（and）的关系，也可以通过嵌套 if-elif-else 结构实现更复杂的逻辑。
"""
nested_lists = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]
result2 = [
    z for i in nested_lists
    for j in i
    for z in j
    if z % 2 == 0
]
print(result2, np.array(nested_lists).shape)
"""5. 代码可读性：尽管列表推导式能够以简洁的语法实现复杂的逻辑，但过度复杂的列表推导可能会降低代码的可读性。
    对于过于复杂的嵌套循环和条件判断，考虑使用传统的多层循环和条件语句，或者将部分逻辑封装为单独的函数，以保持代码清晰。

总之，理解列表推导式中多个 for 循环和 if 条件语句的关键在于把握它们的嵌套关系、执行顺序以及条件过滤逻辑。
    这样的结构允许您在一行代码中高效地生成满足特定条件的新列表，但应确保代码保持清晰易懂。在追求简洁的同时，不要忽视代码的可读性和维护性。
"""

print('--------------')

"""列表推导（List Comprehension）是Python中一种简洁而强大的创建新列表的方式，
    它允许在一行代码中完成对现有数据结构（通常是列表、元组、集合、字典等）的遍历、过滤和映射操作。
列表推导有以下特别之处：
**1. 简洁性：列表推导极大地简化了代码，使得创建新列表的过程更加紧凑、易读。
    通过将循环、条件判断以及元素生成逻辑合并到一行表达式中，列表推导消除了传统for循环、if条件语句以及append操作的冗余代码，
    提升了代码的简洁性和可读性。
# 传统方式创建平方数列表
"""
squares = []
for num in range(10):
    squares.append(num ** 2)

# 列表推导创建平方数列表
squares = [num ** 2 for num in range(10)]
"""
**2. 高效性：列表推导在内部实现上通常比对应的for循环更为高效，因为它是由C语言编写的Python解释器直接处理的。
    此外，列表推导避免了在循环体内频繁调用list.append()方法，减少了函数调用开销，提升了性能。
**3. 表达力强：列表推导能够轻松处理复杂的列表生成逻辑，包括嵌套循环、多重条件筛选等。
    这使得开发者能够以直观、一致的方式表达复杂的列表生成操作。
"""
# 创建二维矩阵（列表的列表）
matrix = [[row * col for col in range(5)] for row in range(5)]

# 仅保留偶数元素
even_numbers = [num for num in range(20) if num % 2 == 0]

"""
**4. 可扩展性：列表推导不仅限于简单的一维列表生成，还可以与生成器表达式、条件表达式（三元运算符）、lambda函数等结合使用，进一步提升其功能和灵活性。
"""
# 使用生成器表达式生成斐波那契数列（节省内存）
# fibonacci = [x for x in (a + b for a, b in zip([0, 1], itertools.repeat(1, 998))[:1000])]

# 使用条件表达式根据条件生成不同的值
mixed_list = [x if x % 2 == 0 else 'odd' for x in range(10)]

# 使用lambda函数对列表元素进行复杂变换
words = []
transformed = [(lambda x: x.lower().strip())(word) for word in words]

""" 
**5. 泛化到其他类型：除了列表推导，Python还提供了集合推导（Set Comprehension）和字典推导（Dictionary Comprehension），
    它们具有类似的语法结构和优点，分别用于创建集合和字典。
"""
unique_chars = {char for char in 'abracadabra'}
fruit_counts = {fruit: count for fruit, count in [('apple', 3), ('banana', 2), ('orange', 5)]}


# 实例化对象
class Weight:
    def __init__(self, weight):
        self._weight = weight

    def __repr__(self):
        return f"weight:{self._weight}"


weight_instances = [Weight(i) for i in range(4)]
print(weight_instances)

# 类型转换
string_first_100 = [str(i) for i in range(100)]
single_string = ','.join([str(i) for i in range(100)])

print('----------------------使用列表推导而不是map（）和filter（）-----------------------')
"""简单情况推荐使用列表推导"""
nums = [1, 2, 3, 4, 66, 5, 6, 7, 8, 8, 765]


def is_odd_number(number: int) -> bool:
    return number % 2 == 1


odd_numbers = list(filter(is_odd_number, nums))
odd_numbers_doubled = list(map(lambda x: x * 2, nums))

# 使用列表推导式 pythonic
odd_numbers1 = [num for num in nums if num % 2 == 1]

print('----------------------使用负索引进行快速反向访问-----------------------')

print('----------------------确定可迭代性的all和any的使用-----------------------')
"""1. all()
功能：all() 函数接受一个可迭代对象作为参数，如果可迭代对象中所有元素都为真值（即非零、非空、非 None 等），则返回 True，否则返回 False。
"""
# 示例列表
numbers = [1, 2, 3, 4, 5]
bool_values = [True, True, False, True, True]
strings = ["hello", "", "world"]

# 使用 all() 函数进行判断
print(all(numbers))  # 输出: True （所有整数非零，视为真）
print(all(bool_values))  # 输出: False （存在 False，不满足所有元素为真）
print(all(strings))  # 输出: False （存在空字符串，视为假）

# 判断列表中所有元素是否大于0
positive_numbers = [1, 2, 3, 4, 5]
print(all(number > 0 for number in positive_numbers))  # 输出: True

# 判断字典中所有值是否为True
data = {'a': True, 'b': True, 'c': True}
print(all(value for value in data.values()))  # 输出: True

"""2. any()
功能：any() 函数同样接受一个可迭代对象作为参数。如果可迭代对象中存在至少一个元素为真值，any() 函数返回 True；如果所有元素均为假值，则返回 False。
语法：
"""
# 示例列表
numbers = [0, 8, 4, 0]
bool_values = [False, True, False, False, False]
strings = ["", "non-empty", "", None, "another non-empty"]

# 使用 any() 函数进行判断
print(any(numbers))  # 输出: True （存在非零元素，视为真）
print(any(bool_values))  # 输出: True （存在 True，满足至少有一个为真）
print(any(strings))  # 输出: True （存在非空字符串和非 None 元素，视为真）

# 判断列表中是否存在偶数
numbers_list = [1, 3, 5]
print(any(number % 2 == 0 for number in numbers_list))  # 输出: True

# 判断字典中是否存在值为False的项
data = {'a': True, 'b': False, 'c': True}
print(any(value is False for value in data.values()))  # 输出: True

"""注：not all(Iterable) 相当于 any(Iterable)"""

print('----------------------使用*运算符操作剩余序列-----------------------')
"""
相当于将一个变量变成一个容器，以列表的方式存储在变量中
"""
mylist = ['a', 'b', 'c', 'd', 'e']

(e1, w2, *w3) = mylist
print(w3, type(w3))  # ['c', 'd', 'e'] <class 'list'>

print('----------------------使用array.array获取基本类型数组-----------------------')
"""
array ： 数据元素只能是单一类型
list：元素可以是不同类型
"""
import array

marr = array.array('f', (123, 1231, 12312, 356, 323, 41, 43, 8, 45, 64, 5342, 3, 8, 732, 62.34))

"""array 模块是 Python 的标准库之一，它提供了高效的数组操作功能。与列表（list）相比，array 类型的数据结构专注于存储相同类型的数据，
    从而在内存使用和访问效率上具有更高的性能。
下面对 array 模块进行详细解析：

    
array 对象支持类似列表的操作方式：
索引访问：arr[i]
切片访问：arr[start:end]
遍历：for elem in arr: ...
修改元素：arr[i] = value
扩展或缩短数组：通过切片赋值或使用 extend() 方法


创建 array 对象： 创建一个 array 对象时，需要指定数据类型和初始元素（可选）。
    数据类型由字符代码表示，如 'i' 表示整数、'f' 表示浮点数、'u' 表示无符号整数等
    
array 模块支持以下数据类型：
'b': 有符号字节（signed char）
'B': 无符号字节（unsigned char）
'u': Unicode字符（Py_UNICODE）
'h': 有符号短整型（signed short）
'H': 无符号短整型（unsigned short）
'i': 有符号整型（signed int）
'I': 无符号整型（unsigned int）
'l': 有符号长整型（signed long）
'L': 无符号长整型（unsigned long）
'q': 有符号长整型（signed long long）
'Q': 无符号长整型（unsigned long long）
'f': 浮点型（float）
'd': 双精度浮点型（double）
"""
# 创建一个只包含整数的空数组
int_array = array.array('i')

# 创建一个包含浮点数的数组
float_array = array.array('f', [1.5, 2.3, 3.7])

# 创建一个包含无符号字符的数组
char_array = array.array('B', b'hello')
"""append(): 向数组末尾添加一个元素。"""
int_array.append(10)
"""extend(): 将另一个数组或可迭代对象的元素添加到数组末尾"""
int_array.extend([11, 12, 13])
"""insert(): 在指定位置插入一个元素。"""
int_array.insert(0, 5)
"""pop(): 删除并返回数组末尾的元素，或者指定索引处的元素。"""
# last_element = int_array.pop()
# element_at_index_0 = int_array.pop(0)

"""remove(): 从数组中移除第一个匹配给定值的元素。"""
int_array.remove(5)

"""append(x): 将元素 x 添加到数组末尾。
extend(iterable): 将 iterable 中的元素逐一添加到数组末尾。
count(x): 返回数组中元素 x 的出现次数。
index(x[, start[, stop]]): 返回数组中第一个匹配元素 x 的索引，可指定搜索范围。
insert(i, x): 在索引 i 位置插入元素 x。
remove(x): 删除数组中第一个匹配元素 x。
reverse(): 反转数组中的元素顺序。
tobytes(): 返回一个表示数组内容的字节串。
tofile(f): 将数组内容以二进制形式写入到打开的文件对象 f 中。
frombytes(bytes_object): 根据给定的字节串创建一个新的数组。
fromfile(f[, n]): 从打开的文件对象 f 中读取 n 个元素（默认读取全部）并创建一个新的数组。
"""

print('----------------------带str的不可变unicode字符数组-----------------------')

print('----------------------带有bytearray的单字节可变序列-----------------------')

print('----------------------使用字节作为不可变的单字节序列-----------------------')
