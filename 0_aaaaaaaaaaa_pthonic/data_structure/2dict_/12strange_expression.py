a = {True: 'apple', 1: 'orange', 1.0: 'banana'}
print(a)  # {True: 'banana'}
print(True == 1)  # True
print(True == 1.0)  # True
print(1 == 1.0)  # True
print(True == 1 == 1.0)  # True

"""在 Python 中，True、1 和 1.0 确实在逻辑上相等，且它们的哈希值相同。当用作字典的键时，这些值会被视为相等，因此后添加的键会覆盖前面的键。
    但具体哪个键保留在字典中，实际上取决于字典的内部处理方式，以及键被添加的顺序。

在这种情况下，当字典按 {True: 'apple', 1: 'orange', 1.0: 'banana'} 的顺序添加键值对时，
    每一个后续的键（尽管它们逻辑上相等）都覆盖了之前的值，但最终保留的键名则是最初的键名 True。
    因此，尽管 1 和 1.0 覆盖了之前的值，但字典的内部实现保留了第一次插入的键 True。
    这就是为什么最后的输出是 {True: 'banana'}。这个行为与 Python 的字典实现细节相关，可能会因为不同版本的 Python 有所不同。

总的来说，尽管 1 和 1.0 更新了对应的值，但字典最终显示的是第一次添加的键 True。
"""
b = {1: 'apple', True: 'orange', 1.0: 'banana'}
print(b)  # {1: 'banana'}
