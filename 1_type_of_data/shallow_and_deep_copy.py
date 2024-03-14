"""
在Python中，浅拷贝（shallow copy）和深拷贝（deep copy）是两种不同的复制对象的方式，它们之间的主要区别在于如何处理对象内部包含的可变子对象。
浅拷贝（Shallow Copy）：
浅拷贝通过创建一个新的引用指向原始对象的内存地址来实现。这意味着新旧对象共享同一块内存中的数据。
当对象是一个不可变类型（如整数、字符串、元组等）时，浅拷贝和深拷贝没有区别，因为不可变对象的值不能改变。
当对象是一个可变类型（如列表、字典或其他自定义类实例）时，浅拷贝只会复制对象的第一层内容，
————————注（改变第一层不可变元素的话，会申请一个新的内存块来保存改变了的值，从而不会影响原始对象）
  即它会为容器对象（如列表或字典）创建新的引用，但容器内的元素仍然是原来的引用，
  也就是说，如果容器内包含其他可变对象，那么这些可变对象还是会被原始对象和浅拷贝的对象共享。

"""
import copy

# 示例：浅拷贝列表
original_list = [1, 2, [3, 4]]
shallow_copy = copy.copy(original_list)
print(original_list, "id=", id(original_list))
print(shallow_copy, "id=", id(shallow_copy))
print(id(original_list[0]), id(original_list[1]), id(original_list[2]))
print(id(shallow_copy[0]), id(shallow_copy[1]), id(shallow_copy[2]))
print('------------------------')
# 改变浅拷贝列表中嵌套列表的内容会影响原列表
shallow_copy[0] = 'asda'
shallow_copy[2][0] = 'Changed'
print(original_list)  # 输出：[1, 2, ['Changed', 4]]
print(shallow_copy)  # 输出：['asda', 2, ['Changed', 4]]
print(id(original_list[0]), id(original_list[1]), id(original_list[2]))
print(id(shallow_copy[0]), id(shallow_copy[1]), id(shallow_copy[2]))

print('------------------------')

# 示例：浅拷贝字典
original_dict = {'a': 1, 'b': [2, 3]}
shallow_dict_copy = copy.copy(original_dict)

# 改变浅拷贝字典中嵌套列表的内容也会影响原字典
shallow_dict_copy['b'][0] = 'Changed'
print(original_dict)  # 输出：{'a': 1, 'b': ['Changed', 3]}
print('000000000000000000000000000000000000000000000000000000000000000000000000')
"""深拷贝（Deep Copy）：
深拷贝则会递归地复制整个对象及其所有子对象，直到所有的可变元素都被复制到新的内存空间，形成一个与原对象完全独立的新对象。
对于任何类型的对象（包括可变对象），深拷贝都会创建一个全新的副本，修改深拷贝后的对象不会影响原始对象。
"""
import copy

# 示例：深拷贝列表
original_list1 = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original_list)
print(original_list1, "id=", id(original_list1))
print(deep_copy, "id=", id(deep_copy))
print(id(original_list1[0]), id(original_list1[1]), id(original_list1[2]))
print(id(deep_copy[0]), id(deep_copy[1]), id(deep_copy[2]))
print('------------------------')
# 改变深拷贝列表中嵌套列表的内容不会影响原列表
deep_copy[1] = 'adaqwe'
deep_copy[2][0] = 'Changed'
print(original_list1)  # 输出：[1, 2, [3, 4]]
print(deep_copy)  # 输出：[1, 'adaqwe', ['Changed', 4]]
print(id(original_list1[0]), id(original_list1[1]), id(original_list1[2]))
print(id(deep_copy[0]), id(deep_copy[1]), id(deep_copy[2]))
# 示例：深拷贝字典
original_dict = {'a': 1, 'b': [2, 3]}
deep_dict_copy = copy.deepcopy(original_dict)

# 改变深拷贝字典中嵌套列表的内容不会影响原字典
deep_dict_copy['b'][0] = 'Changed'
print(original_dict)  # 输出：{'a': 1, 'b': [2, 3]}

"""总结来说，在实际编程中，选择使用浅拷贝还是深拷贝取决于你是否需要保持原对象与复制对象间的独立性。
如果你不希望改变复制对象会影响到原始对象的内部状态，尤其是当对象结构较为复杂时，应该使用深拷贝。"""
