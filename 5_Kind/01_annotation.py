"""类型注解
能让代码更加易读。类型注解又叫类型暗示，它将函数、变量声明为一种特定类型。并不是严格的类型绑定，所以这个机制并不能阻止跳动着传入不应该传入的参数，但是可以增强代码的可读性。

变量类型：在变量名后加一个冒号，冒号后跟写变量的数据类型
函数返回类型：方法参数中如有变量类型，则在参数括号后加一个箭头，箭头后为返回值的类型
"""

"""基本数据类型注解"""
x: int = 1
x: str = '13'
x: float = 1.0
x: bool = True
x: list = [1, 2, 3]
x: tuple = (1, 2, 3)
x: dict = {'a': 1, 'b': 2}
x: set = {1, 2, 3}
x: frozenset = frozenset({1, 2, 3})
x: bytes = b'123'
x: bytearray = bytearray(b'123')
x: memoryview = memoryview(b'123')
x: complex = 1 + 2j
x: range = range(1, 10, 2)
x: slice = slice(1, 10, 2)
x: type = int
x: object = object()

"""使用 | 表达联合类型(types.UnionType),表示几个类型均可"""
from typing import Union, Optional, Iterable

number: Union[int, float] = 1
number1: int | float = 10.2
print(type(int | float))  # <class 'types.UnionType'>

print((int | float) | str == int | float | str)  # 多次组合的结果会被平推
print(int | float | int == int | float)  # 两个相同类型的结果会自动合并
print(int | float == float | int)  # 比较时会忽略顺序
print(int | float == Union[int, float])  # 与Union类型一致
print(str | None == Optional[str])
# 在Python 3.10 及更高版本中，使用了类型提示（Type Hints）的概念。这里的 str | None 是指一个变量可以是字符串类型或者 None 类型，
# 这是Python的联合类型（Union Type）表示法。而 Optional[str] 是类型提示库 typing 中的一种特殊类型，它同样表示一个变量可能是 str 类型，也可能是 None 类型

"""容器类型注解
在容器后的方括号里按顺序注明
"""
x: list[int] = [1, 2, 3]
x: tuple[int, int, int] = (1, 2, 3)
x: tuple = (1, 2, 3)
x: set[float] = {1.9, 2.9, 3.9}
x: dict[str, int] = {'a': 1, 'b': 2}

# 对于可能为NOne的值，使用Optional类型
x: Optional[str] = '12'


# 函数注解
def func1(a: int, b: int) -> int:
    return a + b


"""鸭子类型注解"""
from typing import Mapping, MutableMapping, Sequence, Iterable


# 可迭代对象
def f(ints: Iterable[int]) -> list[int]:
    return [i for i in ints]


# 映射类型
def d(my_mapping: Mapping[str, int]) -> list[int]:
    return list(my_mapping.values())


# 可变映射类型
def dd(my_mapping: MutableMapping[str, int]) -> set[str]:
    return set(my_mapping.keys())
