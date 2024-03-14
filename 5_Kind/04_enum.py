"""枚举类型"""
"""Python 中的枚举类型（Enum）是一种特殊的类，它允许定义一组命名的常量集合。
    在 Python 3.4 版本中引入了标准库 enum 模块来支持枚举类型的创建和使用。
    通过枚举类型可以更好地组织代码、提高可读性，并且提供了一种形式化的方式来声明和处理有限的、预定义的离散值集合
"""
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


"""上述代码定义了一个名为 Color 的枚举类型，它有三个成员：RED、GREEN 和 BLUE，每个成员都有一个关联的整数值。
枚举成员特性：
唯一标识：枚举成员是唯一的，即使它们的值相同。————在比较操作时也是不相等的————
不可变：枚举成员的值在定义后不能被修改。————枚举名称不能重复，重复则会发生覆盖，后面的相当于前面的别名。————
名称与值：每个枚举成员有两个属性，一个是其名称（name），另一个是其值（value）。例如，Color.RED.name 是 'RED'，Color.RED.value 是 1。

-----
成员名称的唯一性： 枚举类中的每个成员名称都必须是唯一的。这意味着在同一枚举类内部，不能有重名的成员。
    例如，在一个表示季节的枚举类中，不可能同时存在两个 SPRING 成员。
成员值的默认唯一性（Python 3.4 及更高版本）： 默认情况下，从 Python 3.4 开始，枚举类中的成员值也要求是唯一的。
    也就是说，你不能有两个不同的成员具有相同的值。如果尝试给两个不同的枚举成员赋予相同的值，程序将会抛出 ValueError 异常。
    然而，在某些情况下，可以通过设置 Enum 的子类 IntEnum 或自定义元类等方法允许重复的数值，但这并不是标准枚举类型的默认行为。
    
总之，枚举类型确保了其成员能够通过名称或值（在默认设置下）唯一地标识和区分，从而提供了一种结构化的、安全的方式来表示一组固定的、不可变的选项集合。
----

枚举方法：
迭代：可以通过 for 循环遍历枚举的所有成员。
比较：枚举成员之间可以直接进行比较，根据它们在枚举中的定义顺序或者值进行比较。
查找：可以通过枚举类的方法 from_name() 或 from_value() 根据名称或值查找对应的枚举成员。
转换为字符串：调用枚举成员的 __str__() 方法会返回成员的名称。
子类化： Python 支持从 Enum 类派生出具有更复杂行为的枚举类型，比如 IntEnum（值为整数）、StrEnum（值为字符串）等。
自动赋值： 如果不指定枚举成员的值，默认情况下，它们会按照定义顺序自动分配递增的整数值。
类型安全： 在类型检查工具的支持下，枚举类型可以确保变量只能持有预定义的枚举成员，从而减少运行时错误。
用途举例： 枚举类型常见于需要明确列出所有可能状态或选项的地方，如日志级别、星期几、交通信号灯颜色、棋局状态等等。
枚举成员的访问： 可以通过点运算符直接访问枚举成员，如 Color.RED，并且在条件判断、函数参数、以及任何需要固定集合值的地方使用。
异常处理： 当尝试将非法值转换为枚举类型时，Python 会抛出 ValueError 异常。
总之，Python 中的枚举类型提供了结构化的数据管理方式，增强了代码的清晰性和可靠性，并在一定程度上保证了程序的安全性。
"""


class Season(Enum):
    """定义一个枚举类"""
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


def print_season(season_code: int):
    if season_code == Season.SPRING.value:
        print("SPRING")
    elif season_code == Season.SUMMER.value:
        print("SUMMER")
    elif season_code == Season.AUTUMN.value:
        print("AUTUMN")
    elif season_code == Season.WINTER.value:
        print("Winter")


print_season(2)
print_season(4)

