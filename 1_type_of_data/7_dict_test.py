"""
利用**解包字典
"""

x = {"a": 1, "b": 2}
y = {"c": 3, "d": 4}
z1 = {**x, **y, 'e': 5, 'f': 9}
z2 = {**y, **x, 'e': 5, 'f': 9}

print(z1)
print(z2)

"""
is 和 == 都用于比较两个对象，但它们的作用和含义不同：
is：
这是身份运算符，用于判断两个引用是否指向内存中的同一个对象。
如果两个变量引用的是内存中的同一块区域（即它们实际上是同一个对象），则返回 True，否则返回 False

==：
这是比较运算符，用于判断两个对象的值是否相等。
对于基本数据类型，它比较的是它们的实际值。对于复合类型（如列表、字典等），它会递归地比较每个元素或键值对是否相等。

dict的三种视图，都会认为自己与自己是不同的对象；除值视图外，项目视图和键视图会认为自身与自身的值是相同的。
"""
print(x.items() is x.items(), x.keys() is x.keys(), x.values() is x.values())
print(x.items() == x.items(), x.keys() == x.keys(), x.values() == x.values())

d = {'a': 111, 'b': 222, 'c': '333'}
d_dictview = d.items()  # 返回一个视图对象， 每个健值对以元组的形式，作为列表的元素存在
print(d_dictview)
print(d.keys())  # 返回一个视图对象， 每个键作为列表的元素存在。
print(d.values())  # 返回一个视图对象， 每个值作为列表的元素存在。
print(len(d_dictview), len(d.keys()), len(d.values()))  # 3 3 3
print('----------------')
print(iter(d_dictview))  # 迭代器 <dict_itemiterator object at 0x102abfd80>
print([*iter(d_dictview)])  # # 使用列表推导式将迭代器iter_d_dictview转换为列表,d_dictview_list = [*iter_d_dictview]
print(('a', 111) in d_dictview)

reversed(d_dictview)  # 不是原地操作，反转一个迭代对象
print(d_dictview)
print([*iter(reversed(d_dictview))])

print('----------------')
d['d'] = '444'  # 给字典d添加键值对
print(d.items())

d.setdefault('f', 999)  # 如果键不存在，就添加一个键值对,默认值设为999，不指定为None，否则不添加
print(d)

d1 = {'aa': 123, 'bb': 456}
d1.update(d)  # 将字典d中的键值对添加到字典d1中，如果键相同，则覆盖
print(d1)
print(d1.get('na', 100))  # 如果键不存在，返回默认值100，否则返回键对应的值 ,不设置默认值，则返回None
d2 = d1.copy()  # 返回字典d1的--浅拷贝
d2['aa'] = 12999
print(d1, '\n', d2)

print('--------------------')
c1 = {'y': 'aada', 'm': 123, 'n': {'a': 111, 'b': 222, 'c': '333'}}
c2 = c1.copy()
c2['m'] = 9090909
print(c1, '\n', c2)
c2['n']['b'] = 999
print(c1, '\n', c2)

"""有序字典OrderedDict
显示的、有明确类型意义的、有顺序的字典"""
from collections import OrderedDict

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = OrderedDict(d1)
print(d2)
print('-----------------------------------')
e = OrderedDict()
e['a'] = 1
e['b'] = 2
e['c'] = 3
e1 = OrderedDict(a=1, b=2, c=3)
e2 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
e3 = OrderedDict((('a', 1), ('b', 2), ('c', 3)))
e4 = OrderedDict({('a', 1), ('b', 2), ('c', 3)})
e5 = OrderedDict({'a': 1, 'b': 2, 'c': 3})

"""dict.fromkeys(iterable, value=None)
iterable: 这是一个可迭代对象（如列表、元组或字符串等），其元素将作为新字典中的键。
value (可选): 所有键对应的新值，默认为 None。如果提供了这个参数，那么新字典中所有键对应的值都会是这个指定的值
"""
f = OrderedDict()
f.fromkeys(['a', 'b', 'c'], )  # 以iterable构建字典的健，如果value为空，就用None填充
f.fromkeys(['a', 'b', 'c'], 1)  # 以iterable构建字典的健，value设为默认值1
f.fromkeys(['a', 'b', 'c'], [1, 2, 3])  # 以iterable构建字典的健，value设为默认值【1，2，3】

"""映射链Chainmap
可将多个字典或者其他映射类型的对象链接起来，形成（一个）逻辑上的字典/逻辑上的单一映射。

ChainMap 是 collections 模块提供的一个类，它可以将多个映射（如字典）串联在一起形成一个虚拟的映射集合(逻辑上的字典)。
当你通过 ChainMap 访问一个键时，它会按照映射列表中的-顺序-依次查找该键是否存在及其对应的值。
如果键在一个较早添加到链中的映射里出现，则后续映射中的同名键将不会被访问。
"""

from collections import ChainMap

# 定义两个字典
dict1 = {'x': 1, 'y': 2}
dict2 = {'y': 3, 'z': 4}

# 创建一个映射链，将这两个字典串联起来
chain_dict = ChainMap(dict1, dict2)
print(type(chain_dict))  # 输出：<class 'collections.ChainMap'>
print(chain_dict)  # 输出：ChainMap({'x': 1, 'y': 2}, {'y': 3, 'z': 4})

