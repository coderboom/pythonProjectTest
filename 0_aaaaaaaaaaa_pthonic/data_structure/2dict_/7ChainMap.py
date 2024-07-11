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

# 添加元素
print('---------------------在chainmap中添加/删除元素------------------------')
"""
在chainmap中添加元素，是在---第 1 个---dict---中添加
"""
chain_dict['gold'] = 'asdasdadadasd'
print(chain_dict)

print('---------------------在chainmap中查询/修改元素------------------------')
"""
    若修改除第一个dict以外dict的元素，直接使用 hain_dict[var]=‘adasd’ 会导致第一个dict中添加 var=adasd，

    若查询元素，会优先从第一个dict中查询，若有则返回，若第一个dict中没有，继续第二个dict中查询。
"""

"""在collections.ChainMap中，new_child()方法用于创建一个新的子映射，并将其添加到ChainMap的最前面。
这意味着当查找键时，新的子映射将拥有最高的优先级"""

# 假设我们有以下两个字典和一个ChainMap对象
dict1 = {'x': 1, 'y': 2}
dict2 = {'y': 3, 'z': 4}
chain_dict = ChainMap(dict1, dict2)

""" 创建并附加一个新的子映射
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

print('--------------------------------------------------------------')
"""通过 .maps 属性可以查看和修改 ChainMap 内部维护的映射列表顺序，这对于处理层级环境变量、配置文件继承等场景非常有用。
"""
print(new_child.maps)
print('--------------------------------------------------------------')

print('--------------------------------------------------------------')
dict1 = {'x': 1, 'y': 2}
one_child_dict = ChainMap(dict1)
one_child_dict['x'] = 123
print(one_child_dict.maps)
