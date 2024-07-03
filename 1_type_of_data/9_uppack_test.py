"""
拆开一个序列：*iterable
拆开一个字典：**dictionary

"""
a = '1231312'
b = [1, 2, 31, 23, 1231, 3, 12, 1, 31, 23, 1, 2]
c = (1, 2, 3, 12, 3, 'asod', 'oiuer')
d = {1, '890', 54, 'ada', 'fogi'}
e = {'a': 1, 'b': 2, 'c': 3}
f = range(10, 30)

print([*a], '\n', {*a})
"""Python语法并不支持直接将可迭代对象解包到创建元组的圆括号内，而是需要通过显式转换或列表推导式等间接方法来实现。"""
# print((*a))  # SyntaxError: cannot use starred expression here
print(tuple([*a]))
print([*b])
print(tuple([*b]))
print(*b)
print('---------------')
"""
 def_name（*a）：解包a到函数调用的圆括号内，是将a解包，可迭代对象的元素作为传递给函数的参数，语法上是合法的
 （*a）：语法上不支持直接将可迭代对象解包到创建元组的圆括号内，(*a,) or 可以通过显式转换或列表推导式等间接方法来实现 
"""
print([*a], '\n', [*b], '\n', [*c], '\n', [*d], '\n', [*f])
print((*a,), '\n', (*b,), '\n', (*c,), '\n', (*d,), '\n', (*f,))
print({*a}, '\n', {*b}, '\n', {*c}, '\n', {*d}, '\n', {*f}, '\n', {**e})
print('---------------')

x = ('a', 'b', 'c')
y = (1, 2, 3)
print(*x, *y)  # 将x和y的每个元素分别作为参数传递给函数
print((*x, *y))  # 将x和y的元素展开，再形成一个新的元组
print((*x,))  # 将x的元素展开，和一个空元组合并
d = (1, 23, 1, 23, 1, 3,)
print(d)

"""
*args:常用来声明元组变量（位置变量） 注：解包到函数调用的圆括号内，是将可迭代对象拆开，其元素作为传递给函数的参数。
    所以语法将不支持(*iterable)：将容器直接解包到创建元组的圆括号内，但可以合并到一个元组中（和一个空元组合并）。
    
**kwargs:常用来声明字典变量（关键字变量）
"""
args = [1, 2, 3, 4]


def f(a, b, c, d):
    print(a, c, b, d)


"""解包到函数的形参位置，是作为位置参数"""
f(*args)  # 输出: 1 3 2 4


def f1(a, b, c, *d):
    print(a, c, b, d)


args1 = [1, 2, 3, 4, 234, 67, 563, 52, 32, 42, 4]
f1(*args1)

print('------------------------')
""" 在字典中，**解包，后面的字典的键值始终覆盖前面字典的相同键的值"""
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# 合并字典
combined_dict = {**dict1, **dict2}
print(combined_dict)  # 输出: {'a': 1, 'b': 3, 'c': 4}

"""合并序列"""
cc = [*x, *args]
print(cc)
"""将变量变成一个容器"""
a, *b, c = range(1, 10)
print(a, *b, c)
print(type(b))  # 输出: <class 'list'>
c, *_, d = range(20, 30)  # 变量_是一个特殊的变量，用_来接收不使用的变量
print(c, d, sep=' ')

print('------------------------')

numbers = [1, 2.5, 'three']
*individual_numbers, = numbers
print(type(individual_numbers), individual_numbers)  # <class 'list'>  [1, 2.5, 'three']
