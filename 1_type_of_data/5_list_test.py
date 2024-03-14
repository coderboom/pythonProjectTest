"""
三种基本序列类型——有顺序的数据列
list、tuple、rang()对象、
二进制数据（bytes） 和 文本字符串（str）也是序列类型，它们是特殊序列类型，会有一些特殊的性质和操作

Python 的内置序列类型有：
类型	     创建方法	      可变性  	特别方法
列表  	 list()	           可变	    sort()
元组	     tuple()	      不可变
等差数列   range()	      不可变	     属性方法
字符串	 str()	          不可变	    字符的方法
字节串	 bytes()	      不可变
字节数组	 bytearray()	   可变
内存视图	 memoryview()	  不可变
注：集合、字典不是序列类型，虽然字典在最新的 Python 版本中具备了元素顺序特性，但这不是一种「保证」
"""
from collections import abc

a = [1, 2, 3]
b = {1, 2, 3}
c = (1, 2, 3)

isinstance(a, abc.Sequence)
# True
isinstance(b, abc.Sequence)
# False

# 可变类型
isinstance(a, abc.MutableSequence)
# True
isinstance(c, abc.MutableSequence)
# False

"""
序列的特点是由若干元素组成，元素的分布有顺序，因此根据这个特点，它们支持一些共性的操作
运算	                                  结果：	                                               备注
x in s	                 如果 s 中的某项等于 x 则结果为 True，否则为 False	
x not in s	             如果 s 中的某项等于 x 则结果为 False，否则为 True	
s + t	                           s 与 t 相拼接	
s * n 或 n * s	                 相当于 s 与自身进行 n 次拼接	
s[i]	                       s 的第 i 项，起始为 0	                                     切片操作
s[i:j]	                        s 从 i 到 j 的切片	
s[i:j:k]	                  s 从 i 到 j 步长为 k 的切片	
len(s)                          	s 的长度	
min(s)	                           s 的最小项	
max(s)	                            s 的最大项	
s.index(x[, i[, j]])	    x 在 s 中首次出现项的索引号（索引号在 i 或其后且在 j 之前）          count 方法
s.count(x)	                   x 在 s 中出现的总次数	                                    index 方法
for i in x:pass	                         迭代	
hash(x)	                              对象的哈希值	                                     仅不可变序列
sorted(x)	                           排序	
all(x) 或者 any(x)	               全真或者有真检测	
iter(x)	                                生成迭代器

注：以上部分操作需要额外的特殊方法实现。当我们在处理数据量大且需频繁查找元素（如 in 操作）时，最好使用 set、dict ，这样将会大幅度提升处理速度


以下是仅可变序列支持的操作：
运算	                                  结果：	                                           
s[i] = x	                   将 s 的第 i 项替换为 x	
s[i:j] = t	                   将 s 从 i 到 j 的切片替换为可迭代对象 t 的内容	
del s[i:j]	                   等同于 s[i:j] = []	
s[i:j:k] = t	               将 s[i:j:k] 的元素替换为 t 的元素	
del s[i:j:k]	               从列表中移除 s[i:j:k] 的元素	
s.append(x)	                   将 x 添加到序列的末尾 (等同于 s[len(s):len(s)] = [x])	
s.clear()	                   从 s 中移除所有项 (等同于 del s[:])	
s.copy()	                   创建 s 的浅拷贝 (等同于 s[:])	
s.extend(t) 或 s += t	       用 t 的内容扩展 s (基本上等同于 s[len(s):len(s)] = t)	

s *= n	                      使用 s 的内容重复 n 次来对其进行更新	
s.insert(i, x)	              在由 i 给出的索引位置将 x 插入 s (等同于 s[i:i] = [x])	
s.pop() 或 s.pop(i)	          提取在 i 位置上的项，并将其从 s 中移除	
s.remove(x)	                  删除 s 中第一个 s[i] 等于 x 的项目。	
s.reverse()	                  就地将列表中的元素逆序。


序列的本质
序列是一种可迭代（iterable）的对象，它支持通过 __getitem__() 特殊方法来使用整数索引进行高效的元素访问，并定义了一个返回序列长度的 __len__() 方法。
内置的序列类型有 list、str、tuple 和 bytes。
注意虽然 dict 也支持 __getitem__() 和 __len__()，但它被认为属于映射而非序列，因为它查找时使用任意的不可变的（immutable）键而非整数。

collections.abc.Sequence 抽象基类定义了一个更丰富的接口，它在 __getitem__() 和 __len__() 之外又添加了 count()、index()、__contains__() 和 __reversed__() 。  
实现此扩展接口的类型可以使用 register() 来显式地注册。

"""

list_num = ['sdad', 'asdiueb', 'vriebbsd', 'Hasdoiuqwn', 'vidhqwey', 'siuhdwbei']

list_num.insert(2, str(124121))
print(list_num)

list_num.remove('124121')
print(list_num)

list_num.sort()
print(list_num)

list_num.sort(key=str.lower)
print(list_num)

# list_num.append(123123123)
list_num.sort(reverse=True)  # 无法对数字和字符串同时进行排序，同时只能对一种数据类型排序
print(list_num)

from collections import abc

