"""只读字典
"""
"""
在高并发中 常使用
代理不会影响并发性能，
适用于： 读写分离
"""
from collections import ChainMap

print('--------------------types.MappingProxyType------------------------')

"""
使用 types.MappingProxyType 类
从Python 3.3开始，types 模块引入了 MappingProxyType 类，它专门为创建只读字典视图而设计。
    MappingProxyType 对一个底层字典进行封装，使得用户无法直接修改这个封装后的字典对象。
"""
import types

# 原始字典
underlying_dict = {'key1': 'value1', 'key2': 'value2'}

# 使用 MappingProxyType 创建只读字典，相当于一个代理
readonly_dict = types.MappingProxyType(underlying_dict)

# 尝试修改会引发 TypeError
try:
    readonly_dict['key1'] = 'new_value'
except TypeError as e:
    print(e)  # 'mappingproxy' object does not support item assignment

""" 修改原始数据，代理会变：代理会随着原始数据的修改而变化。"""

underlying_dict['key1'] = 123123123123
print(readonly_dict)
"""
修改原始字典时代理会变：这是因为MappingProxyType提供的是一种动态的只读视图。
    虽然它本身不可被直接修改，但它始终指向并反映了底层原始字典的实际状态。当您修改了underlying_dict，即更改了基础数据结构的内容，
    readonly_dict作为对这个底层字典的映射视图，会即时反映出这些改动。因此，尽管不能通过readonly_dict直接更改键值对，但可以看到其内容随着底层字典的变化而更新。
"""
print('-----------------')
"""删除原始数据，代理中的数据依然存在：表明删除原始字典不影响代理字典"""
del underlying_dict
print(readonly_dict)  # {'key1': 123123123123, 'key2': 'value2'}

"""
这与Python的垃圾回收机制和MappingProxyType对象的工作方式有关。
    在Python中，当您删除一个变量（如del underlying_dict）时，----实际上是解除了该变量名与所引用对象之间的绑定-----
    如果该对象没有其他引用，则会在适当的时机被垃圾回收机制清理。
    然而，在本例中，尽管删除了underlying_dict，但readonly_dict（即MappingProxyType对象）仍然保持着对原始字典对象的内部引用。
    因此，即使underlying_dict被删除，原始字典对象由于仍有readonly_dict的引用而未被回收，readonly_dict仍能访问到原始字典的数据。

具体分析：
    当您创建readonly_dict时，MappingProxyType内部记录了对underlying_dict的实际引用（即内存地址），而非仅记录underlying_dict变量名。
    删除underlying_dict只是断开了变量名与原始字典对象的关联，但并未影响readonly_dict对原始字典的内部引用。
    因此，即使underlying_dict被删除，只要原始字典对象未被垃圾回收，readonly_dict仍可以通过其内部保存的引用访问到原始字典的数据。
结论：
在本例中，第5点描述的现象是由于MappingProxyType对象保持了对原始字典的内部引用，即使删除了underlying_dict变量，只要原始字典对象未被垃圾回收，readonly_dict仍能访问其数据。
    这展示了Python中对象引用、垃圾回收机制以及MappingProxyType工作方式的一些特性。
    
    然而，这种依赖于内部引用的行为在实际编程中应谨慎对待，因为一旦原始字典被垃圾回收，readonly_dict将会失效，且可能引发难以预料的错误。
    通常情况下，建议----避免直接删除------原始字典-----，以确保MappingProxyType对象的稳定性和可预测性。
"""
