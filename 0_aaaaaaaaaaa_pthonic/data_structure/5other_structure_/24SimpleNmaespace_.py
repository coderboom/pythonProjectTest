"""simplenamespace"""
from types import SimpleNamespace

"""
SimpleNamespace 是 Python types 模块中的一个类，它提供了一个简单的属性容器，类似于一个轻量级的字典或者对象。
    相比于直接使用字典，SimpleNamespace 允许你通过属性访问的方式来读写数据，这使得代码更加自然和易读。

types.SimpleNamespace 是在 Python 中创建数据对象的快捷方式。它提供了访问其命名空间的默认值，并将其所有key公开为类属性。
    默认情况下，所有实例还包含一个有意义的 __repr__。与空类相比，这提供了以下优点
    
* 它允许您在构造对象时初始化属性：sn = SimpleNamespace(a=1, b=2)。
* 它提供了一个可读的 repr()。
* 它会覆盖默认比较。它不是通过 id() 进行比较，而是比较属性值。
简而言之，types.SimpleNamespace 只是一个超简单的类，允许您设置、更改和删除属性，同时它还提供了一个不错的 repr 输出字符串。属性可以自由添加、修改和删除。


下面是对 SimpleNamespace 的详细解析：
定义与创建
要使用 SimpleNamespace，首先需要从 types 模块中导入它，然后像创建普通对象一样创建一个实例。
    你可以直接在实例化时设置属性值，或者之后通过点语法来设置和获取属性。
"""
# 创建一个 SimpleNamespace 对象
ns = SimpleNamespace()

# 设置属性
ns.name = "Alice"
ns.age = 30

# 访问属性
print(ns.name)  # 输出: Alice
print(ns.age)  # 输出: 30
"""动态属性
SimpleNamespace 支持动态添加属性，这意味着你可以在任何时候给它添加新的属性，就像操作普通对象一样。
"""
ns.country = "Wonderland"
print(ns.country)  # 输出: Wonderland

"""作为容器使用
由于其灵活性，SimpleNamespace 很适合作为小型配置对象或临时数据容器。它比定义一个完整的类更简洁，特别是在不需要复杂逻辑或方法的情况下。

与字典的比较
    访问方式：与字典不同，SimpleNamespace 使用点语法(.)访问属性，而字典使用键访问([])。
    动态性：两者都支持动态添加键/属性。
    性能：对于大量数据或频繁的键查找，字典通常更快，因为它们在内部进行了优化。
    可读性：SimpleNamespace 提供了更好的代码可读性和更少的语法噪音，尤其是在处理具有语义意义的属性时。
    
与 namedtuple 的比较
    动态性：SimpleNamespace 是完全动态的，而 namedtuple 在定义时就需要确定所有字段。
    性能：namedtuple 由于是元组的子类，因此在某些情况下可能比 SimpleNamespace 更高效，尤其是在属性数量固定且频繁访问时。
    结构化数据：如果你需要结构化的数据且字段固定，namedtuple 更合适；如果需要灵活的属性添加，则选择 SimpleNamespace。
    
实际应用场景
    快速原型设计：在编写原型或测试代码时，可以快速创建具有属性的对象，无需定义完整的类。
    配置管理：用于存储和传递配置参数，尤其是当这些参数需要以属性形式访问时。
    动态属性需求：当属性集不是预先确定的，或者需要根据运行时情况动态添加属性时。
    总的来说，SimpleNamespace 提供了一种简单、直观的方式来组织和访问数据，特别适合那些不需要复杂类结构的场景。
"""

ba = SimpleNamespace(abc='qeqweq', id=12313, bool_t=False, data={1, 2, 3, 4, 5, 6, 6})
print(ba.abc)

bc = SimpleNamespace(id=12313, bool_t=False, abc='qeqweq', data={1, 2, 3, 4, 5, 6, 6})
"""它不是通过 id() 进行比较，而是比较属性值。，所以ba=bc"""
print(ba == bc)  # True
# del ba.abc
print(ba)  # namespace(id=12313, bool_t=False, data={1, 2, 3, 4, 5, 6})

repr(bc)  # namespace(abc='qeqweq', id=12313, bool_t=False, data={1, 2, 3, 4, 5, 6})


class CustomSimpoleNamespace(SimpleNamespace):
    def __repr__(self):
        keys = sorted(self.__dict__)
        items = (f"{k}:{self.__dict__[k]}" for k in keys)
        return f"{type(self).__name__}({'，'.join(items)})"


data = CustomSimpoleNamespace(a=1, b=2, c=3)
print(data)