"""
sort() 是内置函数，是直接对原有列表进行原地排序，而不是创建一个新的排序后的列表

sort() 函数适用于列表对象。
它不返回任何值，而是直接修改调用它的列表。
可以通过 key 参数自定义排序依据。
可以通过 reverse=True 进行降序排序，默认是升序排序

--key参数是一个可选参数，它接受一个函数作为值--
这个函数会被应用到列表中的每个元素上，并且排序是基于该函数对每个元素返回的结果进行的。

因此，key参数的具体使用非常灵活，可以根据实际需求选择不同的函数来定制排序规则。
以下是一些常用的key参数使用的例子：

数字排序：
升序排序（默认）：无需指定key参数。
降序排序：reverse=True，无需key参数，但如果需要基于某个特定字段降序，则可以配合key使用。

字符串排序：
默认按字典顺序排序单词：无需指定key参数。
按照字符串长度排序：key=len。

元组或列表排序：
根据第二个元素排序：key=lambda x: x[1]。
根据第二个元素降序排序：key=lambda x:-x[1] or key=lambda x:x[1]，reverse=True
对于多级排序（先按第一个元素升序，然后按第二个元素降序）：可以使用匿名函数或者定义外部函数处理。
自定义对象排序：
如果列表包含自定义类的对象，可以根据对象的属性进行排序，例如假设有一个Person类，有age和name属性，按照年龄升序排序：key=lambda person: person.age。

转换类型后排序：
将所有元素转换为小写后排序字符串：key=str.lower。
将元素转换为整数后排序（比如原本是浮点数但要忽略小数部分）：key=int。

复杂数据结构排序：
排序嵌套列表或字典时，可能需要更复杂的key函数来提取用于排序的关键值。
总的来说，key参数接受任何能够接收单个元素并返回用于比较的单一值的函数，这意味着你可以根据实际情况创建任意复杂的逻辑来进行排序。
"""

print(['a', 'b'] + ['c', 'd'])
print(['a', 'b'] * 3)
a = [1, 2, 3]
len(a)  # 3 元素个数
max(a)  # 3 最大值
min(a)  # 1 最小值
sum(a)  # 6 求和
a.index(2)  # 1 指定元素位置
a.count(1)  # 1 求元素的个数
for i in a:
    print(i)  # 迭代元素
sorted(a)  # 返回一个排序的列表，但不改变原列表
any(a)  # True 是否至少有一个元素为真
b = [1, 2, 3, 0]
print(all(b))  # True 是否所有元素为真

a = [1, 2, 3]
a.append(4)  # a: [1, 2, 3, 4] 增加一个元素
a.pop()  # 每执行一次删除最后一个元素
a.extend([9, 8])  # a: [1, 2, 3, 9, 8] # 和其他列表合并
a.insert(1, 'a')  # a: [1, 'a', 2, 3] 指定索引位插入元素
a.remove('a')  # 删除第一个指定元素
a.clear()  # [] 清空

a.reverse()  # 反转顺序
a.sort()  # 排序
a.sort(reverse=True)  # 反序
a.sort(key=abs)  # 传入函数关键字作为排序规则

# 将一个可迭代的对象展开形成一个列表
b = [i for i in range(5)]
# [0, 1, 2, 3, 4]

# 可以将结果进行处理
['第' + str(i) for i in range(5)]
# ['第0', '第1', '第2', '第3', '第4']

# 可以进行条件筛选, 实现取偶数
c = [i for i in range(5) if i % 2 == 0]

# 拆开字符, 过滤空格，全变成大写
[i.upper() for i in 'Hello world' if i != ' ']
# ['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']
# 对于复杂逻辑可以分行编写
[i.upper()
 for i in 'Hello world'
 if i != ' '
 ]

# 条件分支
data = ['good', 'bad', 'bad', 'good', 'bad']
d = [1 if x == 'good' else 0 for x in data]
# [1, 0, 0, 1, 0]

"""extend(x),会对可迭代对象x，进行一层解包，然后将解包后的元素添加到data中。"""
data.extend(['123', '321'])
print(data)
data.extend([['98', '456', '789', '987', ]])
print(data)

print(data.reverse())
print(data)
print('----------------------')
"""sorted() 函数：
sorted() 是一个内置函数，它接收一个可迭代对象（如列表、元组或字符串等），并返回一个新的已排序的列表。
它不会改变原对象本身，而是创建一个新的排序后列表。
可以自定义排序规则，通过 key 参数指定排序依据，以及通过 reverse 参数决定是否降序排列。
"""
original_list = [5, 2, 9, 1, 5]
sorted_list = sorted(original_list)
print(type(sorted_list))
print(sorted_list)  # 输出：[1, 2, 5, 5, 9]
print(sorted(original_list, reverse=True))  # 输出：[9, 5, 5, 2, 1]

"""list.sort() 方法：
sort() 是列表对象的方法，只能用于对列表进行原地排序。
调用 sort() 方法会直接修改原始列表，而不是创建新的列表。
同样支持 key 和 reverse 参数来定制排序规则。
"""
list_to_sort = [5, 2, 9, 1, 5]
list_to_sort.sort()
print(list_to_sort)  # 输出：[1, 2, 5, 5, 9]

"""reversed() 函数和 list.reverse() 方法：
reversed() 是一个内置函数，它可以返回给定序列的迭代器，并不直接生成新列表（不是一个原地操作）。常用于反向遍历序列，
或者配合其他构造函数（如 list()）生成反转后的列表。
要查看返回的这个迭代器的内容，需要迭代输出或者将其转化为列表

list.reverse() 是列表对象的方法，只能用于对列表进行原地反转。
示例：
"""

original_list = [1, 2, 3, 4, 5]
reversed_iterator = reversed(original_list)
print(list(reversed_iterator))  # 输出：[5, 4, 3, 2, 1]

# 使用 list.reverse() 方法
original_list.reverse()  # 直接反转原列表 是一个原地操作
print(original_list)  # 输出：[5, 4, 3, 2, 1]

"""sorted() 返回排序后的副本，不影响原对象；
list.sort() 在原地排序列表，改变原对象；
reversed() 或 list.reverse() 不是排序，而是反转序列元素的顺序
"""
