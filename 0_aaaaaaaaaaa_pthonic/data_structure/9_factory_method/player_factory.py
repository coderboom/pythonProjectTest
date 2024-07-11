print('----------------')
"""
作为abc模块的抽象基类一节的补充，带着大家先从一个传统的例子入手，发现其中的代码的坏味道，然后通过重构，引入工厂方法来管理实现了多态对象的优雅生成。
例子里面展现了Pythonic的工厂方法的设计与实现，既简单又优雅。
同时也向大家传递了“封闭原则”、“依赖注入”，“不变”的编程思想以及重构的时机的把控。
"""
from typing import Callable, Any
from player import Player

"""
这一行使用了类型注解（Type Annotation），它是 Python 3.5 及以后版本引入的特性，用于为变量、函数参数以及函数返回值指定静态类型。
    这样做有助于提高代码的可读性和可维护性，并能利用类型检查工具（如 mypy）进行静态类型检查。
    
在这个声明中：
    dict 是内置的字典类型。
    <str, Callable[..., Player]> 描述了字典的键值对类型：
    键（key）类型为 str，表示字典的键都是字符串。
    值（value）类型为 Callable[..., Player]，这是一个特殊的类型，表示字典的值都是可调用对象（如函数），这些可调用对象满足以下条件：
    接受任意数量（由省略号 ... 表示）和任意类型的参数（称为变长参数列表）。
    返回类型为 Player，即这些可调用对象在被调用后应返回一个 Player 类型的对象。
    
    声明一个名为 player_creation_functions 的字典变量，该字典的键为字符串类型，值为可接受任意参数并返回 Player 类型对象的可调用对象（通常是函数）。
        初始状态下，该字典为空。
    在实际应用中，这个字典可能用来存储各种创建 Player 类实例的工厂函数，每种函数可以通过其名称（作为字典的键）来访问和调用。例如：
"""
player_creation_functions: dict[str, Callable[..., Player]] = {}


def register(role: str, creation_function: Callable[..., Player]) -> None:
    player_creation_functions[role] = creation_function


def unregister(role: str) -> None:
    player_creation_functions.pop(role, None)


def create(args: dict[str, Any]) -> Player:
    """创建函数"""
    the_args = args.copy()
    role = the_args['role']
    try:
        create_function = player_creation_functions[role]
        return create_function(**the_args)
    except KeyError:
        raise ValueError(f"未知的角色{role!r}") from None
