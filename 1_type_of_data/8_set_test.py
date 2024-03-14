"""集合
是存放无顺序无索引内容的容器
可以用集合消除重复的元素，可以进行交、差、并、或（补）等数学集合运算
可以认为集合是仅有键的字典，所有元素不重复，是可哈希的。其中不能有列表、集合、字典等可变内容存在。
虽然无法更改集合中的元素，但可以向集合中添加元素，也可以从集合中删除元素。
一个空的{}是字典，不是空集合，空集合只能用set()不传值来创建
"""
a = {}  # {}是字典，不是空集合，空集合只能用set()不传值来创建
b = {'asdf', 'asdf', 'asdf', 'soihs'}  # 去重
c = set()  # 空集合
d = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 集合
e = {1, True, 2, 0, False}  # 集合
print(a, b, c, d, e, end='\n')
print(type(a), type(b), type(c), type(d), type(e))
# cc = {1, 2, 3, 4, {12, 34}} #unhashable type: 'set'
# print(cc)
# print({[1, 2, 3], 98})  # unhashable type: 'list'
"""set()
可选择带有可迭代对象获取的元素
"""
a = set()
b = set("asodasiduo")
c = set(('a', 's', 'd', 'q', 'e', 1, 2))
d = set(b'osahoeoqh')
e = set({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
f = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
g = set(range(9, 123, 6))
print(a, b, c, d, e, f, g, end='\n')
f.add('897')
print(f)

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8, 9}
print(a & b, a | b, a - b, a ^ b)  # 交、并、差、对称差,原地操作版本是&=、|=、-=、^=
print(a <= b, a < b, a >= b, a > b)

"""冻结集合：frozenset
内置函数frozenset([iterable])，可构建不可变集合,返回一个frozenset对象，frozenset对象是不可变的，可以被其他集合操作。
也是无序的。
"""

a = frozenset([1, 2, 3, 3, 1, 21, 3121, 21, 2])
b = frozenset('asdqhonasg')
c = frozenset(range(1, 20))
d = frozenset()
print(type(a), type(b), type(c), type(d))

fs = frozenset([1, 2, 3])
print(fs)
print(fs.intersection([2, 3, 5]))
print(fs.symmetric_difference([2, 3, 5]))
print(fs.union([19, 11, 423]))
print(fs.issubset([1, 2, 3, 4, 5, 99, 6, 7, 8, 9, 10]))

# for v in a:
#     print(v)