"""Enum 定义了类似nametuple的接口，也是一个可调用对象，

第一个参数是枚举的名称，
    第二个参数用于给出枚举的成语啊吗，成员支持多种形式的数据。
"""
#  默认枚举值从1开始
Season = Enum('Season', 'SPRING SUMMER AUTUMN WINTER')
Season = Enum('Season', 'SPRING, SUMMER, AUTUMN, WINTER')
Season = Enum('Season', ('SPRING', 'SUMMER', 'AUTUMN', 'WINTER'))
Season = Enum('Season', ['SPRING', 'SUMMER', 'AUTUMN', 'WINTER'])

# 指定枚举值
Season = Enum('Season', [('SPRING', 1), ('SUMMER', 3), ('AUTUMN', 7), ('WINTER', 9)])
Season = Enum('Season', {'SPRING': 11, 'SUMMER': 22, 'AUTUMN': 33, 'WINTER': 44})

# 指定枚举起始值
Season = Enum('Season', ['SPRING', 'SUMMER', 'AUTUMN', 'WINTER'], start=20)

# 可迭代
for enum in Season:
    print(enum.name, enum.value)

Season1 = Enum('Season1', {'SPRING': 11, 'SUMMER': 22, 'AUTUMN': 33, 'WINTER': 44})
print(type(Season1), type(Season1.SUMMER))
print(Season1.SUMMER)
print(Season1.SUMMER.name, '----', Season1.SUMMER.value)  # SUMMER ---- 22
print(Season1(33), '---', Season1['WINTER'])  # Season.AUTUMN --- Season.WINTER

print(list(Season1))  # [<Season.SPRING: 11>, <Season.SUMMER: 22>, <Season.AUTUMN: 33>, <Season.WINTER: 44>]

# 特殊属性__members__是一个从名称到成员的只读有序映射
# 包含枚举中定义的所有成员，包括别名
"""__members__: 这是每个枚举类（如继承自 enum.Enum）的一个内置属性，它返回一个包含枚举成员名和其对应的枚举实例的字典。
    字典的键是枚举成员的名字（字符串），而值是实际的枚举实例对象。
"""
for enum, member in Season1.__members__.items():
    print(enum, ',', member, ',', member.name, ":", member.value)
"""
SPRING , Season1.SPRING , SPRING : 11
SUMMER , Season1.SUMMER , SUMMER : 22
AUTUMN , Season1.AUTUMN , AUTUMN : 33
WINTER , Season1.WINTER , WINTER : 44
"""

"""枚举成员之间可以按标识符进行比较，但是不能比较大小，枚举只有自己个自己是相等的，成员与成员、值与值都是不相等的。"""
print(Season1.SPRING == Season1.SPRING)
print(Season1.SPRING == Season1.SUMMER)
try:
    Season1.SPRING < Season1.SUMMER
except TypeError:
    print("不能比较枚举成员的值")

"""枚举值的唯一性
@unique 装饰器用于自动确保枚举类中的成员是唯一的。尽管从 Python 3.4 开始，
    所有通过 Enum 类创建的枚举默认都是唯一（即具有与 @unique 相同的效果），但在更早版本或为了显式强调这一特性时，可以明确使用 @unique 装饰器。
"""
from enum import Enum, unique


@unique
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# 尝试定义重复名称或值会抛出 ValueError 异常
# Color.RED = 4  # 这将引发异常，因为无法更改已存在的枚举成员的值
# Color.YELLOW = 1  # 这也会引发异常，因为1这个值已经与Color.RED关联
print('--------------------------')


class Season11(Enum):
    """定义一个枚举类"""
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4
    AAAAAA = 1


for color in Season11:
    print(color.name, color.value)

print('--------------------------')

from enum import unique


@unique
class Season111(Enum):
    """定义一个枚举类"""
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4
    # AAAAAA = 1  # 这将引发异常，因为1这个值已经与Color.RED关联


for color in Season111:
    print(color.name, color.value)