# 现在可以通过 chain_dict 来访问合并后的键值对
print(chain_dict['x'])  # 输出：1 （从 dict1 中获取）
print(chain_dict['y'])  # 输出：2 （虽然 dict2 中也有 'y'，但优先返回 dict1 中的 'y' 值）
print(chain_dict['z'])  # 输出：4 （因为 'z' 只在 dict2 中存在）

print(chain_dict.maps)  # 输出：[{'x': 1, 'y': 2}, {'y': 3, 'z': 4}] :内部维护的映射(字典)顺序，存放在list中

# 更新操作会作用于第一个映射（即最优先的映射） 即：多个字典中都存在的健，dict1（顺序第一） 中的键被更新
chain_dict['y'] = 5
print(chain_dict.maps[0]['y'])  # 输出：5，原 dict1 中的 'y' 已经更新为 5
print(chain_dict.maps[0], chain_dict.maps[1])

"""在collections.ChainMap中，new_child()方法用于创建一个新的子映射，并将其添加到ChainMap的最前面。
这意味着当查找键时，新的子映射将拥有最高的优先级"""

# 假设我们有以下两个字典和一个ChainMap对象
dict1 = {'x': 1, 'y': 2}
dict2 = {'y': 3, 'z': 4}
chain_dict = ChainMap(dict1, dict2)

"""# 创建并附加一个新的子映射
输出: ChainMap({'y': 5, 'w': 6}, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})
在chain_dict这个映射关系内创建一个子映射，子映射的优先级高于原映射（位于原有内部维护的映射顺序之前的位置）"""
new_child_dict = {'y': 5, 'w': 6}
updated_chain_dict = chain_dict.new_child(new_child_dict)
print(updated_chain_dict)  # 输出: ChainMap({'y': 5, 'w': 6}, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})

# 现在访问 'y' 时，它会从 new_child_dict 中获取值
print(updated_chain_dict['y'])  # 输出: 5

new_child = chain_dict.new_child()  # 在chain_dict这个映射关系内创建一个子映射，子映射的优先级高于原映射（位于原有内部维护的映射顺序之前的位置）
print(new_child)
new_child['new_key'] = 'new_value'  # 新建键值对
new_child['new_key2'] = 'new_value2'  # 新建键值对
print(new_child)  # 输出新映射内容，包含原有映射以及新增的键值对

print('----------------------')
"""通过 .maps 属性可以查看和修改 ChainMap 内部维护的映射列表顺序，这对于处理层级环境变量、配置文件继承等场景非常有用。
"""

from collections import defaultdict

"""，collections.defaultdict 是一个内建 dict 类的子类，它提供了一种更加便捷的方式来处理字典中键不存在的情况。
当尝试访问一个默认字典中尚未存在的键时，它不会抛出 KeyError 异常，而是自动调用一个预定义的工厂函数来生成并返回一个新的值作为该键的默认值。
"""
default_dict_int = defaultdict(int)  # 默认值为int类型,未显示设置时，默认值为0
print(default_dict_int['123'])

default_dict_str = defaultdict(str)
print(default_dict_str['123'])  # 默认值为str类型,未显示设置时，默认值为空字符串''
default_dict_str['123'] = '123'
print(default_dict_str)  # 输出：defaultdict(<class 'str'>, {'123': '123'})
"""第一个参数是工厂函数"""
default_dict_1 = defaultdict(lambda: '000', a=1, b=2)  # 默认值为lambda函数，未显示设置时，默认值为'000'
default_dict_2 = defaultdict(lambda: '000', {'a': 1, 'b': 2})
default_dict_3 = defaultdict(list, {'a': 1, 'b': 2})  # 默认值为list类型,未显示设置时，默认值为[]
default_dict_4 = defaultdict(int, {'a': 1, 'b': 2})  # 默认值为int类型,未显示设置时，默认值为0
print(default_dict_1, '\n', default_dict_2, '\n', default_dict_3, '\n', default_dict_4)

print(default_dict_1.default_factory)
print(default_dict_str.default_factory)
print(default_dict_3.default_factory)
print(default_dict_4.default_factory)
for str1, value in default_dict_2.items():
    print(f'{str1}:{value}')

print('00000000000000000000000')
"""Counter:计数器
用于计算元素出现的次数，类似于一个字典，但键是元素本身，值是元素出现的次数。"""
from collections import Counter

from collections import Counter

# 示例数据
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

# 创建并使用计数器
counter = Counter(data)
print(counter)
# 输出每个元素及其出现次数
for item, count in counter.items():
    print(f"{item}: {count}")

# 或者单独查询某个元素出现的次数
print(f"Apple count: {counter['apple']}")

counter1 = Counter()
counter1.update(data)
counter2 = Counter('sdaisdhiashudiqwjbvaduodygdsbjshdgfaugd')
print(counter2)
counter3 = Counter({'a': 4, 'b': 2})
counter4 = Counter(a=1, b=2)

print(type(counter2.items()), counter2.items())

for item1, count1 in counter2.items():
    print(f'item: {item1}, count1: {count1}')
