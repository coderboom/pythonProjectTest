"""不可变集合"""

"""frozenset 是 Python 中的一种不可变集合数据类型。它是 set 的不可变版本，意味着一旦创建，你就不能更改其内容，包括添加、删除元素或清空集合。
    这使得 frozenset 成为哈希表的键或其它需要不可变性的场景的理想选择。
    
    不可变性：一旦创建，frozenset 的内容就不能被修改。
    哈希性：由于 frozenset 是不可变的，它可以被用作字典的键或者作为集合的元素。
    操作：尽管你不能直接修改 frozenset，但你可以对它们进行集合操作，如并集(|)、交集(&)、差集(-)和对称差集(^)，这些操作会返回新的 frozenset 对象。

以下是关于 frozenset 的一些关键点和使用示例：
"""
frozen_set_example = frozenset(["apple", "banana", "cherry"])
print(frozen_set_example)  # frozenset({'cherry', 'banana', 'apple'})

frozen_key = frozenset([1, 2, 3])
my_dict = {frozen_key: "This is a frozenset as a key."}
print(my_dict)  # {frozenset({1, 2, 3}): 'This is a frozenset as a key.'}

"""将字典的键拿出来，作为一个集合"""
books_map = {
    'name': 'python游戏编程',
    'author': 'Bobby',
    'start': 78,
    'publish_at': '2022-8-9',
    'info': {
        'alias': 'python game programming',
        'users': 10000,
        # 'id': 999999999999999
    }
}

frozen_dict_key = frozenset(books_map)
print(frozen_dict_key)  # frozenset({'start', 'info', 'author', 'publish_at', 'name'})

# frozen_dict_key.add('1231')  # AttributeError: 'frozenset' object has no attribute 'add'
